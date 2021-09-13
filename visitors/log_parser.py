import json


class LogParser:
    """Parses log entries and extracts data from them"""

    def get_ip(self, log_entry):
        """Extract the ip address from a log entry"""
        log = json.loads(log_entry)
        return log.get("ip")

