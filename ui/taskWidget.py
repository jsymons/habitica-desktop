from PyQt5 import QtCore, QtGui, QtWidgets

class TaskWidget(QtWidgets.QFrame):



	def __init__(self,task,parent=None):

		super().__init__(parent)


		self.task = task

		
		QtWidgets.QFrame.__init__(self, parent)

		self.setFixedSize(210,57)

		self.setContentsMargins(0,0,0,0)

		self.setStyleSheet(".TaskWidget{background-color: rgb(170,255,127);border-radius:5px;}")

		taskLabel = QtWidgets.QLabel(self.tr(self.task.title))
		taskLabel.setGeometry(QtCore.QRect(0,0,161,41))

		if self.task.type == 'habit':
			self.positiveButton = QtWidgets.QPushButton()
			self.positiveButton.setText("+")
			self.positiveButton.setFixedSize(31,22)
			
			self.negativeButton = QtWidgets.QPushButton()
			self.negativeButton.setText("-")
			self.negativeButton.setFixedSize(31,22)
		else:
			self.checkbox = QtWidgets.QCheckBox()
			self.checkbox.setFixedSize(31,44)

		


		layout = QtWidgets.QGridLayout(self)
		layout.setGeometry(QtCore.QRect(0,0,210,57))


		if self.task.type == 'habit':
			if self.task.up and self.task.down:
				layout.addWidget(self.positiveButton, 0, 0)
				layout.addWidget(self.negativeButton, 1, 0)
				layout.addWidget(taskLabel, 0, 1, 2, 1)
			elif self.task.up:
				self.positiveButton.setFixedSize(31,44)
				layout.addWidget(self.positiveButton,0,0)
				layout.addWidget(taskLabel,0,1)
			elif self.task.down:
				self.negativeButton.setFixedSize(31,44)
				layout.addWidget(self.negativeButton,0,0)
				layout.addWidget(taskLabel,0,1)
		else:
			layout.addWidget(self.checkbox,0,0)
			layout.addWidget(taskLabel,0,1)

		

