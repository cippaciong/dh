import pytest

from visitors.visitors_registry import VisitorsRegistry


@pytest.fixture
def valid_ip():
    return "1.1.1.1"


@pytest.fixture
def invalid_ip():
    return "0.0.0.0"


class TestVisitorsRegistry:
    def test_empty_ips(self):
        visitors_registry = VisitorsRegistry()
        assert visitors_registry.already_visited(valid_ip) == False
        assert visitors_registry.already_visited(valid_ip) == True
