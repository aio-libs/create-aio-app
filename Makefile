test:
	rm -rf some-new/
	pip install .
	create-aio-ms some-new --redis
