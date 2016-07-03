'''
	to run test,
	python -m unittest test_todoserver.py
'''

import unittest					# can also use doctest, 
import json

from todoserver import app
app.testing = True					# for debugging

def json_body(resp):
	return json.loads(resp.data.decode("utf-8"))			# in python 3 data is of type bytes and therefore need 
															# to decode using json. in python 2 it is string
															# any decode errors are due to string with invalid json syntax

class TestTodoServer(unittest.TestCase):
	def test_get_empty_list_of_tasks(self):
		client=app.test_client()
		resp=client.get("/tasks/")
		self.assertEqual(200, resp.status_code)
		data = json_body(resp)										# in python 3 data is of type bytes and therefore need 
															# to decode using json. in python 2 it is string
															# any decode errors are due to string with invalid json syntax
		self.assertEqual([], data)
		
	def test_create_a_task_and_get_its_details(self):
		client = app.test_client()
		
		# verify test preconditions
		resp=client.get("/tasks/")
		self.assertEqual([], json_body(resp))
	
		# create new task
		new_task_data = {
						"summary": "Get some Nachos",
						"description": "Those really delicious nachos"
						}
		resp = client.post("/tasks/",data=json.dumps(new_task_data))
		self.assertEqual(200,resp.status_code)
		data = json_body(resp)
		
		# get task details by id
		task_id = data["id"]
		resp = client.get("/tasks/{:d}".format(task_id))
		self.assertEqual(200, resp.status_code)
		task = json_body(resp)
		self.assertEqual(task_id, task["id"])
# 		self.assertEqual("Get some Nachos", task["summary"])
# 		self.assertEqual("Those really delicious nachos", task["description"])
		


