import logging
import threading
from visitors.log_parser import LogParser
from visitors.visitors_registry import VisitorsRegistry


threadLock = threading.Lock()


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
        logging.debug(f"Recevied log entry for IP: {ip}")
        if not self.visitors_registry.already_visited(ip):
            with threadLock:
                self.visitors += 1
                logging.debug(f"Current number of unique visitors: {self.visitors}")
        else:
            logging.debug(f"IP address '{ip}' is already present in the visitors registry")
