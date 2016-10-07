from .taskWidget import TaskWidget
from .habitica_api.daily import Daily
from .connection import Connection
import ui.app as App
from PyQt5 import QtCore, QtGui, QtWidgets
from .scrollableVbox import ScrollableVbox



class Dailies(Daily):

	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.widget = TaskWidget(self)
		Dailies.all.append(self)
	
	

	@classmethod
	def update_all(cls):
		task_type = 'dailys'
		dailies = Connection.active.get_tasks(task_type)
		if dailies is not None:
			if App.window.dailiesLayout is not None:
				App.window.main.removeWidget(App.window.dailiesLayout)
			Dailies.all = []
			widgets = []
			for daily in dailies:
				widgets.append(Dailies(**daily).widget)
			App.window.dailiesLayout = ScrollableVbox((260,60,260,545),widgets,App.window.main)

