# Rocket.Chat Rest API Web Application

The Basic local chat web application using rocketchat_API of Pyhton. This application has ability to send messages from channels and also direct messages.

## Installation

Firstly please follow instructions on [this link](https://docs.rocket.chat/guides/developer/quick-start) to create server locally for Linux. 

For Windows 10 [this link](https://docs.rocket.chat/guides/developer/developing-on-windows-10)

Please start server and then login the system and record your credentials. Because we use them in Python side.

```bash
git clone https://github.com/kopuskopecik/rocket.git
```

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

Installing Python requirements(django, requests, rocketchat_API)

```bash
pip install -r requirements.txt
```

create channels, users and messages otomatically

```bash
python manage.py create_channels
```


## Usage

To login RocketServer set your credentials in rocket/settings.py  like below. I ignore security but If you want you can use python-decouple.

```python
PROXY_DICT = {
        "http"  : "http://127.0.0.1:3000",
        "https" : "https://127.0.0.1:3000",
    }

ROCKET_USERNAME = "sahinturk"
ROCKET_PASSWORD = "Aa123456"
SERVER_URL = "http://127.0.0.1:3000/"

```

and then run Django server

```bash
python manage.py runserver
```