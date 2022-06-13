#Weather API
Small API telling temperature and weather description in city of your choice using FastAPI.

[TOC]

###Requirements
To install required packages use:
```
pip install -r requirements.txt
```

###Running the API
To run the API go to the **app** directory and use: 
```
uvicorn main:app --reload
```
It should run on [localhost](http://localhost).

###Building a docker image
To build a docker image use: 
```
docker build -t weatherapp .
docker run -d --name weathercontainer -p 80:80 weatherapp
```

###Database for usage history
This API implements creating of SQLite database for storing usage history with the help of SQLAlchemy. There is no front-end support for this, however you can test this feature in [Swagger UI](http://localhost/docs#/default/create_history_history_add_post "Swagger UI") and see the full database in [localhost/history](http://localhost/history "localhost/history")