# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.user import User
from ui.connection import Connection
from ui.main import Ui_MainWindow
from ui.habits import Habits
import ui.app as App
from ui.scrollableVbox import ScrollableVbox

loginfile = open('test_credentials')
username = loginfile.readline().strip()
password = loginfile.readline().strip()
loginfile.close()

connection = Connection()
connection.login(username,password)

user = None


class InterfaceWindow(Ui_MainWindow):

    def setupUi(self, MainWindow):
        self.main = MainWindow
        super().setupUi(MainWindow)
        user = User(window=self)
        user.update_status()
        self.habitsLayout = None
        

    


        





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = InterfaceWindow()
    ui.setupUi(MainWindow)
    App.window = ui
    Habits.update_all()
    MainWindow.show()
    sys.exit(app.exec_())

