# Visitors Counter
The following project provides an API to evaluate log lines with the following structure
```json
{ "timestamp": "2020-06-24T15:27:00.123456Z", "ip": "83.150.59.250", "url": "some/path" }
```
and keep track of the total number of unique visitors.

The API exposes two endpoints:
* `POST /logs` to receive log entries as JSON
* `GET /visitors` to get the current number of unique visitors

## Install
To get started using this repository you should first clone it
```shell
git clone https://github.com/cippaciong/dh.git && cd dh
```
Then create a virtualenv where you will install all the required dependencies
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
After you have installed the dependencies and activated the virtualenv, you can
run the Flask app
```shell
export FLASK_APP=app
flask run
```
The app will be available on `http://127.0.0.1:5000/`

You can now send new log entries to the API with
```shell
curl --header "Content-Type: application/json" \
     -X POST http://127.0.0.1:5000/logs \
     --data '{ "timestamp": "2020-06-24T15:27:00.123456Z", "ip": "83.150.59.251", "url": "some/path" }'
```
or get the total number of unique visitors with
```shell
curl http://127.0.0.1:5000/visitors
```

## Run tests
To run tests, make sure you have activated the virtualenv
```shell
source .venv/bin/activate
```
and then run
```
python -m pytest
```
