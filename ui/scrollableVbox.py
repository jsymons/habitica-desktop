from PyQt5 import QtCore, QtGui, QtWidgets

class ScrollableVbox(QtWidgets.QWidget):

	def __init__(self, geometry, widgets, parent=None):
		super(ScrollableVbox, self).__init__(parent=parent)
		
		
		self.setGeometry(*geometry)

		#Container widget
		widget = QtWidgets.QWidget()

		#Layout of Container Widget
		layout = QtWidgets.QVBoxLayout(self)

		for w in widgets:
			layout.addWidget(w)

		
		widget.setLayout(layout)

		#Scroll Area Properties
		scroll = QtWidgets.QScrollArea()
		scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		scroll.setWidgetResizable(False)
		scroll.setWidget(widget)

		#SCroll Area Layer add
		vLayout = QtWidgets.QVBoxLayout(self)
		vLayout.addWidget(scroll)
		self.setLayout(vLayout)

