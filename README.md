# Weather API
Small API telling temperature and weather description in location of your choice using FastAPI.

### Requirements
To install required packages use:
```
pip install -r requirements.txt
```

### Running the API
To run the API go to the **app** directory and use: 
```
uvicorn main:app --reload
```
It should run on [localhost](http://localhost).

### Running using docker-compose
To build and run docker-compose containers use: 
```
docker-compose build
docker-compose up
```
It should run on [localhost:8000](http://localhost:8000).

### Additional features
This API implements creating of PostgreSQL database for storing usage history with the help of SQLAlchemy. You can test this feature in [Swagger UI](http://localhost/docs#/default/create_history_history_add_post "Swagger UI") and see the full database in [localhost/history](http://localhost/history "localhost/history").
There is also a simple HTTP authentication. You can test it by clicking a link on an index page.