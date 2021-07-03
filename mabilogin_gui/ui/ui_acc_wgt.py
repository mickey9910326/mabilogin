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
        self.label = QLabel(self.accNameWgt)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)


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
        self.pushButton = QPushButton(self.accCtlWgt)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_7.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.accCtlWgt)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_7.addWidget(self.pushButton_2)


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
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)


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

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_6 = QVBoxLayout(self.widget_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboBox = QComboBox(self.widget_9)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_6.addWidget(self.comboBox)

        self.widget_7 = QWidget(self.widget_9)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_7)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.lineEdit_6 = QLineEdit(self.widget_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy2)
        self.lineEdit_6.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_6)

        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.lineEdit_7 = QLineEdit(self.widget_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy2.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy2)
        self.lineEdit_7.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_7)


        self.verticalLayout_6.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.widget_9)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_6)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.lineEdit_4 = QLineEdit(self.widget_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy2.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy2)
        self.lineEdit_4.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.lineEdit_5 = QLineEdit(self.widget_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy2.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy2)
        self.lineEdit_5.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_5)


        self.verticalLayout_6.addWidget(self.widget_6)


        self.horizontalLayout_3.addWidget(self.widget_9)


        self.verticalLayout_4.addWidget(self.widget_8)


        self.horizontalLayout_6.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.detailWgt)


        self.retranslateUi(accWgt)

        QMetaObject.connectSlotsByName(accWgt)
    # setupUi

    def retranslateUi(self, accWgt):
        accWgt.setWindowTitle(QCoreApplication.translate("accWgt", u"Form", None))
        self.accNumLbl.setText(QCoreApplication.translate("accWgt", u"1", None))
        self.label.setText(QCoreApplication.translate("accWgt", u"\u540d\u7a31", None))
        self.label_2.setText(QCoreApplication.translate("accWgt", u"\u3000\u3000\u72c0\u614b\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("accWgt", u"\u958b\u555f\u6642\u9593\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("accWgt", u"\u958b\u555f/\u95dc\u9589", None))
        self.pushButton_2.setText(QCoreApplication.translate("accWgt", u"\u91cd\u88fd\u8996\u7a97\u5927\u5c0f", None))
        self.label_4.setText(QCoreApplication.translate("accWgt", u"\u5e33\u865f", None))
        self.lineEdit.setText(QCoreApplication.translate("accWgt", u"account", None))
        self.label_5.setText(QCoreApplication.translate("accWgt", u"\u5bc6\u78bc", None))
        self.lineEdit_2.setText(QCoreApplication.translate("accWgt", u"password", None))
        self.label_6.setText(QCoreApplication.translate("accWgt", u"\u4e0a\u6b21", None))
        self.lineEdit_3.setText(QCoreApplication.translate("accWgt", u"2021/06/26", None))
        self.label_7.setText(QCoreApplication.translate("accWgt", u"\u8996\u7a97\u8a2d\u5b9a", None))
        self.label_8.setText(QCoreApplication.translate("accWgt", u"\u5927\u5c0f\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("accWgt", u"\u4f4d\u7f6e\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("accWgt", u"\u9810\u8a2d", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("accWgt", u"\u507d\u5168\u87a2\u5e55", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("accWgt", u"\u5168\u87a2\u5e55\u7559\u908a", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("accWgt", u"\u81ea\u8a02", None))

        self.label_12.setText(QCoreApplication.translate("accWgt", u"X\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("accWgt", u"  Y\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("accWgt", u"X\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("accWgt", u"  Y\uff1a", None))
    # retranslateUi

