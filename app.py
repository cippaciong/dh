import json

from flask import Flask, request
from visitors.visitors_counter import VisitorsCounter

app = Flask(__name__)

counter = VisitorsCounter()


@app.route("/")
def home():
    return "<p>Use either GET /visitors or POST /logs</p>"


@app.route("/visitors")
def get_visitors():
    return json.dumps({"visitors": counter.visitors})


@app.route("/logs", methods=['POST'])
def post_logs():
    if request.is_json:
        log_entry = request.json
        counter.evaluate(json.dumps(log_entry))
        return json.dumps({"accepted": True})
    return json.dumps({"error": "not a valid json or didn't use application/json"})
