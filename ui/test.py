# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_habitPosNeg(object):
    def setupUi(self, habitPosNeg):
        habitPosNeg.setObjectName("habitPosNeg")
        habitPosNeg.resize(210, 57)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        habitPosNeg.setPalette(palette)
        habitPosNeg.setAutoFillBackground(True)
        self.positive = QtWidgets.QPushButton(habitPosNeg)
        self.positive.setGeometry(QtCore.QRect(0, 10, 31, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.positive.setFont(font)
        self.positive.setObjectName("positive")
        self.negative = QtWidgets.QPushButton(habitPosNeg)
        self.negative.setGeometry(QtCore.QRect(0, 30, 31, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.negative.setFont(font)
        self.negative.setObjectName("negative")
        self.label = QtWidgets.QLabel(habitPosNeg)
        self.label.setGeometry(QtCore.QRect(40, 10, 161, 41))
        self.label.setObjectName("label")

        self.retranslateUi(habitPosNeg)
        QtCore.QMetaObject.connectSlotsByName(habitPosNeg)

    def retranslateUi(self, habitPosNeg):
        _translate = QtCore.QCoreApplication.translate
        habitPosNeg.setWindowTitle(_translate("habitPosNeg", "Form"))
        self.positive.setText(_translate("habitPosNeg", "+"))
        self.negative.setText(_translate("habitPosNeg", "-"))
        self.label.setText(_translate("habitPosNeg", "TextLabel"))

