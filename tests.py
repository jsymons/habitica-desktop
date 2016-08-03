import unittest

from habitica_api import user


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
		self.user.update_habits()

	def tearDown(self):
		for habit in self.user.habits:
			if habit.title == "Test creation habit":
				habit.delete()
		
	def test_read_habits(self):
		test_task_name = "Test habit"
		self.assertTrue(test_task_name in [habit.title for habit in self.user.habits])

	def test_add_habit(self):
		test_task_name = "Test creation habit"
		self.user.add_habit(test_task_name)
		self.assertTrue(test_task_name in [habit.title for habit in self.user.habits])

	def test_delete_habit(self):
		test_task_name = "Test deletion habit"
		self.user.add_habit(test_task_name)
		task_id = ""
		for habit in self.user.habits:
			if habit.title == test_task_name:
				habit.delete()
				break
		self.assertFalse(test_task_name in [habit.title for habit in self.user.habits])
	

