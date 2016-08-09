import requests
import json

JSON_HEADERS = {'content-type': 'application/json'}
BASE_URL = "https://habitica.com/api/v3/"

class Connection():

	def __init__(self):
		self.headers = JSON_HEADERS.copy()
		self.login_status = False
		
	def post(self,url,data=None):
		if data is not None:
			r = requests.post(BASE_URL+url, headers=self.headers, data=json.dumps(data))
		else:
			r = requests.post(BASE_URL+url, headers=self.headers)
		return r.json()

	def get(self,url,params=None):
		if params is not None:
			r = requests.get(BASE_URL+url, headers=self.headers,params=params)
		else:
			r = requests.get(BASE_URL+url, headers=self.headers)
		return r.json()

	def delete(self,url):
		r = requests.delete(BASE_URL+url,headers=self.headers)
		return r.json()

	def put(self,url,data):
		r = requests.put(BASE_URL+url, headers=self.headers, data=json.dumps(data))
		return r.json()


	def login(self,username,password):
		credentials = {'username': username, 'password': password}
		r = self.post('user/auth/local/login',credentials)
		if r['success']:
			self.headers['x-api-user'] = r['data']['id']
			self.headers['x-api-key'] = r['data']['apiToken']
			self.login_status = True

	def get_status(self):
		r = self.get('user')
		if r['success']:
			return r['data']
		else:
			return None

	def add_task(self,data):
		r = self.post('tasks/user',data)
		return r['success']

	def get_tasks(self,task_type=None):
		if task_type:
			r = self.get('tasks/user',params={'type':task_type})
		else:
			r = self.get('tasks/user')
		if r['success']:
			return r['data']
		else:
			return None

	def delete_task(self,id):
		request_url = 'tasks/%s' % (id)
		r = self.delete(request_url)
		return r['success']

	def modify_task(self,id,data):
		request_url = 'tasks/%s' % (id)
		r = self.put(request_url,data)
		return r['success']

	def add_to_checklist(self,id,data):
		request_url = 'tasks/%s/checklist' % (id)
		r = self.post(request_url,data)
		return r['success']

	def delete_from_checklist(self,id,checklist_item_id):
		request_url = 'tasks/%s/checklist/%s' % (id,checklist_item_id)
		r = self.delete(request_url)
		return r['success']

	def edit_checklist(self,id,checklist_item_id,data):
		request_url = 'tasks/%s/checklist/%s' % (id,checklist_item_id)
		r = self.put(request_url,data)
		return r['success']

	def score_task(self,id,direction='up'):
		request_url = 'tasks/%s/score/%s' % (id,direction)
		r = self.post(request_url)
		return r['success']

	def get_task(self,id):
		request_url = 'tasks/%s' % (id)
		r = self.get(request_url)
		if r['success']:
			return r['data']
		else:
			return None