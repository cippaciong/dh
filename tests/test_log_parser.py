import pytest
import json

from visitors.log_parser import LogParser


@pytest.fixture
def log_entry():
    log = {
        "timestamp": "2020-06-24T15:27:00.123456Z",
        "ip": "83.150.59.250",
        "url": "some/path",
    }
    return json.dumps(log)


class TestLogParser:
    def test_get_ip(self, log_entry):
        log_parser = LogParser()
        assert log_parser.get_ip(log_entry) == "83.150.59.250"
