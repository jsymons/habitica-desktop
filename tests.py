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



		