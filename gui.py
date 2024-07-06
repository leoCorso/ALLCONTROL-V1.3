# -*- coding: utf-8 -*-
import time

################################################################################
## Form generated from reading UI file 'mainWindowGVnCpS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import ServerDatabase
import threading
import resources_rc
import re

class Ui_ALLCONTROL_SERVER(QMainWindow):

    databaseHandle = ServerDatabase.DataBase()
    commandParametersForm = dict()  # Holds a key with an associated list value. The lists are [QWidgets, Parametervalues
    databaseViewPaneImages = []

    def __init__(self):
        super().__init__()
        self.font = QFont()
        self.font.setFamily(u"Segoe UI Black")
        self.font.setPointSize(16)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.setupUi()


    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"ALLCONTROL_SERVER")
        self.resize(1676, 1074)
        icon = QIcon()
        icon.addFile(u":/icon/images/ALLCONTROL LOGO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QWidget(self)
        self.commandParameterValuesDict = {}

#-------- Paste update here ----------------------------------------------------------------------------------------------------------------------------------------------------
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(30, 18, 1611, 1011))
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tabs.setFont(font)
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setTabShape(QTabWidget.Rounded)
        self.tabs.setElideMode(Qt.ElideNone)
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(False)
        self.tabs.setMovable(True)
        self.tabs.setTabBarAutoHide(False)
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.Dashboard.setFont(font)
        self.verticalLayoutWidget_2 = QWidget(self.Dashboard)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(430, 310, 371, 311))
        self.keyloggerServerGrid = QVBoxLayout(self.verticalLayoutWidget_2)
        self.keyloggerServerGrid.setObjectName(u"keyloggerServerGrid")
        self.keyloggerServerGrid.setContentsMargins(0, 0, 0, 0)
        self.keyloggerServerConnectedLabel = QLabel(self.verticalLayoutWidget_2)
        self.keyloggerServerConnectedLabel.setObjectName(u"keyloggerServerConnectedLabel")

        self.keyloggerServerGrid.addWidget(self.keyloggerServerConnectedLabel)

        self.connectedClientsKeyloggerServer = QTableWidget(self.verticalLayoutWidget_2)
        if (self.connectedClientsKeyloggerServer.columnCount() < 3):
            self.connectedClientsKeyloggerServer.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.connectedClientsKeyloggerServer.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.connectedClientsKeyloggerServer.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.connectedClientsKeyloggerServer.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.connectedClientsKeyloggerServer.setObjectName(u"connectedClientsKeyloggerServer")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Black")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.connectedClientsKeyloggerServer.setFont(font1)
        self.connectedClientsKeyloggerServer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.connectedClientsKeyloggerServer.setSortingEnabled(True)

        self.keyloggerServerGrid.addWidget(self.connectedClientsKeyloggerServer)

        self.verticalLayoutWidget_3 = QWidget(self.Dashboard)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(820, 310, 771, 311))
        self.infectedClientsGrid = QVBoxLayout(self.verticalLayoutWidget_3)
        self.infectedClientsGrid.setObjectName(u"infectedClientsGrid")
        self.infectedClientsGrid.setContentsMargins(0, 0, 0, 0)
        self.infectedClientsLabel = QLabel(self.verticalLayoutWidget_3)
        self.infectedClientsLabel.setObjectName(u"infectedClientsLabel")

        self.infectedClientsGrid.addWidget(self.infectedClientsLabel)

        self.infectedClients = QTableWidget(self.verticalLayoutWidget_3)
        if (self.infectedClients.columnCount() < 17):
            self.infectedClients.setColumnCount(17)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(15, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.infectedClients.setHorizontalHeaderItem(16, __qtablewidgetitem19)
        self.infectedClients.setObjectName(u"infectedClients")
        self.infectedClients.setFont(font)
        self.infectedClients.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.infectedClients.setSortingEnabled(True)
        self.infectedClients.horizontalHeader().setCascadingSectionResizes(False)
        self.infectedClients.horizontalHeader().setMinimumSectionSize(56)
        self.infectedClients.horizontalHeader().setDefaultSectionSize(100)

        self.infectedClientsGrid.addWidget(self.infectedClients)

        self.verticalLayoutWidget = QWidget(self.Dashboard)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 310, 391, 311))
        self.commandServerGrid = QVBoxLayout(self.verticalLayoutWidget)
        self.commandServerGrid.setObjectName(u"commandServerGrid")
        self.commandServerGrid.setContentsMargins(0, 0, 0, 0)
        self.commandServerConnectedLabel = QLabel(self.verticalLayoutWidget)
        self.commandServerConnectedLabel.setObjectName(u"commandServerConnectedLabel")

        self.commandServerGrid.addWidget(self.commandServerConnectedLabel)

        self.connectedClientsCommandServer = QTableWidget(self.verticalLayoutWidget)
        if (self.connectedClientsCommandServer.columnCount() < 3):
            self.connectedClientsCommandServer.setColumnCount(3)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.connectedClientsCommandServer.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.connectedClientsCommandServer.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.connectedClientsCommandServer.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        self.connectedClientsCommandServer.setObjectName(u"connectedClientsCommandServer")
        self.connectedClientsCommandServer.setFont(font1)
        self.connectedClientsCommandServer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.connectedClientsCommandServer.setSortingEnabled(True)

        self.commandServerGrid.addWidget(self.connectedClientsCommandServer)

        self.verticalLayoutWidget_4 = QWidget(self.Dashboard)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(20, 90, 561, 191))
        self.infoGrid = QVBoxLayout(self.verticalLayoutWidget_4)
        self.infoGrid.setObjectName(u"infoGrid")
        self.infoGrid.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(0)
        self.label.setIndent(0)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.infoGrid.addWidget(self.label)

        self.infoTable = QTableWidget(self.verticalLayoutWidget_4)
        if (self.infoTable.columnCount() < 1):
            self.infoTable.setColumnCount(1)
        if (self.infoTable.rowCount() < 4):
            self.infoTable.setRowCount(4)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(3, __qtablewidgetitem26)
        self.infoTable.setObjectName(u"infoTable")
        self.infoTable.setFont(font)
        self.infoTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.infoTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.infoTable.setAlternatingRowColors(True)
        self.infoTable.setSortingEnabled(True)
        self.infoTable.setRowCount(4)
        self.infoTable.setColumnCount(1)
        self.infoTable.horizontalHeader().setVisible(False)
        self.infoTable.horizontalHeader().setCascadingSectionResizes(False)
        self.infoTable.horizontalHeader().setDefaultSectionSize(100)
        self.infoTable.horizontalHeader().setHighlightSections(True)
        self.infoTable.horizontalHeader().setStretchLastSection(True)
        self.infoTable.verticalHeader().setVisible(True)
        self.infoTable.verticalHeader().setCascadingSectionResizes(False)
        self.infoTable.verticalHeader().setHighlightSections(True)
        self.infoTable.verticalHeader().setStretchLastSection(False)

        self.infoGrid.addWidget(self.infoTable)

        self.verticalLayoutWidget_5 = QWidget(self.Dashboard)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(610, 90, 971, 191))
        self.securityInfoGrid = QVBoxLayout(self.verticalLayoutWidget_5)
        self.securityInfoGrid.setObjectName(u"securityInfoGrid")
        self.securityInfoGrid.setContentsMargins(0, 0, 0, 0)
        self.securityLabel = QLabel(self.verticalLayoutWidget_5)
        self.securityLabel.setObjectName(u"securityLabel")

        self.securityInfoGrid.addWidget(self.securityLabel)

        self.securityTable = QTableWidget(self.verticalLayoutWidget_5)
        if (self.securityTable.columnCount() < 2):
            self.securityTable.setColumnCount(2)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.securityTable.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.securityTable.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        self.securityTable.setObjectName(u"securityTable")
        self.securityTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.securityTable.setAlternatingRowColors(True)
        self.securityTable.setSortingEnabled(True)
        self.securityTable.setRowCount(0)
        self.securityTable.setColumnCount(2)
        self.securityTable.horizontalHeader().setVisible(False)
        self.securityTable.horizontalHeader().setCascadingSectionResizes(False)
        self.securityTable.horizontalHeader().setDefaultSectionSize(100)
        self.securityTable.horizontalHeader().setHighlightSections(True)
        self.securityTable.horizontalHeader().setStretchLastSection(True)
        self.securityTable.verticalHeader().setVisible(False)
        self.securityTable.verticalHeader().setHighlightSections(True)

        self.securityInfoGrid.addWidget(self.securityTable)

        self.verticalLayoutWidget_6 = QWidget(self.Dashboard)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(20, 640, 1571, 311))
        self.logsGrid = QVBoxLayout(self.verticalLayoutWidget_6)
        self.logsGrid.setObjectName(u"logsGrid")
        self.logsGrid.setContentsMargins(0, 0, 0, 0)
        self.logsLabel = QLabel(self.verticalLayoutWidget_6)
        self.logsLabel.setObjectName(u"logsLabel")

        self.logsGrid.addWidget(self.logsLabel)

        self.logsTable = QTableWidget(self.verticalLayoutWidget_6)
        if (self.logsTable.columnCount() < 3):
            self.logsTable.setColumnCount(3)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.logsTable.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.logsTable.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.logsTable.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        self.logsTable.setObjectName(u"logsTable")
        self.logsTable.setFont(font1)
        self.logsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.logsTable.setGridStyle(Qt.DashLine)
        self.logsTable.setSortingEnabled(True)
        self.logsTable.horizontalHeader().setMinimumSectionSize(44)
        self.logsTable.horizontalHeader().setDefaultSectionSize(117)
        self.logsTable.horizontalHeader().setStretchLastSection(True)
        self.logsTable.verticalHeader().setStretchLastSection(False)

        self.logsGrid.addWidget(self.logsTable)

        self.bannerLabel = QLabel(self.Dashboard)
        self.bannerLabel.setObjectName(u"bannerLabel")
        self.bannerLabel.setGeometry(QRect(690, 0, 181, 91))
        self.bannerLabel.setPixmap(QPixmap(u":/banner/images/ALLCONTROL Banner.png"))
        self.bannerLabel.setScaledContents(True)
        self.airplaneModeButton = QPushButton(self.Dashboard)
        self.airplaneModeButton.setObjectName(u"airplaneModeButton")
        self.airplaneModeButton.setGeometry(QRect(1250, 30, 171, 61))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Black")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.airplaneModeButton.setFont(font2)
        self.airplaneModeButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/images/Airplane mode.png", QSize(), QIcon.Normal, QIcon.Off)
        self.airplaneModeButton.setIcon(icon1)
        self.airplaneModeButton.setIconSize(QSize(25, 25))
        self.tabs.addTab(self.Dashboard, "")
        self.Operations = QWidget()
        self.Operations.setObjectName(u"Operations")
        self.connectedClientsSearch = QFrame(self.Operations)
        self.connectedClientsSearch.setObjectName(u"connectedClientsSearch")
        self.connectedClientsSearch.setGeometry(QRect(10, 20, 1581, 391))
        self.connectedClientsSearch.setFrameShape(QFrame.StyledPanel)
        self.connectedClientsSearch.setFrameShadow(QFrame.Plain)
        self.verticalLayoutWidget_8 = QWidget(self.connectedClientsSearch)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 10, 1261, 291))
        self.connectedClientsGrid = QVBoxLayout(self.verticalLayoutWidget_8)
        self.connectedClientsGrid.setObjectName(u"connectedClientsGrid")
        self.connectedClientsGrid.setContentsMargins(0, 0, 0, 0)
        self.connectedClientsLabel = QLabel(self.verticalLayoutWidget_8)
        self.connectedClientsLabel.setObjectName(u"connectedClientsLabel")
        self.connectedClientsLabel.setFont(font)
        self.connectedClientsLabel.setTextFormat(Qt.AutoText)

        self.connectedClientsGrid.addWidget(self.connectedClientsLabel)

        self.connectedClients = QTableWidget(self.verticalLayoutWidget_8)
        if (self.connectedClients.columnCount() < 17):
            self.connectedClients.setColumnCount(17)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(5, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(6, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(7, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(8, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(9, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(10, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(11, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(12, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(13, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(14, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(15, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.connectedClients.setHorizontalHeaderItem(16, __qtablewidgetitem48)
        self.connectedClients.setObjectName(u"connectedClients")
        self.connectedClients.setFont(font)
        self.connectedClients.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.connectedClients.setSortingEnabled(True)

        self.connectedClientsGrid.addWidget(self.connectedClients)

        self.filterFrame = QFrame(self.connectedClientsSearch)
        self.filterFrame.setObjectName(u"filterFrame")
        self.filterFrame.setGeometry(QRect(10, 310, 993, 63))
        self.filterFrame.setMaximumSize(QSize(16777215, 16777215))
        self.filterFrame.setSizeIncrement(QSize(0, 0))
        self.filterFrame.setFrameShape(QFrame.StyledPanel)
        self.filterFrame.setFrameShadow(QFrame.Plain)
        self.valueLabel = QLabel(self.filterFrame)
        self.valueLabel.setObjectName(u"valueLabel")
        self.valueLabel.setGeometry(QRect(350, 9, 71, 41))
        self.valueLabel.setFont(font)
        self.valueLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.fieldLabel = QLabel(self.filterFrame)
        self.fieldLabel.setObjectName(u"fieldLabel")
        self.fieldLabel.setGeometry(QRect(10, 4, 61, 51))
        self.fieldLabel.setFont(font)
        self.fieldLabel.setMouseTracking(False)
        self.fieldLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.applyButton = QPushButton(self.filterFrame)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setGeometry(QRect(850, 14, 121, 38))
        self.applyButton.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icon/images/filter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.applyButton.setIcon(icon2)
        self.applyButton.setIconSize(QSize(25, 25))
        self.fieldComboBox = QComboBox(self.filterFrame)
        self.fieldComboBox.setObjectName(u"fieldComboBox")
        self.fieldComboBox.setGeometry(QRect(80, 14, 245, 36))
        self.fieldComboBox.setFont(font)
        self.textEdit = QTextEdit(self.filterFrame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(430, 14, 401, 37))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Black")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.textEdit.setFont(font3)
        self.verticalLayoutWidget_7 = QWidget(self.connectedClientsSearch)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(1290, 10, 271, 291))
        self.ScheduledCommandsGrid = QVBoxLayout(self.verticalLayoutWidget_7)
        self.ScheduledCommandsGrid.setObjectName(u"ScheduledCommandsGrid")
        self.ScheduledCommandsGrid.setContentsMargins(0, 0, 0, 0)
        self.scheduledCommandsLabel = QLabel(self.verticalLayoutWidget_7)
        self.scheduledCommandsLabel.setObjectName(u"scheduledCommandsLabel")
        self.scheduledCommandsLabel.setFont(font)

        self.ScheduledCommandsGrid.addWidget(self.scheduledCommandsLabel)

        self.scheduledCommands = QTableView(self.verticalLayoutWidget_7)
        self.scheduledCommands.setObjectName(u"scheduledCommands")
        self.scheduledCommands.setFont(font)
        self.scheduledCommands.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.scheduledCommands.setSortingEnabled(True)

        self.ScheduledCommandsGrid.addWidget(self.scheduledCommands)

        self.optionsGroupBox = QGroupBox(self.Operations)
        self.optionsGroupBox.setObjectName(u"optionsGroupBox")
        self.optionsGroupBox.setGeometry(QRect(11, 560, 651, 101))
        self.optionsGroupBox.setFont(font)
        self.sendToAllCheckBox = QCheckBox(self.optionsGroupBox)
        self.sendToAllCheckBox.setObjectName(u"sendToAllCheckBox")
        self.sendToAllCheckBox.setGeometry(QRect(500, 46, 131, 31))
        self.sendToAllCheckBox.setFont(font)
        self.targetClientIDComboBox = QComboBox(self.optionsGroupBox)
        self.targetClientIDComboBox.setObjectName(u"targetClientIDComboBox")
        self.targetClientIDComboBox.setGeometry(QRect(240, 44, 231, 35))
        self.targetClientIDComboBox.setFont(font)
        self.targetLabel = QLabel(self.optionsGroupBox)
        self.targetLabel.setObjectName(u"targetLabel")
        self.targetLabel.setGeometry(QRect(40, 35, 191, 51))
        self.targetLabel.setFont(font)
        self.commandGroupBox = QGroupBox(self.Operations)
        self.commandGroupBox.setObjectName(u"commandGroupBox")
        self.commandGroupBox.setGeometry(QRect(20, 430, 1581, 101))
        self.commandGroupBox.setFont(font)
        self.commandNameLabel = QLabel(self.commandGroupBox)
        self.commandNameLabel.setObjectName(u"commandNameLabel")
        self.commandNameLabel.setGeometry(QRect(2, 21, 122, 79))
        self.commandNameLabel.setFont(font)
        self.commandNameLabel.setTextFormat(Qt.AutoText)
        self.commandNameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.commandDescriptionLabel = QLabel(self.commandGroupBox)
        self.commandDescriptionLabel.setObjectName(u"commandDescriptionLabel")
        self.commandDescriptionLabel.setGeometry(QRect(381, 20, 131, 79))
        self.commandDescriptionLabel.setFont(font)
        self.commandDescriptionLabel.setTextFormat(Qt.AutoText)
        self.commandDescriptionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.commandNameComboBox = QComboBox(self.commandGroupBox)
        self.commandNameComboBox.setObjectName(u"commandNameComboBox")
        self.commandNameComboBox.setGeometry(QRect(130, 45, 231, 36))
        self.commandNameComboBox.setFont(font)
        self.noiseLevelLabel = QLabel(self.commandGroupBox)
        self.noiseLevelLabel.setObjectName(u"noiseLevelLabel")
        self.noiseLevelLabel.setGeometry(QRect(760, 20, 131, 79))
        self.noiseLevelLabel.setFont(font)
        self.noiseLevelLabel.setTextFormat(Qt.AutoText)
        self.noiseLevelLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sendCommandButton = QPushButton(self.commandGroupBox)
        self.sendCommandButton.setObjectName(u"sendCommandButton")
        self.sendCommandButton.setGeometry(QRect(1340, 40, 131, 41))
        self.sendCommandButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icon/images/Send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sendCommandButton.setIcon(icon3)
        self.sendCommandButton.setIconSize(QSize(50, 50))
        self.commandDescriptionBrowser = QPlainTextEdit(self.commandGroupBox)
        self.commandDescriptionBrowser.setObjectName(u"commandDescriptionBrowser")
        self.commandDescriptionBrowser.setGeometry(QRect(520, 24, 231, 66))
        self.noiseLevel = QPlainTextEdit(self.commandGroupBox)
        self.noiseLevel.setObjectName(u"noiseLevel")
        self.noiseLevel.setGeometry(QRect(896, 34, 65, 48))
        self.commandMediaPreview = QFrame(self.Operations)
        self.commandMediaPreview.setObjectName(u"commandMediaPreview")
        self.commandMediaPreview.setGeometry(QRect(710, 570, 640, 360))
        self.commandMediaPreview.setAutoFillBackground(True)
        self.commandMediaPreview.setFrameShape(QFrame.StyledPanel)
        self.commandMediaPreview.setFrameShadow(QFrame.Plain)
        self.commandMediaImageLabel = QLabel(self.commandMediaPreview)
        self.commandMediaImageLabel.setObjectName(u"commandMediaImageLabel")
        self.commandMediaImageLabel.setGeometry(QRect(-3, -2, 641, 361))
        self.commandPreviewControlsGroupbox = QGroupBox(self.Operations)
        self.commandPreviewControlsGroupbox.setObjectName(u"commandPreviewControlsGroupbox")
        self.commandPreviewControlsGroupbox.setGeometry(QRect(1370, 570, 51, 131))
        self.nextMediaImageButton = QPushButton(self.commandPreviewControlsGroupbox)
        self.nextMediaImageButton.setObjectName(u"nextMediaImageButton")
        self.nextMediaImageButton.setGeometry(QRect(5, 5, 41, 41))
        icon4 = QIcon()
        icon4.addFile(u":/icon/images/next right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextMediaImageButton.setIcon(icon4)
        self.nextMediaImageButton.setIconSize(QSize(25, 25))
        self.previousMediaImageButton = QPushButton(self.commandPreviewControlsGroupbox)
        self.previousMediaImageButton.setObjectName(u"previousMediaImageButton")
        self.previousMediaImageButton.setGeometry(QRect(5, 44, 41, 41))
        icon5 = QIcon()
        icon5.addFile(u":/icon/images/next left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previousMediaImageButton.setIcon(icon5)
        self.previousMediaImageButton.setIconSize(QSize(25, 25))
        self.fullscreenImageButton = QPushButton(self.commandPreviewControlsGroupbox)
        self.fullscreenImageButton.setObjectName(u"fullscreenImageButton")
        self.fullscreenImageButton.setGeometry(QRect(5, 83, 41, 41))
        icon6 = QIcon()
        icon6.addFile(u":/icon/images/full screen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreenImageButton.setIcon(icon6)
        self.fullscreenImageButton.setIconSize(QSize(25, 25))
        self.tabs.addTab(self.Operations, "")
        self.database = QWidget()
        self.database.setObjectName(u"database")
        self.databaseViewTable = QTableWidget(self.database)
        self.databaseViewTable.setObjectName(u"databaseViewTable")
        self.databaseViewTable.setGeometry(QRect(30, 30, 841, 841))
        self.databaseViewTable.setFont(font)
        self.databaseViewTable.setStyleSheet(u"")
        self.databaseViewTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.databaseViewTable.setAlternatingRowColors(True)
        self.databaseViewTable.setSortingEnabled(True)
        self.databaseTableFrame = QFrame(self.database)
        self.databaseTableFrame.setObjectName(u"databaseTableFrame")
        self.databaseTableFrame.setGeometry(QRect(570, 890, 461, 61))
        self.databaseTableFrame.setFrameShape(QFrame.StyledPanel)
        self.databaseTableFrame.setFrameShadow(QFrame.Raised)
        self.tableDatabaseLabel = QLabel(self.databaseTableFrame)
        self.tableDatabaseLabel.setObjectName(u"tableDatabaseLabel")
        self.tableDatabaseLabel.setGeometry(QRect(10, 10, 71, 41))
        self.tableDatabaseLabel.setFont(font)
        self.tableDatabaseCombobox = QComboBox(self.databaseTableFrame)
        self.tableDatabaseCombobox.setObjectName(u"tableDatabaseCombobox")
        self.tableDatabaseCombobox.setGeometry(QRect(90, 10, 301, 41))
        self.tableDatabaseCombobox.setFont(font)
        self.refreshTableViewButton = QPushButton(self.databaseTableFrame)
        self.refreshTableViewButton.setObjectName(u"refreshTableViewButton")
        self.refreshTableViewButton.setGeometry(QRect(400, 10, 51, 43))
        icon7 = QIcon()
        icon7.addFile(u":/icon/images/Refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshTableViewButton.setIcon(icon7)
        self.refreshTableViewButton.setIconSize(QSize(25, 25))
        self.databasePreviewFrame = QFrame(self.database)
        self.databasePreviewFrame.setObjectName(u"databasePreviewFrame")
        self.databasePreviewFrame.setGeometry(QRect(900, 30, 691, 841))
        self.databasePreviewFrame.setFrameShape(QFrame.StyledPanel)
        self.databasePreviewFrame.setFrameShadow(QFrame.Plain)
        self.databaseMediaPreviewFrame = QFrame(self.databasePreviewFrame)
        self.databaseMediaPreviewFrame.setObjectName(u"databaseMediaPreviewFrame")
        self.databaseMediaPreviewFrame.setGeometry(QRect(20, 20, 641, 361))
        self.databaseMediaPreviewFrame.setFrameShape(QFrame.StyledPanel)
        self.databaseMediaPreviewFrame.setFrameShadow(QFrame.Plain)
        self.imagePreviewLabel = QLabel(self.databaseMediaPreviewFrame)
        self.imagePreviewLabel.setObjectName(u"imagePreviewLabel")
        self.imagePreviewLabel.setGeometry(QRect(0, 0, 640, 360))
        self.keylogPreviewTBrowser = QTextBrowser(self.databaseMediaPreviewFrame)
        self.keylogPreviewTBrowser.setObjectName(u"keylogPreviewTBrowser")
        self.keylogPreviewTBrowser.setGeometry(QRect(-5, 0, 651, 362))
        self.keylogPreviewTBrowser.setFont(font2)
        self.keylogPreviewTBrowser.setOpenLinks(False)
        self.databaseMediaButtonsFrame = QFrame(self.databasePreviewFrame)
        self.databaseMediaButtonsFrame.setObjectName(u"databaseMediaButtonsFrame")
        self.databaseMediaButtonsFrame.setGeometry(QRect(20, 390, 641, 71))
        self.databaseMediaButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.databaseMediaButtonsFrame.setFrameShadow(QFrame.Raised)
        self.previousDatabaseImageButton = QPushButton(self.databaseMediaButtonsFrame)
        self.previousDatabaseImageButton.setObjectName(u"previousDatabaseImageButton")
        self.previousDatabaseImageButton.setGeometry(QRect(512, 16, 41, 41))
        self.previousDatabaseImageButton.setIcon(icon5)
        self.previousDatabaseImageButton.setIconSize(QSize(25, 25))
        self.nextDatabaseImageButton = QPushButton(self.databaseMediaButtonsFrame)
        self.nextDatabaseImageButton.setObjectName(u"nextDatabaseImageButton")
        self.nextDatabaseImageButton.setGeometry(QRect(551, 16, 41, 41))
        self.nextDatabaseImageButton.setIcon(icon4)
        self.nextDatabaseImageButton.setIconSize(QSize(25, 25))
        self.fullscreenDatabaseButton = QPushButton(self.databaseMediaButtonsFrame)
        self.fullscreenDatabaseButton.setObjectName(u"fullscreenDatabaseButton")
        self.fullscreenDatabaseButton.setGeometry(QRect(590, 16, 41, 41))
        self.fullscreenDatabaseButton.setIcon(icon6)
        self.fullscreenDatabaseButton.setIconSize(QSize(25, 25))
        self.databaseImageDataCapturedLabel = QLabel(self.databaseMediaButtonsFrame)
        self.databaseImageDataCapturedLabel.setObjectName(u"databaseImageDataCapturedLabel")
        self.databaseImageDataCapturedLabel.setGeometry(QRect(10, 10, 161, 51))
        self.databaseImageDataCapturedLabel.setFont(font3)
        self.databaseImageCaptureDateEdit = QTextBrowser(self.databaseMediaButtonsFrame)
        self.databaseImageCaptureDateEdit.setObjectName(u"databaseImageCaptureDateEdit")
        self.databaseImageCaptureDateEdit.setGeometry(QRect(159, 18, 348, 38))
        self.databaseImageCaptureDateEdit.setFont(font)
        self.databaseImageCaptureDateEdit.setOpenLinks(False)
        self.deleteDatabaseRowButton = QPushButton(self.database)
        self.deleteDatabaseRowButton.setObjectName(u"deleteDatabaseRowButton")
        self.deleteDatabaseRowButton.setGeometry(QRect(30, 880, 41, 41))
        icon8 = QIcon()
        icon8.addFile(u":/icon/images/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteDatabaseRowButton.setIcon(icon8)
        self.deleteDatabaseRowButton.setIconSize(QSize(30, 30))
        self.rowCountBrowser = QTextBrowser(self.database)
        self.rowCountBrowser.setObjectName(u"rowCountBrowser")
        self.rowCountBrowser.setGeometry(QRect(189, 881, 201, 39))
        self.rowCountBrowser.setFont(font)
        self.rowCountLabel = QLabel(self.database)
        self.rowCountLabel.setObjectName(u"rowCountLabel")
        self.rowCountLabel.setGeometry(QRect(80, 884, 121, 31))
        self.rowCountLabel.setFont(font3)
        self.tabs.addTab(self.database, "")
        self.Configurations = QWidget()
        self.Configurations.setObjectName(u"Configurations")
        self.enableDisableServerGroupBox = QGroupBox(self.Configurations)
        self.enableDisableServerGroupBox.setObjectName(u"enableDisableServerGroupBox")
        self.enableDisableServerGroupBox.setGeometry(QRect(480, 20, 521, 111))
        self.enableDisableServerGroupBox.setFont(font)
        self.enableDisableServerGroupBox.setAlignment(Qt.AlignCenter)
        self.commandServerCheckBox = QCheckBox(self.enableDisableServerGroupBox)
        self.commandServerCheckBox.setObjectName(u"commandServerCheckBox")
        self.commandServerCheckBox.setGeometry(QRect(50, 50, 201, 41))
        self.commandServerCheckBox.setFont(font)
        self.commandServerCheckBox.setIconSize(QSize(16, 16))
        self.commandServerCheckBox.setTristate(False)
        self.keyloggerServerCheckBox = QCheckBox(self.enableDisableServerGroupBox)
        self.keyloggerServerCheckBox.setObjectName(u"keyloggerServerCheckBox")
        self.keyloggerServerCheckBox.setGeometry(QRect(280, 50, 201, 41))
        self.keyloggerServerCheckBox.setFont(font)
        self.switchesGroupbox = QGroupBox(self.Configurations)
        self.switchesGroupbox.setObjectName(u"switchesGroupbox")
        self.switchesGroupbox.setGeometry(QRect(40, 690, 541, 211))
        self.switchesGroupbox.setFont(font)
        self.clientKeyloggerEnabledCheckbox = QCheckBox(self.switchesGroupbox)
        self.clientKeyloggerEnabledCheckbox.setObjectName(u"clientKeyloggerEnabledCheckbox")
        self.clientKeyloggerEnabledCheckbox.setGeometry(QRect(30, 60, 221, 31))
        self.clientKeyloggerEnabledCheckbox.setFont(font)
        self.clientKeyloggerEnabledCheckbox.setCheckable(True)
        self.dataServerEnabledCheckbox = QCheckBox(self.switchesGroupbox)
        self.dataServerEnabledCheckbox.setObjectName(u"dataServerEnabledCheckbox")
        self.dataServerEnabledCheckbox.setGeometry(QRect(30, 110, 231, 31))
        self.dataServerEnabledCheckbox.setFont(font)
        self.dataServerEnabledCheckbox.setCheckable(True)
        self.favoriteCheckbox = QCheckBox(self.switchesGroupbox)
        self.favoriteCheckbox.setObjectName(u"favoriteCheckbox")
        self.favoriteCheckbox.setGeometry(QRect(30, 160, 231, 31))
        self.favoriteCheckbox.setFont(font)
        self.informationGroupbox = QGroupBox(self.Configurations)
        self.informationGroupbox.setObjectName(u"informationGroupbox")
        self.informationGroupbox.setGeometry(QRect(590, 690, 971, 271))
        self.informationGroupbox.setFont(font)
        self.clientIdTextbox = QPlainTextEdit(self.informationGroupbox)
        self.clientIdTextbox.setObjectName(u"clientIdTextbox")
        self.clientIdTextbox.setGeometry(QRect(120, 40, 91, 41))
        self.clientIdTextbox.setFont(font)
        self.clientIdTextbox.setReadOnly(True)
        self.cleintIdLabel = QLabel(self.informationGroupbox)
        self.cleintIdLabel.setObjectName(u"cleintIdLabel")
        self.cleintIdLabel.setGeometry(QRect(-10, 30, 131, 61))
        self.cleintIdLabel.setFont(font)
        self.cleintIdLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cleintIdLabel.setWordWrap(True)
        self.sIdLabel = QLabel(self.informationGroupbox)
        self.sIdLabel.setObjectName(u"sIdLabel")
        self.sIdLabel.setGeometry(QRect(240, 30, 51, 61))
        self.sIdLabel.setFont(font)
        self.sIdLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sIdLabel.setWordWrap(True)
        self.sIdTextBox = QPlainTextEdit(self.informationGroupbox)
        self.sIdTextBox.setObjectName(u"sIdTextBox")
        self.sIdTextBox.setGeometry(QRect(290, 40, 291, 41))
        self.sIdTextBox.setFont(font)
        self.sIdTextBox.setReadOnly(True)
        self.networkUsernameTextbox = QPlainTextEdit(self.informationGroupbox)
        self.networkUsernameTextbox.setObjectName(u"networkUsernameTextbox")
        self.networkUsernameTextbox.setGeometry(QRect(240, 170, 261, 41))
        self.networkUsernameTextbox.setFont(font)
        self.networkUsernameTextbox.setReadOnly(True)
        self.networkUsernameLabel = QLabel(self.informationGroupbox)
        self.networkUsernameLabel.setObjectName(u"networkUsernameLabel")
        self.networkUsernameLabel.setGeometry(QRect(26, 170, 211, 31))
        self.networkUsernameLabel.setFont(font)
        self.networkUsernameLabel.setAlignment(Qt.AlignCenter)
        self.networkUsernameLabel.setWordWrap(False)
        self.windowUsernameTextbox = QPlainTextEdit(self.informationGroupbox)
        self.windowUsernameTextbox.setObjectName(u"windowUsernameTextbox")
        self.windowUsernameTextbox.setGeometry(QRect(240, 110, 261, 41))
        self.windowUsernameTextbox.setFont(font)
        self.windowUsernameTextbox.setReadOnly(True)
        self.windowsUsernameLabel = QLabel(self.informationGroupbox)
        self.windowsUsernameLabel.setObjectName(u"windowsUsernameLabel")
        self.windowsUsernameLabel.setGeometry(QRect(26, 100, 221, 61))
        self.windowsUsernameLabel.setFont(font)
        self.windowsUsernameLabel.setAlignment(Qt.AlignCenter)
        self.windowsUsernameLabel.setWordWrap(False)
        self.macaddressLabel = QLabel(self.informationGroupbox)
        self.macaddressLabel.setObjectName(u"macaddressLabel")
        self.macaddressLabel.setGeometry(QRect(520, 100, 151, 61))
        self.macaddressLabel.setFont(font)
        self.macaddressLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.macaddressLabel.setWordWrap(False)
        self.macaddressTextbox = QPlainTextEdit(self.informationGroupbox)
        self.macaddressTextbox.setObjectName(u"macaddressTextbox")
        self.macaddressTextbox.setGeometry(QRect(670, 110, 271, 41))
        self.macaddressTextbox.setFont(font)
        self.macaddressTextbox.setReadOnly(True)
        self.timeLabel = QLabel(self.informationGroupbox)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setGeometry(QRect(590, 170, 71, 41))
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.timeLabel.setWordWrap(False)
        self.timeTextbox = QPlainTextEdit(self.informationGroupbox)
        self.timeTextbox.setObjectName(u"timeTextbox")
        self.timeTextbox.setGeometry(QRect(670, 170, 271, 41))
        self.timeTextbox.setFont(font)
        self.timeTextbox.setReadOnly(True)
        self.clientIpLabel = QLabel(self.informationGroupbox)
        self.clientIpLabel.setObjectName(u"clientIpLabel")
        self.clientIpLabel.setGeometry(QRect(590, 40, 101, 41))
        self.clientIpLabel.setFont(font)
        self.clientIpLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.clientIpLabel.setWordWrap(False)
        self.clientIpTextbox = QPlainTextEdit(self.informationGroupbox)
        self.clientIpTextbox.setObjectName(u"clientIpTextbox")
        self.clientIpTextbox.setGeometry(QRect(692, 40, 251, 41))
        self.clientIpTextbox.setFont(font)
        self.clientIpTextbox.setReadOnly(True)
        self.configTabelFrame = QFrame(self.Configurations)
        self.configTabelFrame.setObjectName(u"configTabelFrame")
        self.configTabelFrame.setGeometry(QRect(40, 140, 1531, 531))
        self.configTabelFrame.setFrameShape(QFrame.StyledPanel)
        self.configTabelFrame.setFrameShadow(QFrame.Plain)
        self.filterFrameConfigTab = QFrame(self.configTabelFrame)
        self.filterFrameConfigTab.setObjectName(u"filterFrameConfigTab")
        self.filterFrameConfigTab.setGeometry(QRect(20, 450, 993, 63))
        self.filterFrameConfigTab.setMaximumSize(QSize(16777215, 16777215))
        self.filterFrameConfigTab.setSizeIncrement(QSize(0, 0))
        self.filterFrameConfigTab.setFrameShape(QFrame.StyledPanel)
        self.filterFrameConfigTab.setFrameShadow(QFrame.Plain)
        self.valueLabel_2 = QLabel(self.filterFrameConfigTab)
        self.valueLabel_2.setObjectName(u"valueLabel_2")
        self.valueLabel_2.setGeometry(QRect(350, 9, 71, 41))
        self.valueLabel_2.setFont(font)
        self.valueLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.fieldLabel_2 = QLabel(self.filterFrameConfigTab)
        self.fieldLabel_2.setObjectName(u"fieldLabel_2")
        self.fieldLabel_2.setGeometry(QRect(10, 4, 61, 51))
        self.fieldLabel_2.setFont(font)
        self.fieldLabel_2.setMouseTracking(False)
        self.fieldLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.applyButton_2 = QPushButton(self.filterFrameConfigTab)
        self.applyButton_2.setObjectName(u"applyButton_2")
        self.applyButton_2.setGeometry(QRect(850, 14, 121, 38))
        self.applyButton_2.setFont(font)
        self.applyButton_2.setIcon(icon2)
        self.applyButton_2.setIconSize(QSize(25, 25))
        self.fieldComboBox_2 = QComboBox(self.filterFrameConfigTab)
        self.fieldComboBox_2.setObjectName(u"fieldComboBox_2")
        self.fieldComboBox_2.setGeometry(QRect(80, 14, 245, 36))
        self.fieldComboBox_2.setFont(font)
        self.textEdit_2 = QTextEdit(self.filterFrameConfigTab)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(430, 14, 401, 37))
        self.textEdit_2.setFont(font3)
        self.infectedClientsConfigViewTable = QTableWidget(self.configTabelFrame)
        if (self.infectedClientsConfigViewTable.columnCount() < 17):
            self.infectedClientsConfigViewTable.setColumnCount(17)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(3, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(4, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(5, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(6, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(7, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(8, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(9, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(10, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(11, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(12, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(13, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(14, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(15, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.infectedClientsConfigViewTable.setHorizontalHeaderItem(16, __qtablewidgetitem65)
        self.infectedClientsConfigViewTable.setObjectName(u"infectedClientsConfigViewTable")
        self.infectedClientsConfigViewTable.setGeometry(QRect(20, 10, 1501, 431))
        self.infectedClientsConfigViewTable.setFont(font)
        self.infectedClientsConfigViewTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.infectedClientsConfigViewTable.setAlternatingRowColors(True)
        self.infectedClientsConfigViewTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.infectedClientsConfigViewTable.setSortingEnabled(True)
        self.frame = QFrame(self.Configurations)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 910, 541, 51))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.updateConfigButton = QPushButton(self.frame)
        self.updateConfigButton.setObjectName(u"updateConfigButton")
        self.updateConfigButton.setGeometry(QRect(-1, -1, 51, 53))
        self.updateConfigButton.setMaximumSize(QSize(16777215, 16777215))
        self.updateConfigButton.setBaseSize(QSize(0, 1))
        icon9 = QIcon()
        icon9.addFile(u":/icon/images/save_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateConfigButton.setIcon(icon9)
        self.updateConfigButton.setIconSize(QSize(25, 25))
        self.undoConfigChangeButton = QPushButton(self.frame)
        self.undoConfigChangeButton.setObjectName(u"undoConfigChangeButton")
        self.undoConfigChangeButton.setGeometry(QRect(48, -1, 51, 53))
        icon10 = QIcon()
        icon10.addFile(u":/icon/images/undoButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.undoConfigChangeButton.setIcon(icon10)
        self.undoConfigChangeButton.setIconSize(QSize(25, 25))
        self.allControlConfigBannerBGFrame = QFrame(self.Configurations)
        self.allControlConfigBannerBGFrame.setObjectName(u"allControlConfigBannerBGFrame")
        self.allControlConfigBannerBGFrame.setGeometry(QRect(1020, 30, 551, 101))
        self.allControlConfigBannerBGFrame.setAutoFillBackground(True)
        self.allControlConfigBannerBGFrame.setFrameShape(QFrame.StyledPanel)
        self.allControlConfigBannerBGFrame.setFrameShadow(QFrame.Raised)
        self.allControlConfigBannerLabel = QLabel(self.allControlConfigBannerBGFrame)
        self.allControlConfigBannerLabel.setObjectName(u"allControlConfigBannerLabel")
        self.allControlConfigBannerLabel.setGeometry(QRect(-325, 20, 341, 71))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Black")
        font4.setPointSize(36)
        font4.setBold(True)
        font4.setWeight(75)
        self.allControlConfigBannerLabel.setFont(font4)
        self.tabs.addTab(self.Configurations, "")
        self.frame.raise_()
        self.enableDisableServerGroupBox.raise_()
        self.switchesGroupbox.raise_()
        self.informationGroupbox.raise_()
        self.configTabelFrame.raise_()
        self.allControlConfigBannerBGFrame.raise_()
        self.logoFooterLabel = QLabel(self.centralwidget)
        self.logoFooterLabel.setObjectName(u"logoFooterLabel")
        self.logoFooterLabel.setGeometry(QRect(830, 1030, 41, 41))
        self.logoFooterLabel.setPixmap(QPixmap(u":/icon/images/ALLCONTROL LOGO.png"))
#------ Paste ends when retranslateUi() is called in pydesigner code-----------------------------------------------------------------------------------------------------------

        self.setCentralWidget(self.centralwidget)

        self.createDatabaseFilterSection(font)
        self.createCommandParametersSection(font)

        self.keylogPreviewTBrowser.setVisible(False)
        commandParametersGrid = QGridLayout()
        commandParametersGrid.setObjectName(u"commandParametersGrid")
        commandParametersGrid.setContentsMargins(0, 0, 0, 0)

        #self.commandParametersWidget.setLayout(commandParametersGrid)

        # Preview pane should as well (eventually)

        self.retranslateUi()
       # self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def createDatabaseFilterSection(self, font):
        # Creates groupbox
        self.databaseFiltersGroupBox = QGroupBox(self.databasePreviewFrame)
        self.databaseFiltersGroupBox.setObjectName(u"databaseFiltersGroupBox")
        self.databaseFiltersGroupBox.setGeometry(QRect(20, 470, 641, 318))
        self.databaseFiltersGroupBox.setFont(font)
        self.databaseFiltersGroupBox.setTitle('Filters')

        # Creates main vertical layout
        self.databaseFiltersVerticalLayout = QVBoxLayout(self.databaseFiltersGroupBox)
        self.databaseFiltersVerticalLayout.setGeometry(QRect(10, 40, 621, 301))
        self.databaseFiltersVerticalLayout.setObjectName(u"databaseFiltersVerticalLayout")
        self.databaseFiltersVerticalLayout.setContentsMargins(10, 25, 10, 10)

        # Creates a scroll area
        self.databaseFilterWidgetsScrollArea = QScrollArea()
        self.databaseFilterWidgetsScrollArea.setObjectName(u"databaseFilterWidgetsScrollArea")
        self.databaseFilterWidgetsScrollArea.setWidgetResizable(True)
        self.databaseFilterWidgetsScrollArea.setFrameShape(QScrollArea.NoFrame)

        # Widget holding scroll content(filter widgets)
        self.databaseFilterWidgetsScrollContent = QWidget(self.databaseFilterWidgetsScrollArea)
        self.databaseFilterWidgetsScrollContent.setObjectName(u"databaseFilterWidgetsScrollContent")
        self.databaseFilterWidgetsScrollContent.setGeometry(QRect(0, 0, 617, 297))
        self.databaseFilterWidgetsScrollArea.setWidget(self.databaseFilterWidgetsScrollContent)
        self.databaseFilterWidgetsScrollContent.setContentsMargins(0, 10, 0, 10)

        # Create vertical layout for the scrollable content
        self.databaseFilterContentVLayout = QVBoxLayout(self.databaseFilterWidgetsScrollContent)
        self.databaseFilterContentVLayout.setGeometry(QRect(-1, -1, 621, 301))
        self.databaseFilterContentVLayout.setObjectName(u"databaseFilterContentVLayout")
        self.databaseFilterContentVLayout.setContentsMargins(0, 0, 0, 00)

        self.databaseFiltersVerticalLayout.addWidget(self.databaseFilterWidgetsScrollArea)

        # Create Apply button
        self.databaseViewFilterApplyButton = QPushButton(self.databasePreviewFrame)
        self.databaseViewFilterApplyButton.setText('Update')
        self.databaseViewFilterApplyButton.setGeometry(QRect(470, 794, 90, 40))

        self.databaseViewFilterApplyButton.setFont(font)

        self.databaseViewFilterApplyButton.setObjectName(u"databaseViewFilterApplyButton")
        self.databaseViewFilterApplyButton.setContentsMargins(0, 0, 0, 0)

        # Create Reset Button
        self.databaseViewFilterResetButton = QPushButton(self.databasePreviewFrame)
        self.databaseViewFilterResetButton.setGeometry(QRect(570, 794, 90, 40))
        self.databaseViewFilterResetButton.setText('Reset')
        self.databaseViewFilterResetButton.setFont(font)

        self.databaseViewFilterResetButton.setObjectName(u"databaseViewFilterResetButton")
        self.databaseViewFilterResetButton.setContentsMargins(0, 0, 0, 0)

    def createCommandParametersSection(self, font):
        # Creates groupbox
        self.commandParametersGroupBox = QGroupBox(self.Operations)
        self.commandParametersGroupBox.setObjectName(u"databaseFiltersGroupBox")
        self.commandParametersGroupBox.setGeometry(QRect(10, 685, 651, 244))
        self.commandParametersGroupBox.setFont(font)
        self.commandParametersGroupBox.setTitle('Filters')

        # Creates main vertical layout
        self.commandParametersVerticalLayout = QVBoxLayout(self.commandParametersGroupBox)
        self.commandParametersVerticalLayout.setGeometry(QRect(10, 40, 621, 301))
        self.commandParametersVerticalLayout.setObjectName(u"commandParametersVerticalLayout")
        self.commandParametersVerticalLayout.setContentsMargins(10, 25, 10, 10)

        # Creates a scroll area
        self.commandParametersWidgetsScrollArea = QScrollArea()
        self.commandParametersWidgetsScrollArea.setObjectName(u"commandParametersWidgetsScrollArea")
        self.commandParametersWidgetsScrollArea.setWidgetResizable(True)
        self.commandParametersWidgetsScrollArea.setFrameShape(QScrollArea.NoFrame)

        # Widget holding scroll content(filter widgets)
        self.commandParametersScrollContent = QWidget(self.commandParametersWidgetsScrollArea)
        self.commandParametersScrollContent.setObjectName(u"commandParametersScrollContent")
        self.commandParametersScrollContent.setGeometry(QRect(0, 0, 617, 297))
        self.commandParametersWidgetsScrollArea.setWidget(self.commandParametersScrollContent)
        self.commandParametersScrollContent.setContentsMargins(0, 10, 0, 10)

        # Create vertical layout for the scrollable content
        self.commandParametersContentVLayout = QVBoxLayout(self.commandParametersScrollContent)
        self.commandParametersContentVLayout.setGeometry(QRect(-1, -1, 621, 301))
        self.commandParametersContentVLayout.setObjectName(u"commandParametersContentVLayout")
        self.commandParametersContentVLayout.setContentsMargins(0, 0, 0, 00)

        self.commandParametersVerticalLayout.addWidget(self.commandParametersWidgetsScrollArea)

    def updateLabel(self, param_name, label, value):
        label.setText(str(value))

        value = str(value)
        match = re.search(r'\d+', value)

        # Check if a match was found
        if match:
            # Extract and convert the matched digits to an integer
            number = int(match.group())
            print("Extracted Number:", number)
        else:
            print("No digits found in the string.")

        print(f'{param_name} = {number}')
        self.commandParameterValuesDict[label.text()] = number



    def applyFilter(self):
        self.button = QPushButton(self.filterFrame)
        self.button.setGeometry(0, 0, 121, 38)
        self.button.setText('test')
        print(self.button)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("ALLCONTROL_SERVER", u"MainWindow", None))
        self.keyloggerServerConnectedLabel.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Keylogger Server Connections", None))
        ___qtablewidgetitem = self.connectedClientsKeyloggerServer.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_id", None));
        ___qtablewidgetitem1 = self.connectedClientsKeyloggerServer.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_address", None));
        ___qtablewidgetitem2 = self.connectedClientsKeyloggerServer.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"sID", None));
        # if QT_CONFIG(tooltip)
        self.connectedClientsKeyloggerServer.setToolTip(QCoreApplication.translate("ALLCONTROL_SERVER",
                                                                                   u"Clients currently connected to our keylogging server.",
                                                                                   None))
        # endif // QT_CONFIG(tooltip)
        self.infectedClientsLabel.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Infected Clients", None))
        ___qtablewidgetitem3 = self.infectedClients.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_id", None));
        ___qtablewidgetitem4 = self.infectedClients.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"sID", None));
        ___qtablewidgetitem5 = self.infectedClients.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"mac_address", None));
        ___qtablewidgetitem6 = self.infectedClients.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_ip", None));
        ___qtablewidgetitem7 = self.infectedClients.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"infected_date", None));
        ___qtablewidgetitem8 = self.infectedClients.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"windows_username", None));
        ___qtablewidgetitem9 = self.infectedClients.horizontalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"os_info", None));
        ___qtablewidgetitem10 = self.infectedClients.horizontalHeaderItem(7)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"system_manufacturer", None));
        ___qtablewidgetitem11 = self.infectedClients.horizontalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"ssid", None));
        ___qtablewidgetitem12 = self.infectedClients.horizontalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"net_user_name", None));
        ___qtablewidgetitem13 = self.infectedClients.horizontalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"name_net_card", None));
        ___qtablewidgetitem14 = self.infectedClients.horizontalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"auth_method", None));
        ___qtablewidgetitem15 = self.infectedClients.horizontalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"cipher_method", None));
        ___qtablewidgetitem16 = self.infectedClients.horizontalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"radio_type", None));
        ___qtablewidgetitem17 = self.infectedClients.horizontalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"cpu_arch", None));
        ___qtablewidgetitem18 = self.infectedClients.horizontalHeaderItem(15)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"cpu_name", None));
        ___qtablewidgetitem19 = self.infectedClients.horizontalHeaderItem(16)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"timezone", None));
        # if QT_CONFIG(tooltip)
        self.infectedClients.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"All our infected clients.", None))
        # endif // QT_CONFIG(tooltip)
        self.commandServerConnectedLabel.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Command Server Connections", None))
        ___qtablewidgetitem20 = self.connectedClientsCommandServer.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_id", None));
        ___qtablewidgetitem21 = self.connectedClientsCommandServer.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_address", None));
        ___qtablewidgetitem22 = self.connectedClientsCommandServer.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"name", None));
        # if QT_CONFIG(tooltip)
        self.connectedClientsCommandServer.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Clients currently connected to the command server.",
                                       None))
        # endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Info", None))
        ___qtablewidgetitem23 = self.infoTable.verticalHeaderItem(0)
        ___qtablewidgetitem23.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Command Server Status", None));
        ___qtablewidgetitem24 = self.infoTable.verticalHeaderItem(1)
        ___qtablewidgetitem24.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Keylogger Server Status", None));
        ___qtablewidgetitem25 = self.infoTable.verticalHeaderItem(2)
        ___qtablewidgetitem25.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Command Server IP & Port", None));
        ___qtablewidgetitem26 = self.infoTable.verticalHeaderItem(3)
        ___qtablewidgetitem26.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Keylogger Server IP & Port", None));
        # if QT_CONFIG(tooltip)
        self.infoTable.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Server status and location.", None))
        # endif // QT_CONFIG(tooltip)
        self.securityLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Security Info", None))
        ___qtablewidgetitem27 = self.securityTable.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Date", None));
        ___qtablewidgetitem28 = self.securityTable.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Message", None));
        # if QT_CONFIG(tooltip)
        self.securityTable.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"System infromation logs.", None))
        # endif // QT_CONFIG(tooltip)
        self.logsLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Logs", None))
        ___qtablewidgetitem29 = self.logsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"date", None));
        ___qtablewidgetitem30 = self.logsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Source", None));
        ___qtablewidgetitem31 = self.logsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"message", None));
        # if QT_CONFIG(tooltip)
        self.logsTable.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Log information on System and clients.", None))
        # endif // QT_CONFIG(tooltip)
        self.bannerLabel.setText("")
        # if QT_CONFIG(tooltip)
        self.airplaneModeButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Closes all connections on the server side.", None))
        # endif // QT_CONFIG(tooltip)
        self.airplaneModeButton.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Airplane Mode", None))
        self.tabs.setTabText(self.tabs.indexOf(self.Dashboard),
                             QCoreApplication.translate("ALLCONTROL_SERVER", u"Dashboard", None))
        self.connectedClientsLabel.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Connected Clients", None))
        ___qtablewidgetitem32 = self.connectedClients.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_id", None));
        ___qtablewidgetitem33 = self.connectedClients.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"sID", None));
        ___qtablewidgetitem34 = self.connectedClients.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"mac_address", None));
        ___qtablewidgetitem35 = self.connectedClients.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_ip", None));
        ___qtablewidgetitem36 = self.connectedClients.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"infected_date", None));
        ___qtablewidgetitem37 = self.connectedClients.horizontalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"windows_username", None));
        ___qtablewidgetitem38 = self.connectedClients.horizontalHeaderItem(6)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"os_info", None));
        ___qtablewidgetitem39 = self.connectedClients.horizontalHeaderItem(7)
        ___qtablewidgetitem39.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"system_manufacturer", None));
        ___qtablewidgetitem40 = self.connectedClients.horizontalHeaderItem(8)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"ssid", None));
        ___qtablewidgetitem41 = self.connectedClients.horizontalHeaderItem(9)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"net_user_name", None));
        ___qtablewidgetitem42 = self.connectedClients.horizontalHeaderItem(10)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"name_net_card", None));
        ___qtablewidgetitem43 = self.connectedClients.horizontalHeaderItem(11)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"auth_method", None));
        ___qtablewidgetitem44 = self.connectedClients.horizontalHeaderItem(12)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"cipher_method", None));
        ___qtablewidgetitem45 = self.connectedClients.horizontalHeaderItem(13)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"radio_type", None));
        ___qtablewidgetitem46 = self.connectedClients.horizontalHeaderItem(14)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"cpu_arch", None));
        ___qtablewidgetitem47 = self.connectedClients.horizontalHeaderItem(15)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"cpu_name", None));
        ___qtablewidgetitem48 = self.connectedClients.horizontalHeaderItem(16)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"timezone", None));
        # if QT_CONFIG(tooltip)
        self.connectedClients.setToolTip(QCoreApplication.translate("ALLCONTROL_SERVER", u"Online clients.", None))
        # endif // QT_CONFIG(tooltip)
        self.valueLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Value:", None))
        self.fieldLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Field:", None))
        self.applyButton.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Apply", None))
        self.textEdit.setPlaceholderText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Enter value to find connected clients", None))
        self.scheduledCommandsLabel.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Scheduled Commands", None))
        # if QT_CONFIG(tooltip)
        self.scheduledCommands.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Schedule delayed commands.", None))
        # endif // QT_CONFIG(tooltip)
        self.optionsGroupBox.setTitle(QCoreApplication.translate("ALLCONTROL_SERVER", u"Options", None))
        # if QT_CONFIG(tooltip)
        self.sendToAllCheckBox.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Send to all the currenlty connected clients.", None))
        # endif // QT_CONFIG(tooltip)
        self.sendToAllCheckBox.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Send to all", None))
        # if QT_CONFIG(tooltip)
        self.targetClientIDComboBox.setToolTip(QCoreApplication.translate("ALLCONTROL_SERVER",
                                                                          u"The target to send the command to. Select the client id that correlates.",
                                                                          None))
        # endif // QT_CONFIG(tooltip)
        self.targetLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Target (Client ID):", None))
        self.commandGroupBox.setTitle(QCoreApplication.translate("ALLCONTROL_SERVER", u"Command", None))
        self.commandNameLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Name:", None))
        self.commandDescriptionLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Description:", None))
        # if QT_CONFIG(tooltip)
        self.commandNameComboBox.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Select a command.", None))
        # endif // QT_CONFIG(tooltip)
        self.noiseLevelLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Noise Level:", None))
        # if QT_CONFIG(tooltip)
        self.sendCommandButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Send the selected command to the selected client.",
                                       None))
        # endif // QT_CONFIG(tooltip)
        self.sendCommandButton.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Send", None))
        # if QT_CONFIG(tooltip)
        self.commandMediaImageLabel.setToolTip(QCoreApplication.translate("ALLCONTROL_SERVER",
                                                                          u"Will display any media captured from a successful commnad.",
                                                                          None))
        # endif // QT_CONFIG(tooltip)
        self.commandMediaImageLabel.setText("")
        self.commandPreviewControlsGroupbox.setTitle("")
        # if QT_CONFIG(tooltip)
        self.nextMediaImageButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Next command media frame.", None))
        # endif // QT_CONFIG(tooltip)
        self.nextMediaImageButton.setText("")
        # if QT_CONFIG(tooltip)
        self.previousMediaImageButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Previous command media frame.", None))
        # endif // QT_CONFIG(tooltip)
        self.previousMediaImageButton.setText("")
        # if QT_CONFIG(tooltip)
        self.fullscreenImageButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Fullscreen command meda content.", None))
        # endif // QT_CONFIG(tooltip)
        self.fullscreenImageButton.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.Operations),
                             QCoreApplication.translate("ALLCONTROL_SERVER", u"Operations", None))
        # if QT_CONFIG(tooltip)
        self.databaseViewTable.setToolTip(QCoreApplication.translate("ALLCONTROL_SERVER",
                                                                     u"Displays database info. Try clickign the cells if its media for display.",
                                                                     None))
        # endif // QT_CONFIG(tooltip)
        self.tableDatabaseLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Table:", None))
        # if QT_CONFIG(tooltip)
        self.refreshTableViewButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Refresh the selected table.", None))
        # endif // QT_CONFIG(tooltip)
        self.refreshTableViewButton.setText("")
        self.imagePreviewLabel.setText("")
        # if QT_CONFIG(tooltip)
        self.keylogPreviewTBrowser.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Media selected from table will display here.", None))
        # endif // QT_CONFIG(tooltip)
        self.keylogPreviewTBrowser.setHtml(QCoreApplication.translate("ALLCONTROL_SERVER",
                                                                      u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                      "p, li { white-space: pre-wrap; }\n"
                                                                      "</style></head><body style=\" font-family:'Segoe UI Black','Segoe UI Black'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
                                                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                                      None))
        # if QT_CONFIG(tooltip)
        self.previousDatabaseImageButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Previous content frame", None))
        # endif // QT_CONFIG(tooltip)
        self.previousDatabaseImageButton.setText("")
        # if QT_CONFIG(tooltip)
        self.nextDatabaseImageButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Next content frame.", None))
        # endif // QT_CONFIG(tooltip)
        self.nextDatabaseImageButton.setText("")
        # if QT_CONFIG(tooltip)
        self.fullscreenDatabaseButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Fullscreen the selecetd content.", None))
        # endif // QT_CONFIG(tooltip)
        self.fullscreenDatabaseButton.setText("")
        self.databaseImageDataCapturedLabel.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Date Captured:", None))
        # if QT_CONFIG(tooltip)
        self.databaseImageCaptureDateEdit.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"The date this media was captured.", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.deleteDatabaseRowButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Delete the selected row.", None))
        # endif // QT_CONFIG(tooltip)
        self.deleteDatabaseRowButton.setText("")
        self.rowCountBrowser.setHtml(QCoreApplication.translate("ALLCONTROL_SERVER",
                                                                u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                "p, li { white-space: pre-wrap; }\n"
                                                                "</style></head><body style=\" font-family:'Segoe UI Black','Segoe UI Black'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
                                                                "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                                None))
        self.rowCountLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Row count", None))
        self.tabs.setTabText(self.tabs.indexOf(self.database),
                             QCoreApplication.translate("ALLCONTROL_SERVER", u"Database", None))
        # if QT_CONFIG(tooltip)
        self.enableDisableServerGroupBox.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Start or shutdown the servers.", None))
        # endif // QT_CONFIG(tooltip)
        self.enableDisableServerGroupBox.setTitle(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Enable or Disable Servers", None))
        self.commandServerCheckBox.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Command Server", None))
        self.keyloggerServerCheckBox.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Keylogger Server", None))
        # if QT_CONFIG(tooltip)
        self.switchesGroupbox.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Set client side settings.", None))
        # endif // QT_CONFIG(tooltip)
        self.switchesGroupbox.setTitle(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Enable or Disable Client Options", None))
        self.clientKeyloggerEnabledCheckbox.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Keylogger Enabled", None))
        self.dataServerEnabledCheckbox.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Data Server Enabled", None))
        # if QT_CONFIG(tooltip)
        self.favoriteCheckbox.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Will highlight client on table for easy visibility.",
                                       None))
        # endif // QT_CONFIG(tooltip)
        self.favoriteCheckbox.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Favorite", None))
        # if QT_CONFIG(tooltip)
        self.informationGroupbox.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Quick information on the selected client.", None))
        # endif // QT_CONFIG(tooltip)
        self.informationGroupbox.setTitle(QCoreApplication.translate("ALLCONTROL_SERVER", u"Information", None))
        self.clientIdTextbox.setPlainText("")
        # if QT_CONFIG(accessibility)
        self.cleintIdLabel.setAccessibleDescription(QCoreApplication.translate("ALLCONTROL_SERVER", u"0", None))
        # endif // QT_CONFIG(accessibility)
        self.cleintIdLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Client ID: ", None))
        # if QT_CONFIG(accessibility)
        self.sIdLabel.setAccessibleDescription(QCoreApplication.translate("ALLCONTROL_SERVER", u"0", None))
        # endif // QT_CONFIG(accessibility)
        self.sIdLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"sID: ", None))
        # if QT_CONFIG(accessibility)
        self.networkUsernameLabel.setAccessibleDescription(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"0", None))
        # endif // QT_CONFIG(accessibility)
        self.networkUsernameLabel.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Network Username:", None))
        # if QT_CONFIG(accessibility)
        self.windowsUsernameLabel.setAccessibleDescription(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"0", None))
        # endif // QT_CONFIG(accessibility)
        self.windowsUsernameLabel.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Windows Username: ", None))
        # if QT_CONFIG(accessibility)
        self.macaddressLabel.setAccessibleDescription(QCoreApplication.translate("ALLCONTROL_SERVER", u"0", None))
        # endif // QT_CONFIG(accessibility)
        self.macaddressLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Mac Address: ", None))
        # if QT_CONFIG(accessibility)
        self.timeLabel.setAccessibleDescription(QCoreApplication.translate("ALLCONTROL_SERVER", u"0", None))
        # endif // QT_CONFIG(accessibility)
        self.timeLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Time: ", None))
        # if QT_CONFIG(accessibility)
        self.clientIpLabel.setAccessibleDescription(QCoreApplication.translate("ALLCONTROL_SERVER", u"0", None))
        # endif // QT_CONFIG(accessibility)
        self.clientIpLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Client IP:", None))
        self.valueLabel_2.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Value:", None))
        self.fieldLabel_2.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Field:", None))
        self.applyButton_2.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Apply", None))
        self.textEdit_2.setPlaceholderText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Enter value to find clients", None))
        ___qtablewidgetitem49 = self.infectedClientsConfigViewTable.horizontalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_id", None));
        ___qtablewidgetitem50 = self.infectedClientsConfigViewTable.horizontalHeaderItem(1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"sID", None));
        ___qtablewidgetitem51 = self.infectedClientsConfigViewTable.horizontalHeaderItem(2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"mac_address", None));
        ___qtablewidgetitem52 = self.infectedClientsConfigViewTable.horizontalHeaderItem(3)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_ip", None));
        ___qtablewidgetitem53 = self.infectedClientsConfigViewTable.horizontalHeaderItem(4)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"infected_date", None));
        ___qtablewidgetitem54 = self.infectedClientsConfigViewTable.horizontalHeaderItem(5)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"windows_username", None));
        ___qtablewidgetitem55 = self.infectedClientsConfigViewTable.horizontalHeaderItem(6)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"os_info", None));
        ___qtablewidgetitem56 = self.infectedClientsConfigViewTable.horizontalHeaderItem(7)
        ___qtablewidgetitem56.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"system_manufacturer", None));
        ___qtablewidgetitem57 = self.infectedClientsConfigViewTable.horizontalHeaderItem(8)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"ssid", None));
        ___qtablewidgetitem58 = self.infectedClientsConfigViewTable.horizontalHeaderItem(9)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"net_user_name", None));
        ___qtablewidgetitem59 = self.infectedClientsConfigViewTable.horizontalHeaderItem(10)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"name_net_card", None));
        ___qtablewidgetitem60 = self.infectedClientsConfigViewTable.horizontalHeaderItem(11)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"auth_method", None));
        ___qtablewidgetitem61 = self.infectedClientsConfigViewTable.horizontalHeaderItem(12)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"cipher_mode", None));
        ___qtablewidgetitem62 = self.infectedClientsConfigViewTable.horizontalHeaderItem(13)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"radio_type", None));
        ___qtablewidgetitem63 = self.infectedClientsConfigViewTable.horizontalHeaderItem(14)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"cpu_arch", None));
        ___qtablewidgetitem64 = self.infectedClientsConfigViewTable.horizontalHeaderItem(15)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"cpu_name", None));
        ___qtablewidgetitem65 = self.infectedClientsConfigViewTable.horizontalHeaderItem(16)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"timezone", None));
        # if QT_CONFIG(tooltip)
        self.infectedClientsConfigViewTable.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"All client configs.", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.updateConfigButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Save the client settings.", None))
        # endif // QT_CONFIG(tooltip)
        self.updateConfigButton.setText("")
        # if QT_CONFIG(tooltip)
        self.undoConfigChangeButton.setToolTip(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"Undo client setting changes.", None))
        # endif // QT_CONFIG(tooltip)
        self.undoConfigChangeButton.setText("")
        self.allControlConfigBannerLabel.setText(
            QCoreApplication.translate("ALLCONTROL_SERVER", u"ALLCONTROL", None))
        self.tabs.setTabText(self.tabs.indexOf(self.Configurations),
                             QCoreApplication.translate("ALLCONTROL_SERVER", u"Configurations", None))
        self.logoFooterLabel.setText("")
    # retranslateUi


class fullScreenImageWindow:
    new_window = None
    fullscreenImageLabel = None
    window_width = None
    window_height = None

    def __init__(self):
        # Get users screen size, and make it the 16:9 ratio below it
        screen_info = QDesktopWidget().screenGeometry()

        # Retrieve the width and height
        self.window_width = screen_info.width() - 160
        self.window_height = screen_info.height() - 160

        X_POS = (screen_info.width() - self.window_width) / 2
        Y_POS = (screen_info.height() - self.window_height) / 2

        self.new_window = QDialog()
        self.new_window.setWindowTitle("New Window")
        self.new_window.setGeometry(X_POS, Y_POS, self.window_width, self.window_height)

        self.fullscreenImageLabel = QLabel(self.new_window)
        self.fullscreenImageLabel.setGeometry(0, 0, self.window_width, self.window_height)

    def show(self):
        self.new_window.show()










