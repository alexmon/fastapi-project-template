## Project initialization
```bash
$ pip3 install virtualenv
$ easy_install-3.7 virtualenv
$ virtualenv -p python3 env
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install fastapi
$ pip3 install uvicorn
$ pip3 install email-validator
$ pip3 install python-dotenv
$ pip3 install pytest
$ pip3 install SQLAlchemy
$ pip3 install databases[postgresql]
$ pip3 install python-multipart
$ pip3 freeze > requirements.txt
```

## Requirements
- Python3
- pip3
- makefile

## Build / Test / Run
```bash

$ make test

$ make migrate

$ make docker-build

$ make docker-run

$ make freeze

$ make run

$ make run-dev

```