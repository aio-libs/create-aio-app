
bandit:
	bandit -r ./create_aio_app -x create_aio_app/template

checkrst:
	python setup.py check --restructuredtext

pyroma:
	pyroma -d .

flake: checkrst bandit pyroma
	flake8 create_aio_app setup.py --exclude create_aio_app/template

test:
	rm -rf project_new/
	pip install .
	create-aio-app project_new
	doc8 project_new/docs/
	cd project_new/ && docker-compose up test  && docker-compose stop

ci: flake test

.PHONY: all flake test vtest cov clean doc ci
