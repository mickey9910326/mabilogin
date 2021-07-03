# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acc_setting_wgt.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_accSettingWgt(object):
    def setupUi(self, accSettingWgt):
        if not accSettingWgt.objectName():
            accSettingWgt.setObjectName(u"accSettingWgt")
        accSettingWgt.resize(365, 134)
        self.verticalLayout = QVBoxLayout(accSettingWgt)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mabiFolderLbl = QLabel(accSettingWgt)
        self.mabiFolderLbl.setObjectName(u"mabiFolderLbl")

        self.horizontalLayout_2.addWidget(self.mabiFolderLbl)

        self.mabiFolderLineEdit = QLineEdit(accSettingWgt)
        self.mabiFolderLineEdit.setObjectName(u"mabiFolderLineEdit")

        self.horizontalLayout_2.addWidget(self.mabiFolderLineEdit)

        self.mabiFolderBtn = QPushButton(accSettingWgt)
        self.mabiFolderBtn.setObjectName(u"mabiFolderBtn")

        self.horizontalLayout_2.addWidget(self.mabiFolderBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.openCountLbl = QLabel(accSettingWgt)
        self.openCountLbl.setObjectName(u"openCountLbl")

        self.horizontalLayout_13.addWidget(self.openCountLbl)

        self.openCountSpinBox = QSpinBox(accSettingWgt)
        self.openCountSpinBox.setObjectName(u"openCountSpinBox")

        self.horizontalLayout_13.addWidget(self.openCountSpinBox)


        self.gridLayout.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.openDelayLbl = QLabel(accSettingWgt)
        self.openDelayLbl.setObjectName(u"openDelayLbl")

        self.horizontalLayout_12.addWidget(self.openDelayLbl)

        self.openDelayLineEdit = QLineEdit(accSettingWgt)
        self.openDelayLineEdit.setObjectName(u"openDelayLineEdit")

        self.horizontalLayout_12.addWidget(self.openDelayLineEdit)


        self.gridLayout.addLayout(self.horizontalLayout_12, 0, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.startNumLbl = QLabel(accSettingWgt)
        self.startNumLbl.setObjectName(u"startNumLbl")

        self.horizontalLayout_10.addWidget(self.startNumLbl)

        self.startLineLineEdit = QLineEdit(accSettingWgt)
        self.startLineLineEdit.setObjectName(u"startLineLineEdit")

        self.horizontalLayout_10.addWidget(self.startLineLineEdit)


        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.endNumLbl = QLabel(accSettingWgt)
        self.endNumLbl.setObjectName(u"endNumLbl")

        self.horizontalLayout_11.addWidget(self.endNumLbl)

        self.endNumLineEdit = QLineEdit(accSettingWgt)
        self.endNumLineEdit.setObjectName(u"endNumLineEdit")

        self.horizontalLayout_11.addWidget(self.endNumLineEdit)


        self.gridLayout.addLayout(self.horizontalLayout_11, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.startBtn = QPushButton(accSettingWgt)
        self.startBtn.setObjectName(u"startBtn")

        self.horizontalLayout_9.addWidget(self.startBtn)

        self.stopBtn = QPushButton(accSettingWgt)
        self.stopBtn.setObjectName(u"stopBtn")

        self.horizontalLayout_9.addWidget(self.stopBtn)

        self.cloneBtn = QPushButton(accSettingWgt)
        self.cloneBtn.setObjectName(u"cloneBtn")

        self.horizontalLayout_9.addWidget(self.cloneBtn)

        self.configBtn = QPushButton(accSettingWgt)
        self.configBtn.setObjectName(u"configBtn")

        self.horizontalLayout_9.addWidget(self.configBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(accSettingWgt)

        QMetaObject.connectSlotsByName(accSettingWgt)
    # setupUi

    def retranslateUi(self, accSettingWgt):
        accSettingWgt.setWindowTitle(QCoreApplication.translate("accSettingWgt", u"Form", None))
        self.mabiFolderLbl.setText(QCoreApplication.translate("accSettingWgt", u"\u746a\u5947\u8cc7\u6599\u593e\uff1a", None))
        self.mabiFolderBtn.setText(QCoreApplication.translate("accSettingWgt", u"....", None))
        self.openCountLbl.setText(QCoreApplication.translate("accSettingWgt", u"\u958b\u555f\u6578\u91cf\uff1a", None))
        self.openDelayLbl.setText(QCoreApplication.translate("accSettingWgt", u"\u6642\u9593\u9593\u9694\uff1a", None))
        self.startNumLbl.setText(QCoreApplication.translate("accSettingWgt", u"\u958b\u59cb\u7de8\u865f\uff1a", None))
        self.endNumLbl.setText(QCoreApplication.translate("accSettingWgt", u"\u7d50\u675f\u7de8\u865f\uff1a", None))
        self.startBtn.setText(QCoreApplication.translate("accSettingWgt", u"\u555f\u52d5", None))
        self.stopBtn.setText(QCoreApplication.translate("accSettingWgt", u"\u4e2d\u65b7", None))
        self.cloneBtn.setText(QCoreApplication.translate("accSettingWgt", u"\u95dc\u9589", None))
        self.configBtn.setText(QCoreApplication.translate("accSettingWgt", u"\u8a2d\u5b9a\u6a94", None))
    # retranslateUi

