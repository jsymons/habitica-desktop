import unittest

from habitica_api.user import User
from habitica_api import task
from habitica_api import habitica

loginfile = open('test_credentials')
username = loginfile.readline().strip()
password = loginfile.readline().strip()
loginfile.close()

def helper_title_matcher(search_in,search_for):
	return [search_item for search_item in search_in if search_item.title == search_for]

class TestAPILogin(unittest.TestCase):

	def test_login(self):
		connection = habitica.Connection()
		connection.login(username,password)
		self.assertTrue(connection.login_status)


class TestUserProfile(unittest.TestCase):

	def setUp(self):
		connection = habitica.Connection()
		connection.login(username,password)
		self.user = User(connection)
		

	def test_status_update(self):
		self.assertTrue(self.user.update_status())

class TestTasks(unittest.TestCase):

	def setUp(self):
		connection = habitica.Connection()
		connection.login(username,password)
		self.user = User(connection)
		self.user.update_tasks()
		

	def tearDown(self):
		for habit in self.user.habits:
			if habit.title == "Test creation habit":
				habit.delete()

		for daily in self.user.dailies:
			if daily.title == "Test creation daily" or daily.title == "Test xdays daily":
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
			self.assertEqual(habit.notes,test_task['notes'], 'Notes do not match')
			self.assertEqual(habit.up,test_task['up'], 'Up is set to false')
			self.assertEqual(habit.down,test_task['down'], 'Down is set to true')
			self.assertEqual(habit.difficulty,test_task['difficulty'], 'Difficulty does not match')

	def test_delete_habit(self):
		test_task_name = "Test deletion habit"
		self.user.add_habit(test_task_name)
		for habit in self.user.habits:
			if habit.title == test_task_name:
				habit.delete()
		self.assertFalse(test_task_name in [habit.title for habit in self.user.habits])

	def test_edit_task(self):
		test_task = {}
		test_task['title'] = "Test modification habit"
		test_task['notes'] = "Test habit notes"
		test_task['up'] = True
		test_task['down'] = False
		test_task['difficulty'] = 1.5
		self.user.add_habit(**test_task)
		edited_task = {}
		edited_task['title'] = "Test modified habit"
		edited_task['notes'] = "Modified notes"
		edited_task['up'] = False
		edited_task['down'] = True
		edited_task['difficulty'] = 0.1
		for habit in [habit for habit in self.user.habits if habit.title == test_task['title']]:
			habit.modify(edited_task)
		self.assertFalse(test_task['title'] in [habit.title for habit in self.user.habits], "Original task title still exits")
		self.assertTrue(edited_task['title'] in [habit.title for habit in self.user.habits])
		for habit in [habit for habit in self.user.habits if habit.title == edited_task['title']]:
			self.assertEqual(habit.notes,edited_task['notes'])
			self.assertEqual(habit.up,edited_task['up'])
			self.assertEqual(habit.down,edited_task['down'])
			self.assertEqual(habit.difficulty,edited_task['difficulty'])
			habit.delete()
	
	def test_read_dailies(self):
		test_task_name = "Test daily"
		self.assertTrue(test_task_name in [daily.title for daily in self.user.dailies])

	def test_add_daily(self):
		test_task = {}
		test_task['title'] = "Test creation daily"
		test_task['notes'] = "Test daily notes"
		test_task['difficulty'] = 2
		test_task['repeat'] = {
			'su': True,
			'm': False,
			't': True,
			'w': False,
			'th': True,
			'f': False,
			's': True
		}
		test_task['frequency'] = 'weekly'

		self.user.add_daily(**test_task)
		self.assertTrue(test_task['title'] in [daily.title for daily in self.user.dailies])
		for daily in [daily for daily in self.user.dailies if daily.title == test_task['title']]:
			self.assertEqual(daily.notes,test_task['notes'])
			self.assertEqual(daily.difficulty,test_task['difficulty'])
			self.assertEqual(daily.repeat,test_task['repeat'])
			self.assertEqual(daily.frequency,test_task['frequency'])

	def test_add_xdays_daily(self):
		test_task = {}
		test_task['title'] = "Test xdays daily"
		test_task['everyX'] = 5
		test_task['frequency'] = 'daily'
		self.user.add_daily(**test_task)
		self.assertTrue(test_task['title'] in [daily.title for daily in self.user.dailies])
		for daily in [daily for daily in self.user.dailies if daily.title == test_task['title']]:
			self.assertEqual(daily.everyX,test_task['everyX'])
			self.assertEqual(daily.frequency,test_task['frequency'])


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
		test_task = {}
		test_task['title'] = "Test creation todo"
		test_task['notes'] = "Test notes"
		test_task['date'] = "2016-12-25"
		test_task['difficulty'] = 2
		
		self.user.add_todo(**test_task)
		self.assertTrue(test_task['title'] in [todo.title for todo in self.user.todos])
		for todo in [todo for todo in self.user.todos if todo.title == test_task['title']]:
			self.assertEqual(todo.notes,test_task['notes'])
			self.assertTrue(todo.due_date.startswith(test_task['date']), 'Date mismatch: %s vs. %s' % (test_task['date'],todo.due_date))
			self.assertEqual(todo.difficulty,test_task['difficulty'])

	def test_delete_todo(self):
		test_task_name = "Test deletion todo"
		self.user.add_todo(test_task_name)
		for todo in self.user.todos:
			if todo.title == test_task_name:
				todo.delete()
		self.assertFalse(test_task_name in [todo.title for todo in self.user.todos])


	def test_add_checklist_item(self):
		test_task = {}
		test_task['title'] = "Test checklist todo"
		self.user.add_todo(**test_task)
		checklist_text = "Test checklist item"
		for todo in [todo for todo in self.user.todos if todo.title == test_task['title']]:
			todo.add_to_checklist(checklist_text)
		for todo in [todo for todo in self.user.todos if todo.title == test_task['title']]:
			checklist_titles = [checklist_item['text'] for checklist_item in todo.checklist]
			self.assertTrue(checklist_text in checklist_titles,"%s not in %s" % (checklist_text, checklist_titles))
			todo.delete()

	def test_delete_checklist_item(self):
		test_task = {}
		test_task['title'] = "Test checklist deletion todo"
		self.user.add_todo(**test_task)
		checklist_text = "I shouldn't be here"
		for todo in [todo for todo in self.user.todos if todo.title == test_task['title']]:
			todo.add_to_checklist(checklist_text)
		for todo in [todo for todo in self.user.todos if todo.title == test_task['title']]:
			checklist_id = [checklist_item['id'] for checklist_item in todo.checklist if checklist_item['text'] == checklist_text][0]
			todo.delete_from_checklist(checklist_id)
		for todo in [todo for todo in self.user.todos if todo.title == test_task['title']]:
			self.assertFalse(checklist_text in [checklist_item['text'] for checklist_item in todo.checklist])
			todo.delete()

	def test_edit_checklist_item(self):
		test_task = {}
		test_task['title'] = "Test checklist edit todo"
		self.user.add_todo(**test_task)
		checklist_text = "You shouldn't see me."
		for todo in [todo for todo in self.user.todos if todo.title == test_task['title']]:
			todo.add_to_checklist(checklist_text)
		edited_text = "I'm what you should see."
		for todo in [todo for todo in self.user.todos if todo.title == test_task['title']]:
			checklist_item = {}
			checklist_item['id'] = [checklist_item['id'] for checklist_item in todo.checklist if checklist_item['text'] == checklist_text][0]
			checklist_item['text'] = edited_text
			todo.edit_checklist(**checklist_item)
		for todo in [todo for todo in self.user.todos if todo.title == test_task['title']]:
			checklist = [checklist_item['text'] for checklist_item in todo.checklist]
			self.assertFalse(checklist_text in checklist)
			self.assertTrue(edited_text in checklist)
			todo.delete()

	def test_score_task(self):
		test_task = {}
		test_task['title'] = "Test score daily"
		self.user.add_daily(**test_task)
		for daily in [daily for daily in self.user.dailies if daily.title == test_task['title']]:
			daily.score()
		for daily in [daily for daily in self.user.dailies if daily.title == test_task['title']]:
			self.assertTrue(daily.completed)
			daily.delete()

	def test_score_habit(self):
		test_task = {}
		test_task['title'] = "Test score habit"
		test_task['up'] = True
		test_task['down'] = True
		self.user.add_habit(**test_task)
		self.user.update_status()
		current_xp = self.user.profile['stats']['exp']
		current_hp = self.user.profile['stats']['hp']
		for habit in helper_title_matcher(self.user.habits,test_task['title']):
			habit.score('up')
			self.user.update_status()
			self.assertNotEqual(current_xp,self.user.profile['stats']['exp'],'XP has not changed')
		for habit in helper_title_matcher(self.user.habits,test_task['title']):
			habit.score('down')
			self.user.update_status()
			self.assertNotEqual(current_hp,self.user.profile['stats']['hp'],'HP has not changed')
			habit.delete()

