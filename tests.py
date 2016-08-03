import unittest

from habitica_api import user


class TestAPILogin(unittest.TestCase):

	def setUp(self):
		self.user = user.NewLogin()
		loginfile = open('test_credentials')
		self.username = loginfile.readline().strip()
		self.password = loginfile.readline().strip()
		loginfile.close()


	def test_not_logged_in(self):
		self.assertFalse(self.user.login_status)

	def test_login(self):
		self.user.login(self.username,self.password)
		self.assertTrue(self.user.login_status)


