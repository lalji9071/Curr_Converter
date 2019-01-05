# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_converter(object):
    def setupUi(self, converter):
        converter.setObjectName("converter")
        converter.resize(512, 157)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/images/LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        converter.setWindowIcon(icon)
        converter.setWindowOpacity(3.0)
        self.lineEdit = QtWidgets.QLineEdit(converter)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(converter)
        self.pushButton.setGeometry(QtCore.QRect(190, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(converter)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(converter)
        QtCore.QMetaObject.connectSlotsByName(converter)

    def retranslateUi(self, converter):
        _translate = QtCore.QCoreApplication.translate
        converter.setWindowTitle(_translate("converter", "Currency Converter by Lalji"))
        self.pushButton.setText(_translate("converter", "-->"))

import image_rc
