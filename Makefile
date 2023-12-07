venv:
	python3 -m venv myenv
		source myenv/bin/activate

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:	
	black *.py 

lint:
	ruff check *.py 

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	az webapp up --sku F1 --name TellMeMyProfession --location eastus
		
all: install lint test format deploy