# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import mabilogin_gui.ui.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 500)
        palette = QPalette()
        brush = QBrush(QColor(168, 151, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush)
        MainWindow.setPalette(palette)
        self.topWidget = QWidget(MainWindow)
        self.topWidget.setObjectName(u"topWidget")
        self.topWidget.setStyleSheet(u"/* MENUS */\n"
"\n"
"#topWidget {\n"
"	background-color: #F7F6F4;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"#titleBarWgt {\n"
"	background-color: #6B8A47;\n"
"}\n"
"\n"
"#ctxWgt {\n"
"	background-color: #F7F6F4;\n"
"}\n"
"\n"
"#leftMenuWgt {\n"
"	background-color: #A7C584;\n"
"}\n"
"\n"
"QPushButton#closeAppBtn:pressed {\n"
"	background-color: #ed4245;\n"
"}\n"
"QPushButton#closeAppBtn:hover {\n"
"	background-color: #ed4245;\n"
"}\n"
"QPushButton {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(0,0,0,50);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,50);\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.topWidget)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.titleBarWgt = QWidget(self.topWidget)
        self.titleBarWgt.setObjectName(u"titleBarWgt")
        self.titleBarWgt.setMinimumSize(QSize(0, 25))
        self.titleBarWgt.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.titleBarWgt)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.appIconWgt = QWidget(self.titleBarWgt)
        self.appIconWgt.setObjectName(u"appIconWgt")
        self.appIconWgt.setMinimumSize(QSize(25, 25))
        self.appIconWgt.setMaximumSize(QSize(25, 25))
        self.appIconWgt.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.appIconWgt)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.iconFrm = QFrame(self.appIconWgt)
        self.iconFrm.setObjectName(u"iconFrm")
        self.iconFrm.setMinimumSize(QSize(20, 20))
        self.iconFrm.setMaximumSize(QSize(20, 20))
        self.iconFrm.setStyleSheet(u"background-image: url(:/images/images/mushroom_20x20.png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.iconFrm.setFrameShape(QFrame.StyledPanel)
        self.iconFrm.setFrameShadow(QFrame.Raised)
        self.iconFrm.setLineWidth(0)

        self.horizontalLayout_6.addWidget(self.iconFrm)


        self.horizontalLayout_3.addWidget(self.appIconWgt)

        self.titleWidget = QWidget(self.titleBarWgt)
        self.titleWidget.setObjectName(u"titleWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleWidget.sizePolicy().hasHeightForWidth())
        self.titleWidget.setSizePolicy(sizePolicy)
        self.titleWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.titleWidget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.titleWidget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.horizontalLayout_5.addWidget(self.titleLabel)


        self.horizontalLayout_3.addWidget(self.titleWidget)

        self.controlBarWgt = QWidget(self.titleBarWgt)
        self.controlBarWgt.setObjectName(u"controlBarWgt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.controlBarWgt.sizePolicy().hasHeightForWidth())
        self.controlBarWgt.setSizePolicy(sizePolicy1)
        self.controlBarWgt.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.controlBarWgt)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.controlBarWgt)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.settingsTopBtn.sizePolicy().hasHeightForWidth())
        self.settingsTopBtn.setSizePolicy(sizePolicy2)
        self.settingsTopBtn.setMinimumSize(QSize(25, 25))
        self.settingsTopBtn.setMaximumSize(QSize(25, 25))
        self.settingsTopBtn.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))
        self.settingsTopBtn.setAutoDefault(False)
        self.settingsTopBtn.setFlat(False)

        self.horizontalLayout_4.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.controlBarWgt)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.minimizeAppBtn.sizePolicy().hasHeightForWidth())
        self.minimizeAppBtn.setSizePolicy(sizePolicy2)
        self.minimizeAppBtn.setMinimumSize(QSize(25, 25))
        self.minimizeAppBtn.setMaximumSize(QSize(25, 25))
        self.minimizeAppBtn.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.controlBarWgt)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.maximizeRestoreAppBtn.sizePolicy().hasHeightForWidth())
        self.maximizeRestoreAppBtn.setSizePolicy(sizePolicy2)
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(25, 25))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(25, 25))
        self.maximizeRestoreAppBtn.setToolTipDuration(-1)
        self.maximizeRestoreAppBtn.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.controlBarWgt)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.closeAppBtn.sizePolicy().hasHeightForWidth())
        self.closeAppBtn.setSizePolicy(sizePolicy2)
        self.closeAppBtn.setMinimumSize(QSize(25, 25))
        self.closeAppBtn.setMaximumSize(QSize(25, 25))
        self.closeAppBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.closeAppBtn.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.closeAppBtn)


        self.horizontalLayout_3.addWidget(self.controlBarWgt)


        self.appMargins.addWidget(self.titleBarWgt)

        self.appWgt = QWidget(self.topWidget)
        self.appWgt.setObjectName(u"appWgt")
        self.horizontalLayout_2 = QHBoxLayout(self.appWgt)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftMenuWgt = QWidget(self.appWgt)
        self.leftMenuWgt.setObjectName(u"leftMenuWgt")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftMenuWgt.sizePolicy().hasHeightForWidth())
        self.leftMenuWgt.setSizePolicy(sizePolicy3)
        self.leftMenuWgt.setMinimumSize(QSize(35, 0))
        self.leftMenuWgt.setMaximumSize(QSize(35, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuWgt)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lmToggleWgt = QWidget(self.leftMenuWgt)
        self.lmToggleWgt.setObjectName(u"lmToggleWgt")
        self.lmToggleWgt.setMaximumSize(QSize(16777215, 35))
        self.verticalLayout_3 = QVBoxLayout(self.lmToggleWgt)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lmToggleBtn = QPushButton(self.lmToggleWgt)
        self.lmToggleBtn.setObjectName(u"lmToggleBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lmToggleBtn.sizePolicy().hasHeightForWidth())
        self.lmToggleBtn.setSizePolicy(sizePolicy4)
        self.lmToggleBtn.setMaximumSize(QSize(16777215, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/images/icons/icon_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lmToggleBtn.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.lmToggleBtn)


        self.verticalLayout_2.addWidget(self.lmToggleWgt)

        self.mainAccGrpwidget = QWidget(self.leftMenuWgt)
        self.mainAccGrpwidget.setObjectName(u"mainAccGrpwidget")
        sizePolicy4.setHeightForWidth(self.mainAccGrpwidget.sizePolicy().hasHeightForWidth())
        self.mainAccGrpwidget.setSizePolicy(sizePolicy4)
        self.mainAccGrpwidget.setMinimumSize(QSize(0, 0))
        self.mainAccGrpwidget.setMaximumSize(QSize(16777215, 35))
        self.verticalLayout_6 = QVBoxLayout(self.mainAccGrpwidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mainAccGrpBtn = QPushButton(self.mainAccGrpwidget)
        self.mainAccGrpBtn.setObjectName(u"mainAccGrpBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(35)
        sizePolicy5.setVerticalStretch(35)
        sizePolicy5.setHeightForWidth(self.mainAccGrpBtn.sizePolicy().hasHeightForWidth())
        self.mainAccGrpBtn.setSizePolicy(sizePolicy5)
        self.mainAccGrpBtn.setMinimumSize(QSize(0, 35))
        self.mainAccGrpBtn.setMaximumSize(QSize(16777215, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/mainuser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainAccGrpBtn.setIcon(icon5)
        self.mainAccGrpBtn.setIconSize(QSize(23, 23))

        self.verticalLayout_6.addWidget(self.mainAccGrpBtn)


        self.verticalLayout_2.addWidget(self.mainAccGrpwidget)

        self.lmAccAddWgt = QWidget(self.leftMenuWgt)
        self.lmAccAddWgt.setObjectName(u"lmAccAddWgt")
        self.lmAccAddWgt.setMinimumSize(QSize(0, 0))
        self.lmAccAddWgt.setMaximumSize(QSize(16777215, 35))
        self.verticalLayout_4 = QVBoxLayout(self.lmAccAddWgt)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lmAccAddBtn = QPushButton(self.lmAccAddWgt)
        self.lmAccAddBtn.setObjectName(u"lmAccAddBtn")
        sizePolicy4.setHeightForWidth(self.lmAccAddBtn.sizePolicy().hasHeightForWidth())
        self.lmAccAddBtn.setSizePolicy(sizePolicy4)
        icon6 = QIcon()
        icon6.addFile(u":/images/icons/cil-library-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lmAccAddBtn.setIcon(icon6)
        self.lmAccAddBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_4.addWidget(self.lmAccAddBtn)


        self.verticalLayout_2.addWidget(self.lmAccAddWgt)

        self.lmSettingFrm = QFrame(self.leftMenuWgt)
        self.lmSettingFrm.setObjectName(u"lmSettingFrm")
        self.lmSettingFrm.setFrameShape(QFrame.StyledPanel)
        self.lmSettingFrm.setFrameShadow(QFrame.Raised)
        self.lmSettingFrm.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.lmSettingFrm)


        self.horizontalLayout_2.addWidget(self.leftMenuWgt)

        self.ctxWgt = QWidget(self.appWgt)
        self.ctxWgt.setObjectName(u"ctxWgt")

        self.horizontalLayout_2.addWidget(self.ctxWgt, 0, Qt.AlignTop)

        self.leftBarExtraFrm = QWidget(self.appWgt)
        self.leftBarExtraFrm.setObjectName(u"leftBarExtraFrm")
        self.leftBarExtraFrm.setMaximumSize(QSize(0, 16777215))
        self.horizontalLayout = QHBoxLayout(self.leftBarExtraFrm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.leftBarExtraFrm)

        self.leftBarExtraFrm.raise_()
        self.ctxWgt.raise_()
        self.leftMenuWgt.raise_()

        self.appMargins.addWidget(self.appWgt)

        MainWindow.setCentralWidget(self.topWidget)

        self.retranslateUi(MainWindow)

        self.settingsTopBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"MabiLogin", None))
        self.settingsTopBtn.setText("")
        self.minimizeAppBtn.setText("")
        self.maximizeRestoreAppBtn.setText("")
        self.closeAppBtn.setText("")
#if QT_CONFIG(shortcut)
        self.closeAppBtn.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.lmToggleBtn.setText("")
        self.mainAccGrpBtn.setText("")
        self.lmAccAddBtn.setText("")
    # retranslateUi

