'''
	to run test,
	python -m unittest test_todoserver.py
'''

import unittest					# can also use doctest, 
import json

from todoserver import app
app.testing = True	
app.init_db("sqlite:///:memory:")				# for debugging

def json_body(resp):
	return json.loads(resp.data.decode("utf-8"))			# in python 3 data is of type bytes and therefore need 
															# to decode using json. in python 2 it is string
															# any decode errors are due to string with invalid json syntax

class TestTodoServer(unittest.TestCase):
	def setUp(self):
		app.erase_all_test_data()	
										# use the dictionary clear method to clear dic in memory
		self.client = app.test_client()
		# verify test preconditions
		resp=self.client.get("/tasks/")
		self.assertEqual(200, resp.status_code)
		self.assertEqual([], json_body(resp))				# in python 3 data is of type bytes and therefore need 
															# to decode using json. in python 2 it is string
															# any decode errors are due to string with invalid json syntax
		
		
	def test_create_a_task_and_get_its_details(self):
		
		# verify test preconditions
		resp=self.client.get("/tasks/")
		self.assertEqual([], json_body(resp))
	
		# create new task
		new_task_data = {
						"summary": "Get some Nachos",
						"description": "Those really delicious nachos"
						}
		resp = self.client.post("/tasks/",data=json.dumps(new_task_data))
		self.assertEqual(200,resp.status_code)
		data = json_body(resp)
		
		# get task details by id
		task_id = data["id"]
		resp = self.client.get("/tasks/{:d}".format(task_id))
		self.assertEqual(200, resp.status_code)
		task = json_body(resp)
		self.assertEqual(task_id, task["id"])
		self.assertEqual("Get some Nachos", task["summary"])
		self.assertEqual("Those really delicious nachos", task["description"])
		
	def create_multiple_tasks_and_fetch_list(self):
		tasks = [ 
				{"summary": "Get milk",
				 "description": "Get a liter of almond milk"},
				{"summary": "Go to gym",
				 "description": "Get those abs really going"},
				{"summary": "Wash car",
				 "description": "make sure it is shiny and spanking clean"}
				]
		
		for task in tasks:
			with self.subTest(task=task):			# new feature in python 3.4 so for loops can give more detail on sub tests --
													# not sub ported to python 2.x
													# cuts down
				
				resp = self.client.post("/tasks/", data=json.dumps(task))
				self.assertEqual(201, resp.status_code)
		
		# get list of tasks
		resp = self.client.get("/tasks")
		self.assertEqual(200, resp.status_code)
		checked_tasks = json_body(resp)
		self.assertEqual(3, len(checked_tasks))
		
	
		
