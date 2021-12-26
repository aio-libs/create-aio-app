
bandit:
	bandit -r ./create_aio_app -x create_aio_app/template -s B101

checkrst:
	python -m pep517.build . && python -m twine check dist/*

pyroma:
	echo 'import setuptools; setuptools.setup()' > setup.py
	pyroma -d .
	rm setup.py

flake: checkrst bandit pyroma
	flake8 create_aio_app --exclude create_aio_app/template

test:
	rm -rf project_new/
	pip install -e .
	create-aio-app project_new
	doc8 project_new/docs/
	cd project_new/ && make lint && make mypy && docker-compose up test && docker-compose stop

ci: flake test

.PHONY: all flake test vtest cov clean doc ci
