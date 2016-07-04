from flask import Flask, make_response, request 
import json

app = Flask(__name__)

MEMORY = {}													# in-memory dict

@app.route("/tasks/", methods=["Get"])
def get_all_tasks():
	tasks = [ {"id": task_id, "summary": task["summary"]}
				for task_id, task in MEMORY.items()]		# in python 2.x use MEMORY.viewitems()--even better than iteritems()
															# viewitems returns an obj that is iterable whereas iteritems returns
															# an iterator, viewitems obsoletes iteritems---always use viewitems
	return make_response(json.dumps(tasks), 200)

@app.route("/tasks/", methods=["POST"])
def create_task():
	payload = request.get_json(force=True)
	try:
		task_id = 1 + max(MEMORY.keys())
	except ValueError:
		task_id = 1
	MEMORY[task_id] = {
						"summary": payload["summary"],
						"description": payload["description"]
						}
# 	if payload["summary"] != "Get milk":
# 		return make_response("BOOM", 500)
	
	task_info = {"id": task_id}
# 	data = {"id": 1}
	return make_response(json.dumps(task_info,201))

@app.route("/tasks/<int:task_id>")
def task_details(task_id):
	task_info = MEMORY[task_id]
	task_info["id"] = task_id
	return json.dumps(task_info)

if (__name__) == "__main__":
	app.run()
