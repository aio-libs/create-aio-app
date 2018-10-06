
bandit:
	bandit -r ./create_aio_app -x create_aio_app/template

checkrst:
	python setup.py check --restructuredtext

pyroma:
	pyroma -d .

flake: checkrst bandit
	flake8 create_aio_app setup.py --exclude create_aio_app/template

test:
	rm -rf project_new/
	pip install .
	create-aio-app project_new
	cd project_new/ && docker-compose up project_new_app

ci: flake test

.PHONY: all flake test vtest cov clean doc ci
