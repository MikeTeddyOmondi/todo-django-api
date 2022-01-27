# TODO RESTFUL API 

Technology used: 
1. Django - Python web framework
2. MongoDB - Document Database

Getting started: 

#### 1. Running locally

- Clone the git repo; then

- Create a virtual env
```sh
python -m venv env
```

- Install required packages 
```sh
pip install -r requirements.txt
```

- Migrate models to database collections
```sh
python manage.py migrate
```

- Run the development server
```sh
python manage.py runserver 
```

#### 2. Run using Docker

- Using docker-compose commmand

Initially run:
```sh
docker-compose up -d --build
```

Subsequent run: 
```sh
docker-compose up -d 
```

