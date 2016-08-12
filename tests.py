import unittest

from habitica_api.user import User
from habitica_api import task
from habitica_api.connection import Connection
from habitica_api.daily import Daily
from habitica_api.habit import Habit
from habitica_api.todo import ToDo
from habitica_api.tag import Tag

loginfile = open('test_credentials')
username = loginfile.readline().strip()
password = loginfile.readline().strip()
loginfile.close()


class TestAPILogin(unittest.TestCase):

	def test_login(self):
		connection = Connection()
		connection.login(username,password)
		self.assertTrue(connection.login_status)


class TestUserProfile(unittest.TestCase):

	def setUp(self):
		connection = Connection()
		connection.login(username,password)
		self.user = User()
		

	def test_status_update(self):
		self.assertTrue(self.user.update_status())


class TestHabits(unittest.TestCase):

	def setUp(self):
		connection = Connection()
		connection.login(username,password)
		self.user = User()
		Habit.update_all()

	def test_read_habits(self):
		test_task_name = "Test habit"
		self.assertIn(test_task_name,[habit.title for habit in Habit.all])

	def test_add_habit(self):
		test_task = {}
		test_task['title'] = "Test creation habit"
		test_task['notes'] = "Test habit notes"
		test_task['up'] = True
		test_task['down'] = False
		test_task['difficulty'] = 1.5

		Habit.add(**test_task)
		self.assertTrue(test_task['title'] in [habit.title for habit in Habit.all])
		for habit in [habit for habit in Habit.all if habit.title == test_task['title']]:
			self.assertEqual(habit.notes,test_task['notes'], 'Notes do not match')
			self.assertEqual(habit.up,test_task['up'], 'Up is set to false')
			self.assertEqual(habit.down,test_task['down'], 'Down is set to true')
			self.assertEqual(habit.difficulty,test_task['difficulty'], 'Difficulty does not match')
			habit.delete()

	def test_delete_habit(self):
		test_task = {}
		test_task['title'] = "Test deletion habit"
		Habit.add(**test_task)
		for habit in Habit.all:
			if habit.title == test_task['title']:
				habit.delete()
		self.assertNotIn(test_task['title'],[habit.title for habit in Habit.all])

	def test_edit_habit(self):
		test_task = {}
		test_task['title'] = "Test modification habit"
		test_task['notes'] = "Test habit notes"
		test_task['up'] = True
		test_task['down'] = False
		test_task['difficulty'] = 1.5
		Habit.add(**test_task)
		edited_task = {}
		edited_task['title'] = "Test modified habit"
		edited_task['notes'] = "Modified notes"
		edited_task['up'] = False
		edited_task['down'] = True
		edited_task['difficulty'] = 0.1
		for habit in [habit for habit in Habit.all if habit.title == test_task['title']]:
			habit.modify(edited_task)
			self.assertNotEqual(test_task['title'],habit.title)
			self.assertEqual(edited_task['title'],habit.title)
			self.assertEqual(habit.notes,edited_task['notes'])
			self.assertEqual(habit.up,edited_task['up'],"Habit up is %s, should be %s" % (habit.up,edited_task['up']))
			self.assertEqual(habit.down,edited_task['down'])
			self.assertEqual(habit.difficulty,edited_task['difficulty'])
			habit.delete()

class TestDailies(unittest.TestCase):
	def setUp(self):
		connection = Connection()
		connection.login(username,password)
		self.user = User()
		Daily.update_all()

	def test_read_dailies(self):
		test_task_name = "Test daily"
		self.assertIn(test_task_name,[daily.title for daily in Daily.all])

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

		Daily.add(**test_task)
		self.assertIn(test_task['title'],[daily.title for daily in Daily.all])
		for daily in [daily for daily in Daily.all if daily.title == test_task['title']]:
			self.assertEqual(daily.notes,test_task['notes'])
			self.assertEqual(daily.difficulty,test_task['difficulty'])
			self.assertEqual(daily.repeat,test_task['repeat'])
			self.assertEqual(daily.frequency,test_task['frequency'])
			daily.delete()

	def test_add_xdays_daily(self):
		test_task = {}
		test_task['title'] = "Test xdays daily"
		test_task['everyX'] = 5
		test_task['frequency'] = 'daily'
		Daily.add(**test_task)
		self.assertIn(test_task['title'],[daily.title for daily in Daily.all])
		for daily in [daily for daily in Daily.all if daily.title == test_task['title']]:
			self.assertEqual(daily.everyX,test_task['everyX'])
			self.assertEqual(daily.frequency,test_task['frequency'])


	def test_delete_daily(self):
		test_task = {}
		test_task['title'] = "Test deletion daily"
		Daily.add(**test_task)
		for daily in Daily.all:
			if daily.title == test_task['title']:
				daily.delete()
		self.assertNotIn(test_task['title'],[daily.title for daily in Daily.all])




class TestTodos(unittest.TestCase):
	def setUp(self):
		connection = Connection()
		connection.login(username,password)
		self.user = User()
		ToDo.update_all()

	def test_read_todos(self):
		test_task_name = "Test todo"
		self.assertIn(test_task_name,[todo.title for todo in ToDo.all])

	def test_add_todo(self):
		test_task = {}
		test_task['title'] = "Test creation todo"
		test_task['notes'] = "Test notes"
		test_task['date'] = "2016-12-25"
		test_task['difficulty'] = 2
		
		ToDo.add(**test_task)
		self.assertIn(test_task['title'],[todo.title for todo in ToDo.all])
		for todo in [todo for todo in ToDo.all if todo.title == test_task['title']]:
			self.assertEqual(todo.notes,test_task['notes'])
			self.assertTrue(todo.due_date.startswith(test_task['date']), 'Date mismatch: %s vs. %s' % (test_task['date'],todo.due_date))
			self.assertEqual(todo.difficulty,test_task['difficulty'])
			todo.delete()

	def test_delete_todo(self):
		test_task = {}
		test_task['title'] = "Test deletion todo"
		ToDo.add(**test_task)
		for todo in ToDo.all:
			if todo.title == test_task['title']:
				todo.delete()
		self.assertNotIn(test_task['title'],[todo.title for todo in ToDo.all])




class TestChecklists(unittest.TestCase):
	def setUp(self):
		connection = Connection()
		connection.login(username,password)
		self.user = User()
		Daily.update_all()
		Habit.update_all()
		ToDo.update_all()

	def test_add_checklist_item(self):
		test_task = {}
		test_task['title'] = "Test checklist todo"
		ToDo.add(**test_task)
		checklist_text = "Test checklist item"
		for todo in [todo for todo in ToDo.all if todo.title == test_task['title']]:
			todo.add_to_checklist(checklist_text)
			checklist_titles = [checklist_item['text'] for checklist_item in todo.checklist]
			self.assertIn(checklist_text,checklist_titles,"%s not in %s" % (checklist_text, checklist_titles))
			todo.delete()

	def test_delete_checklist_item(self):
		test_task = {}
		test_task['title'] = "Test checklist deletion todo"
		ToDo.add(**test_task)
		checklist_text = "I shouldn't be here"
		for todo in [todo for todo in ToDo.all if todo.title == test_task['title']]:
			todo.add_to_checklist(checklist_text)
			checklist_id = [checklist_item['id'] for checklist_item in todo.checklist if checklist_item['text'] == checklist_text][0]
			todo.delete_from_checklist(checklist_id)
			self.assertNotIn(checklist_text,[checklist_item['text'] for checklist_item in todo.checklist])
			todo.delete()

	def test_edit_checklist_item(self):
		test_task = {}
		test_task['title'] = "Test checklist edit todo"
		ToDo.add(**test_task)
		checklist_text = "You shouldn't see me."
		for todo in [todo for todo in ToDo.all if todo.title == test_task['title']]:
			todo.add_to_checklist(checklist_text)
			edited_text = "I'm what you should see."
			checklist_item = {}
			checklist_item['id'] = [checklist_item['id'] for checklist_item in todo.checklist if checklist_item['text'] == checklist_text][0]
			checklist_item['text'] = edited_text
			todo.edit_checklist(**checklist_item)
			checklist = [checklist_item['text'] for checklist_item in todo.checklist]
			self.assertNotIn(checklist_text,checklist)
			self.assertIn(edited_text,checklist)
			todo.delete()




class TestScoring(unittest.TestCase):
	def setUp(self):
		connection = Connection()
		connection.login(username,password)
		self.user = User()
		Daily.update_all()
		Habit.update_all()
		ToDo.update_all()

	def test_score_task(self):
		test_task = {}
		test_task['title'] = "Test score daily"
		Daily.add(**test_task)
		for daily in [daily for daily in Daily.all if daily.title == test_task['title']]:
			daily.score()
			self.assertTrue(daily.completed)
			daily.delete()

	def test_score_habit(self):
		test_task = {}
		test_task['title'] = "Test score habit"
		test_task['up'] = True
		test_task['down'] = True
		Habit.add(**test_task)
		self.user.update_status()
		current_xp = self.user.profile['stats']['exp']
		current_hp = self.user.profile['stats']['hp']
		for habit in [habit for habit in Habit.all if habit.title == test_task['title']]:
			habit.score('up')
			self.user.update_status()
			self.assertNotEqual(current_xp,self.user.profile['stats']['exp'],'XP has not changed')
			habit.score('down')
			self.user.update_status()
			self.assertNotEqual(current_hp,self.user.profile['stats']['hp'],'HP has not changed')
			habit.delete()

	def test_score_checklist(self):
		test_task = {}
		test_task['title'] = "Test score checklist"
		ToDo.add(**test_task)
		checklist_text = "Check me off!"
		for todo in [todo for todo in ToDo.all if todo.title == test_task['title']]:
			todo.add_to_checklist(checklist_text)
			todo.score_checklist(todo.checklist[0]['id'])
			self.assertTrue(todo.checklist[0]['completed'])
			todo.delete()





class TestTagging(unittest.TestCase):

	def setUp(self):
		connection = Connection()
		connection.login(username,password)
		self.user = User()
		Daily.update_all()
		Habit.update_all()
		ToDo.update_all()
		Tag.update_all()
		

	def test_read_tags(self):
		self.assertTrue(len(Tag.all) > 0)