class VisitorsRegistry:
    """This class holds a registry of all the visitors' IPs encontered so far
    The IPs registry is implemented using a dictionary to have a quick read access"""

    def __init__(self, ips={}):
        self.ips = ips

    def already_visited(self, ip):
        """Returns True if the IP passed as argument is already present in the IPs
        registry. Otherwise adds the IP to the registry and returns False."""
        visited = self.ips.get(ip, False)
        if not visited:
            self.ips[ip] = True
        return visited
