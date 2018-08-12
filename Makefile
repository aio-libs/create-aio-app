test:
	rm -rf some_new/
	pip install .
	create-aio-ms some_new --redis
	cd some_new/ && pip install -e . && make run
