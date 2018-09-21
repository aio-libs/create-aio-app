test:
	rm -rf some_new/
	pip install .
	create-aio-ms some_new
	cd some_new/ && docker-compose up some_new_app
