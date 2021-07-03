# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acc_wgt.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_accWgt(object):
    def setupUi(self, accWgt):
        if not accWgt.objectName():
            accWgt.setObjectName(u"accWgt")
        accWgt.resize(365, 140)
        accWgt.setMaximumSize(QSize(16777215, 140))
        self.verticalLayout = QVBoxLayout(accWgt)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.infoWgt = QWidget(accWgt)
        self.infoWgt.setObjectName(u"infoWgt")
        self.infoWgt.setMinimumSize(QSize(0, 30))
        self.infoWgt.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.infoWgt)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.accNumWgt = QWidget(self.infoWgt)
        self.accNumWgt.setObjectName(u"accNumWgt")
        self.accNumWgt.setMaximumSize(QSize(40, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.accNumWgt)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.accNumLbl = QLabel(self.accNumWgt)
        self.accNumLbl.setObjectName(u"accNumLbl")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.accNumLbl.setFont(font)
        self.accNumLbl.setLineWidth(0)
        self.accNumLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.accNumLbl)


        self.horizontalLayout_2.addWidget(self.accNumWgt)

        self.accNameWgt = QWidget(self.infoWgt)
        self.accNameWgt.setObjectName(u"accNameWgt")
        self.horizontalLayout_9 = QHBoxLayout(self.accNameWgt)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.accNameLbl = QLabel(self.accNameWgt)
        self.accNameLbl.setObjectName(u"accNameLbl")

        self.horizontalLayout_9.addWidget(self.accNameLbl)


        self.horizontalLayout_2.addWidget(self.accNameWgt)

        self.accLogWgt = QWidget(self.infoWgt)
        self.accLogWgt.setObjectName(u"accLogWgt")
        self.verticalLayout_3 = QVBoxLayout(self.accLogWgt)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.accLogWgt)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.accLogWgt)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.accLogWgt)

        self.accCtlWgt = QWidget(self.infoWgt)
        self.accCtlWgt.setObjectName(u"accCtlWgt")
        self.verticalLayout_7 = QVBoxLayout(self.accCtlWgt)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.openCloseBtn = QPushButton(self.accCtlWgt)
        self.openCloseBtn.setObjectName(u"openCloseBtn")

        self.verticalLayout_7.addWidget(self.openCloseBtn)

        self.resetWindowBtn = QPushButton(self.accCtlWgt)
        self.resetWindowBtn.setObjectName(u"resetWindowBtn")

        self.verticalLayout_7.addWidget(self.resetWindowBtn)


        self.horizontalLayout_2.addWidget(self.accCtlWgt)


        self.verticalLayout.addWidget(self.infoWgt)

        self.detailWgt = QWidget(accWgt)
        self.detailWgt.setObjectName(u"detailWgt")
        self.horizontalLayout_6 = QHBoxLayout(self.detailWgt)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget = QWidget(self.detailWgt)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.usernameLbl = QLabel(self.widget)
        self.usernameLbl.setObjectName(u"usernameLbl")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.usernameLbl)

        self.usernameLineEdit = QLineEdit(self.widget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.usernameLineEdit)

        self.passwordLbl = QLabel(self.widget)
        self.passwordLbl.setObjectName(u"passwordLbl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.passwordLbl)

        self.passwordLineEdit = QLineEdit(self.widget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.passwordLineEdit)

        self.lastLoginLbl = QLabel(self.widget)
        self.lastLoginLbl.setObjectName(u"lastLoginLbl")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lastLoginLbl)

        self.lastLoginLineEdit = QLineEdit(self.widget)
        self.lastLoginLineEdit.setObjectName(u"lastLoginLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lastLoginLineEdit)


        self.horizontalLayout_6.addWidget(self.widget)

        self.widget_5 = QWidget(self.detailWgt)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rightLblWgt = QWidget(self.widget_8)
        self.rightLblWgt.setObjectName(u"rightLblWgt")
        self.verticalLayout_5 = QVBoxLayout(self.rightLblWgt)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.rightLblWgt)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_8 = QLabel(self.rightLblWgt)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.rightLblWgt)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)


        self.horizontalLayout_3.addWidget(self.rightLblWgt)

        self.windowsWgt = QWidget(self.widget_8)
        self.windowsWgt.setObjectName(u"windowsWgt")
        self.verticalLayout_6 = QVBoxLayout(self.windowsWgt)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.windowCfgCbox = QComboBox(self.windowsWgt)
        self.windowCfgCbox.addItem("")
        self.windowCfgCbox.addItem("")
        self.windowCfgCbox.addItem("")
        self.windowCfgCbox.addItem("")
        self.windowCfgCbox.setObjectName(u"windowCfgCbox")

        self.verticalLayout_6.addWidget(self.windowCfgCbox)

        self.sizeWgt = QWidget(self.windowsWgt)
        self.sizeWgt.setObjectName(u"sizeWgt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sizeWgt.sizePolicy().hasHeightForWidth())
        self.sizeWgt.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.sizeWgt)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.sizeXLbl = QLabel(self.sizeWgt)
        self.sizeXLbl.setObjectName(u"sizeXLbl")

        self.horizontalLayout_5.addWidget(self.sizeXLbl)

        self.sizeXLineEdit = QLineEdit(self.sizeWgt)
        self.sizeXLineEdit.setObjectName(u"sizeXLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sizeXLineEdit.sizePolicy().hasHeightForWidth())
        self.sizeXLineEdit.setSizePolicy(sizePolicy2)
        self.sizeXLineEdit.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.sizeXLineEdit)

        self.sizeYLbl = QLabel(self.sizeWgt)
        self.sizeYLbl.setObjectName(u"sizeYLbl")

        self.horizontalLayout_5.addWidget(self.sizeYLbl)

        self.sizeYLineEdit = QLineEdit(self.sizeWgt)
        self.sizeYLineEdit.setObjectName(u"sizeYLineEdit")
        sizePolicy2.setHeightForWidth(self.sizeYLineEdit.sizePolicy().hasHeightForWidth())
        self.sizeYLineEdit.setSizePolicy(sizePolicy2)
        self.sizeYLineEdit.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.sizeYLineEdit)


        self.verticalLayout_6.addWidget(self.sizeWgt)

        self.positionWgt = QWidget(self.windowsWgt)
        self.positionWgt.setObjectName(u"positionWgt")
        sizePolicy.setHeightForWidth(self.positionWgt.sizePolicy().hasHeightForWidth())
        self.positionWgt.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.positionWgt)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.positionXLbl = QLabel(self.positionWgt)
        self.positionXLbl.setObjectName(u"positionXLbl")

        self.horizontalLayout_4.addWidget(self.positionXLbl)

        self.positionXLineEdit = QLineEdit(self.positionWgt)
        self.positionXLineEdit.setObjectName(u"positionXLineEdit")
        sizePolicy2.setHeightForWidth(self.positionXLineEdit.sizePolicy().hasHeightForWidth())
        self.positionXLineEdit.setSizePolicy(sizePolicy2)
        self.positionXLineEdit.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.positionXLineEdit)

        self.positionYLbl = QLabel(self.positionWgt)
        self.positionYLbl.setObjectName(u"positionYLbl")

        self.horizontalLayout_4.addWidget(self.positionYLbl)

        self.positionYLineEdit = QLineEdit(self.positionWgt)
        self.positionYLineEdit.setObjectName(u"positionYLineEdit")
        sizePolicy2.setHeightForWidth(self.positionYLineEdit.sizePolicy().hasHeightForWidth())
        self.positionYLineEdit.setSizePolicy(sizePolicy2)
        self.positionYLineEdit.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.positionYLineEdit)


        self.verticalLayout_6.addWidget(self.positionWgt)


        self.horizontalLayout_3.addWidget(self.windowsWgt)


        self.verticalLayout_4.addWidget(self.widget_8)


        self.horizontalLayout_6.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.detailWgt)


        self.retranslateUi(accWgt)

        QMetaObject.connectSlotsByName(accWgt)
    # setupUi

    def retranslateUi(self, accWgt):
        accWgt.setWindowTitle(QCoreApplication.translate("accWgt", u"Form", None))
        self.accNumLbl.setText(QCoreApplication.translate("accWgt", u"1", None))
        self.accNameLbl.setText(QCoreApplication.translate("accWgt", u"\u540d\u7a31", None))
        self.label_2.setText(QCoreApplication.translate("accWgt", u"\u3000\u3000\u72c0\u614b\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("accWgt", u"\u958b\u555f\u6642\u9593\uff1a", None))
        self.openCloseBtn.setText(QCoreApplication.translate("accWgt", u"\u958b\u555f/\u95dc\u9589", None))
        self.resetWindowBtn.setText(QCoreApplication.translate("accWgt", u"\u91cd\u88fd\u8996\u7a97\u5927\u5c0f", None))
        self.usernameLbl.setText(QCoreApplication.translate("accWgt", u"\u5e33\u865f", None))
        self.usernameLineEdit.setText(QCoreApplication.translate("accWgt", u"account", None))
        self.passwordLbl.setText(QCoreApplication.translate("accWgt", u"\u5bc6\u78bc", None))
        self.passwordLineEdit.setText(QCoreApplication.translate("accWgt", u"password", None))
        self.lastLoginLbl.setText(QCoreApplication.translate("accWgt", u"\u4e0a\u6b21", None))
        self.lastLoginLineEdit.setText(QCoreApplication.translate("accWgt", u"2021/06/26", None))
        self.label_7.setText(QCoreApplication.translate("accWgt", u"\u8996\u7a97\u8a2d\u5b9a", None))
        self.label_8.setText(QCoreApplication.translate("accWgt", u"\u5927\u5c0f\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("accWgt", u"\u4f4d\u7f6e\uff1a", None))
        self.windowCfgCbox.setItemText(0, QCoreApplication.translate("accWgt", u"\u9810\u8a2d", None))
        self.windowCfgCbox.setItemText(1, QCoreApplication.translate("accWgt", u"\u507d\u5168\u87a2\u5e55", None))
        self.windowCfgCbox.setItemText(2, QCoreApplication.translate("accWgt", u"\u5168\u87a2\u5e55\u7559\u908a", None))
        self.windowCfgCbox.setItemText(3, QCoreApplication.translate("accWgt", u"\u81ea\u8a02", None))

        self.sizeXLbl.setText(QCoreApplication.translate("accWgt", u"X\uff1a", None))
        self.sizeYLbl.setText(QCoreApplication.translate("accWgt", u"  Y\uff1a", None))
        self.positionXLbl.setText(QCoreApplication.translate("accWgt", u"X\uff1a", None))
        self.positionYLbl.setText(QCoreApplication.translate("accWgt", u"  Y\uff1a", None))
    # retranslateUi

