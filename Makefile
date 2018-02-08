lint:
	pycodestyle audio_recorder
	pycodestyle setup.py
	pycodestyle test_project/test_project
	pycodestyle test_project/audio_files --exclude migrations

test:
	py.test test_project/audio_files/tests.py

serve:
	python test_project/manage.py runserver
