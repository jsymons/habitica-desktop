from .taskWidget import TaskWidget
from .habitica_api.todo import ToDo
from .connection import Connection
import ui.app as App
from PyQt5 import QtCore, QtGui, QtWidgets
from .scrollableVbox import ScrollableVbox



class ToDos(ToDo):

	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.widget = TaskWidget(self)
		ToDos.all.append(self)
	
	

	@classmethod
	def update_all(cls):
		task_type = 'todos'
		todos = Connection.active.get_tasks(task_type)
		if todos is not None:
			if App.window.todosLayout is not None:
				App.window.main.removeWidget(App.window.todosLayout)
			ToDos.all = []
			widgets = []
			for todo in todos:
				widgets.append(ToDos(**todo).widget)
			App.window.todosLayout = ScrollableVbox((520,60,260,545),widgets,App.window.main)

