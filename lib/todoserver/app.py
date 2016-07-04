# todoserver/app.PY2
'''
    create 3 dirs--bin lib tests
    create another file(executable) todoserver to kickoff app
    ./bin/todoserver
    
    cd <project-home>
    git mv todoserver.py lib
    set python path variable so the todoserver.py can find the libs it needs
    export PYTHONPATH=$(pwd)/lib
    ./bin/todoserver                                to run server
    python -m unittest tests/todoserver.py            to run tests
        --------
    cd lib
    mkdir todoserver
    git mv todoserver.py todoserver/__init__.py
    cd tests
    python -m unittest tests/todoserver.py            to run tests
    
'''
import json
from flask import (
                   Flask, 
                   make_response, 
                   request,
                    )

from .store import TaskStore 

class TodoServerApp(Flask):
    def __init__(self,name):
        self.store = TaskStore()
        super().__init__(name)

app = TodoServerApp(__name__)
    


@app.route("/tasks/", methods=["Get"])
def get_all_tasks():
    tasks = app.store.get_all_tasks()
            
    return make_response(json.dumps(tasks), 200)

@app.route("/tasks/", methods=["POST"])
def create_task():
    payload = request.get_json(force=True)
    task_id = app.store.create_task(
                    summary=payload["summary"],
                    description= payload["description"],
                                    )
    
#     if payload["summary"] != "Get milk":
#         return make_response("BOOM", 500)
    
    task_info = {"id": task_id}
#     data = {"id": 1}
    return make_response(json.dumps(task_info,201))

@app.route("/tasks/<int:task_id>")
def task_details(task_id):
    task_info = app.store.task_details(task_id)
    
    return json.dumps(task_info)
    

# if (__name__) == "__main__":
#     app.run()
