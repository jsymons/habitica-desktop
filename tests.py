import unittest

from habitica_api import user
from habitica_api import task

loginfile = open('test_credentials')
username = loginfile.readline().strip()
password = loginfile.readline().strip()
loginfile.close()

class TestAPILogin(unittest.TestCase):

	def setUp(self):
		self.user = user.NewLogin()
		

	def test_not_logged_in(self):
		self.assertFalse(self.user.login_status)

	def test_login(self):
		self.user.login(username,password)
		self.assertTrue(self.user.login_status)


class TestUserProfile(unittest.TestCase):

	def setUp(self):
		self.user = user.NewLogin()
		self.user.login(username,password)
		

	def test_status_update(self):
		self.assertTrue(self.user.update_status())

class TestTasks(unittest.TestCase):

	def setUp(self):
		self.user = user.NewLogin()
		self.user.login(username,password)
		self.user.update_tasks()
		

	def tearDown(self):
		for habit in self.user.habits:
			if habit.title == "Test creation habit":
				habit.delete()

		for daily in self.user.dailies:
			if daily.title == "Test creation daily":
				daily.delete()

		for todo in self.user.todos:
			if todo.title == "Test creation todo":
				todo.delete()
		
	def test_read_habits(self):
		test_task_name = "Test habit"
		self.assertTrue(test_task_name in [habit.title for habit in self.user.habits])

	def test_add_habit(self):
		test_task = {}
		test_task['title'] = "Test creation habit"
		test_task['notes'] = "Test habit notes"
		test_task['up'] = True
		test_task['down'] = False
		test_task['difficulty'] = 1.5

		self.user.add_habit(**test_task)
		self.assertTrue(test_task['title'] in [habit.title for habit in self.user.habits])
		for habit in [habit for habit in self.user.habits if habit.title == test_task['title']]:
			self.assertTrue(habit.notes == test_task['notes'], 'Notes do not match')
			self.assertTrue(habit.up == test_task['up'], 'Up is set to false')
			self.assertTrue(habit.down == test_task['down'], 'Down is set to true')
			self.assertTrue(habit.difficulty == test_task['difficulty'], 'Difficulty does not match')

	def test_delete_habit(self):
		test_task_name = "Test deletion habit"
		self.user.add_habit(test_task_name)
		task_id = ""
		for habit in self.user.habits:
			if habit.title == test_task_name:
				habit.delete()
		self.assertFalse(test_task_name in [habit.title for habit in self.user.habits])
	
	def test_read_dailies(self):
		test_task_name = "Test daily"
		self.assertTrue(test_task_name in [daily.title for daily in self.user.dailies])

	def test_add_daily(self):
		test_task_name = "Test creation daily"
		self.user.add_daily(test_task_name)
		self.assertTrue(test_task_name in [daily.title for daily in self.user.dailies])

	def test_delete_daily(self):
		test_task_name = "Test deletion daily"
		self.user.add_daily(test_task_name)
		for daily in self.user.dailies:
			if daily.title == test_task_name:
				daily.delete()
		self.assertFalse(test_task_name in [daily.title for daily in self.user.dailies])

	def test_read_todos(self):
		test_task_name = "Test todo"
		self.assertTrue(test_task_name in [todo.title for todo in self.user.todos])

	def test_add_todo(self):
		test_task_name = "Test creation todo"
		self.user.add_todo(test_task_name)
		self.assertTrue(test_task_name in [todo.title for todo in self.user.todos])

	def test_delete_todo(self):
		test_task_name = "Test deletion todo"
		self.user.add_todo(test_task_name)
		for todo in self.user.todos:
			if todo.title == test_task_name:
				todo.delete()
		self.assertFalse(test_task_name in [todo.title for todo in self.user.todos])