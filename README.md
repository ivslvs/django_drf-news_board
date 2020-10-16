## Application description

This application is written in Python using Django REST framework.

It's a list of news with functionality to upvote and comment on them. 

Using Celery for reset post upvotes once a day.

- Python 3.8
- Django REST Framework
- PostgreSQL
- Celery
- Docker



## Quick start

```sh
docker-compose build
docker-compose run web python manage.py migrate
docker-compose up

docker-compose down
```

## API Documentation

[Detailed API documentation](https://documenter.getpostman.com/view/8690633/TVKHUvFT) generated by Postman
