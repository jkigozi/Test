# Test

'''
	create 3 dirs--bin lib tests
	create another file(executable) todoserver to kickoff app
	./bin/todoserver
	
	cd <project-home>
	git mv todoserver.py lib
	set python path variable so the todoserver.py can find the libs it needs
	export PYTHONPATH=$(pwd)/lib
	./bin/todoserver								to run server
	python -m unittest tests/todoserver.py			to run tests
		--------
	cd lib
	mkdir todoserver
	git mv todoserver.py todoserver/__init__.py
	cd tests
	python -m unittest tests/todoserver.py			to run tests
	python -m unittest tests.todoserver.py			to run tests
	python -m unittest tests.test_todoserver.TestTodoServer.test_create_a_task_and_get_its_details   to run a method in test suite
		--------
	pip install sqlalchemy
	git diff requirements.txt	
'''
