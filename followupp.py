import requests, json

class Followupp:

	def __init__(self):
		self.api = 'http://www.followupp.co/api/messages'
		self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

	def request(self, data):
		return requests.post(self.api, data=json.dumps(data), headers=self.headers)

