
tests:
	pytest -v .

lint:
	pylint ./app	

migrate:
	python3 -m app.services.migrate up

docker-build:
	docker build --rm -t fastapi-proj .

docker-run:
	docker run --rm -it -p 8000:8000 --name fastapi fastapi-proj

freeze:
	pip3 freeze > requirements.txt

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

run-dev:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
