from PyQt5 import QtCore, QtGui, QtWidgets

class HabitWidget(QtWidgets.QFrame):



	def __init__(self,habit,parent=None):

		super().__init__(parent)


		self.habit = habit

		
		QtWidgets.QFrame.__init__(self, parent)

		self.setFixedSize(210,57)

		self.setContentsMargins(0,0,0,0)

		self.setStyleSheet(".HabitWidget{background-color: rgb(170,255,127);border-radius:5px;}")

		habitLabel = QtWidgets.QLabel(self.tr(self.habit.title))
		habitLabel.setGeometry(QtCore.QRect(0,0,161,41))

		self.positiveButton = QtWidgets.QPushButton()
		self.positiveButton.setText("+")
		self.positiveButton.setFixedSize(31,22)
		self.positiveButton.setStyleSheet("initial")

		self.negativeButton = QtWidgets.QPushButton()
		self.negativeButton.setText("-")
		self.negativeButton.setFixedSize(31,22)
		


		layout = QtWidgets.QGridLayout(self)
		layout.setGeometry(QtCore.QRect(0,0,210,57))


		if self.habit.up and self.habit.down:
			layout.addWidget(self.positiveButton, 0, 0)
			layout.addWidget(self.negativeButton, 1, 0)
			layout.addWidget(habitLabel, 0, 1, 2, 1)
		elif self.habit.up:
			self.positiveButton.setFixedSize(31,44)
			layout.addWidget(self.positiveButton,0,0)
			layout.addWidget(habitLabel,0,1)
		elif self.habit.down:
			self.negativeButton.setFixedSize(31,44)
			layout.addWidget(self.negativeButton,0,0)
			layout.addWidget(habitLabel,0,1)

		

