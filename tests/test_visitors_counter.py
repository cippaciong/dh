import pytest
import json

from visitors.visitors_counter import VisitorsCounter


@pytest.fixture
def existing_visitor():
    return "0.0.0.0"


@pytest.fixture
def log_entry():
    log = {
        "timestamp": "2020-06-24T15:27:00.123456Z",
        "ip": "83.150.59.250",
        "url": "some/path",
    }
    return json.dumps(log)


class TestVisitorsCounter:
    def test_new_visitor(self, log_entry):
        visitors_counter = VisitorsCounter()
        assert visitors_counter.visitors == 0
        visitors_counter.evaluate(log_entry)
        assert visitors_counter.visitors == 1
        visitors_counter.evaluate(log_entry)
        assert visitors_counter.visitors == 1
