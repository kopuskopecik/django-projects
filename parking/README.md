# Django Backend Take Home Project

Parking, Unparking, getting parking info and rate limit for requests

## Installation

create virtual enviroment

```bash
python -m venv myvenv
```
activate myvenv for windows

```bash
myvenv\Scripts\activate
```

activate myvenv for Linux

```bash
$ source venv/bin/activate
```

upgrate pip

```bash
python -m pip install --upgrade pip
```

install django

```bash
pip install django
```

## Usage

```bash
python manage.py makemigrations
python manage.py migrate 
```

create parking slots and .env file like below this. 20 is number of parking slots. You can change whenever you want.

```bash  
python manage.py create_slot 20
```

## Note

You can test all URLs and overflow below [localhost](http://127.0.0.1:8000/) webpage.

## Settings
In the setting file you can change OVERFLOW_REQUEST_NUMBER and OVERFLOW_REQUEST_TIME.
Both default values are 10. 


```bash
python manage.py makemigrations
python manage.py migrate 
```

create parking slots and .env file like below this. 20 is number of parking slots. You can change whenever you want.

```bash  
python manage.py create_slot 20
```

and runserver

```bash  
python manage.py runserver
```

## Note

On the below address You can test Url actions and owerflow for requests.

[localhost](http://127.0.0.1:8000/)

## Explanations

session(Limit) to see requests of a spesific IP_adress and prevent overflow requests.
A custom django command(create_slot) to create number of parking slots and .env file.
A custom decorator(rate_limit) for the views to prevent duplicate.
A templatetag(random_int) to obtain a random value for cars.
