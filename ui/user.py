from .habitica_api.user import User as APIUser
from .connection import Connection

class User(APIUser):

	def __init__(self,window):
		self.window = window
		self.healthBar = window.healthBar
		self.xpBar = window.xpBar
		self.manaBar = window.manaBar
		super().__init__()
		

	def update_status(self):
		super().update_status()
		self.healthBar.setMaximum(self.maxhp)
		self.healthBar.setValue(self.hp)
		self.xpBar.setMaximum(self.xp_to_level)
		self.xpBar.setValue(self.xp)
		self.manaBar.setMaximum(self.maxmp)
		self.manaBar.setValue(self.mp)
