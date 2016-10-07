from .taskWidget import TaskWidget
from .habitica_api.habit import Habit
from .connection import Connection
import ui.app as App
from PyQt5 import QtCore, QtGui, QtWidgets
from .scrollableVbox import ScrollableVbox



class Habits(Habit):

	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.widget = TaskWidget(self)
		Habits.all.append(self)
	
	def score_positive(self):
		self.score(direction='up')

	def score_negative(self):
		self.score(direction='down')

	@classmethod
	def update_all(cls):
		task_type = 'habits'
		habits = Connection.active.get_tasks(task_type)
		if habits is not None:
			if App.window.habitsLayout is not None:
				App.window.main.removeWidget(App.window.habitsLayout)
			Habits.all = []
			widgets = []
			for habit in habits:
				widgets.append(Habits(**habit).widget)
			App.window.habitsLayout = ScrollableVbox((0,60,260,545),widgets,App.window.main)

