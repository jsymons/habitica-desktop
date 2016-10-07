# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'habit_pos.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_habitPositive(object):
    def setupUi(self, habitPositive):
        habitPositive.setObjectName("habitPositive")
        habitPositive.resize(210, 57)
        self.positive = QtWidgets.QPushButton(habitPositive)
        self.positive.setGeometry(QtCore.QRect(0, 11, 31, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.positive.setFont(font)
        self.positive.setObjectName("positive")
        self.label = QtWidgets.QLabel(habitPositive)
        self.label.setGeometry(QtCore.QRect(40, 10, 161, 41))
        self.label.setObjectName("label")

        self.retranslateUi(habitPositive)
        QtCore.QMetaObject.connectSlotsByName(habitPositive)

    def retranslateUi(self, habitPositive):
        _translate = QtCore.QCoreApplication.translate
        habitPositive.setWindowTitle(_translate("habitPositive", "Form"))
        self.positive.setText(_translate("habitPositive", "+"))
        self.label.setText(_translate("habitPositive", "TextLabel"))

