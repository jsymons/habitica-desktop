# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'habit_neg.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_habitNegative(object):
    def setupUi(self, habitNegative):
        habitNegative.setObjectName("habitNegative")
        habitNegative.resize(210, 57)
        self.negative = QtWidgets.QPushButton(habitNegative)
        self.negative.setGeometry(QtCore.QRect(0, 11, 31, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.negative.setFont(font)
        self.negative.setObjectName("negative")
        self.label = QtWidgets.QLabel(habitNegative)
        self.label.setGeometry(QtCore.QRect(40, 10, 161, 41))
        self.label.setObjectName("label")

        self.retranslateUi(habitNegative)
        QtCore.QMetaObject.connectSlotsByName(habitNegative)

    def retranslateUi(self, habitNegative):
        _translate = QtCore.QCoreApplication.translate
        habitNegative.setWindowTitle(_translate("habitNegative", "Form"))
        self.negative.setText(_translate("habitNegative", "-"))
        self.label.setText(_translate("habitNegative", "TextLabel"))

