from visitors.log_parser import LogParser
from visitors.visitors_registry import VisitorsRegistry


class VisitorsCounter:
    """Keeps track of the number of visitors."""

    def __init__(self, log_parser=LogParser(), visitors_registry=VisitorsRegistry()):
        self.visitors = 0
        self.log_parser = log_parser
        self.visitors_registry = visitors_registry

    def evaluate(self, log_entry):
        """Evaluates new log entries and increments the visitors counter if
        the visitor's IP is seen for the first time"""
        ip = self.log_parser.get_ip(log_entry)
        if not self.visitors_registry.already_visited(ip):
            self.visitors += 1
