'''
	to run test,
	python -m unittest test_todoserver.py
'''

import unittest					# can also use doctest, 
import json

from todoserver import app


class TestTodoServer(unittest.TestCase):
	def test_get_empty_list_of_tasks(self):
		client=app.test_client()
		resp=client.get("/tasks/")
		self.assertEqual(200, resp.status_code)
		data=json.loads(resp.data.decode("utf-8"))			# in python 3 data is of type bytes and therefore need 
															# to decode using json. in python 2 it is string
															# any decode errors are due to string with invalid json syntax
		self.assertEqual([], data)
		



