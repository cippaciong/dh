import json
import logging

from pydantic import BaseModel
from fastapi import FastAPI

from visitors.visitors_counter import VisitorsCounter


logging.basicConfig(level=logging.INFO)

app = FastAPI()
counter = VisitorsCounter()


class LogEntry(BaseModel):
    timestamp: str
    ip: str
    url: str

    def __str__(self):
        return json.dumps({"timestamp": self.timestamp, "ip": self.ip, "url": self.url})


@app.get("/")
async def home():
    return "<p>Use either GET /visitors or POST /logs</p>"


@app.get("/visitors")
async def get_visitors():
    return {"visitors": counter.visitors}


@app.post("/logs")
async def post_logs(log_entry: LogEntry):
    counter.evaluate(str(log_entry))
    return {"accepted": True}
