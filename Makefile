test:
	rm -rf project_new/
	pip install .
	create-aio-app project_new
	cd project_new/ && docker-compose up project_new_app
