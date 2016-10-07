# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'habit_posneg.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_habitPosNeg(object):
    def setupUi(self, habitPosNeg):
        habitPosNeg.setObjectName("habitPosNeg")
        habitPosNeg.resize(210, 57)
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

