import pytest

from visitors.visitors_registry import VisitorsRegistry


@pytest.fixture
def new_visitor():
    return "1.1.1.1"


@pytest.fixture
def existing_visitor():
    return "0.0.0.0"


class TestVisitorsRegistry:
    def test_empty_ips(self):
        visitors_registry = VisitorsRegistry()
        assert visitors_registry.already_visited(new_visitor) == False
        assert visitors_registry.already_visited(new_visitor) == True

    def test_existing_visitor(self):
        visitors_registry = VisitorsRegistry({existing_visitor: True})
        assert visitors_registry.already_visited(existing_visitor) == True
