class ServiceMonitor:
    def __init__(self, service_name, port):
        """Initialises the monitor for a specific service.

        Args:
            service_name (str): the name of the service.
            port (int): the port to use for checks.
        """

        print(f"Initializing monitor for service {service_name} on port {port}.")
        self.service = service_name
        self.port = port
        self.is_alive = False

    def check(self):
        """Simulates checking the service status"""
        print(f"METHOD: Checking {self.service} on port {self.port}...")

        self.is_alive = True

        print(f"METHOD: Status for service {self.service}: {"Alive" if self.is_alive else "Down"}")

        return self.is_alive


class HttpServiceMonitor(ServiceMonitor):
    """Extends ServiceMonitor to add an HTTP endpoint check."""
    def __init__(self, service_name, port, url):
        super().__init__(service_name, port)
        self.url = url

    def ping(self):
        """Ping url provided when creating instance."""
        print(f"METHOD: Pinging url {self.url}")

    def check(self):
        alive = super().check()
        print(f"METHOD: Performing HTTP check on {self.url}")

if __name__ == "__main__":
    nginx_monitor = ServiceMonitor("nginx", 80)
    print(isinstance(nginx_monitor, ServiceMonitor))

    status = nginx_monitor.check()
    print(f"Recieved status: {status}")

    http_monitor = HttpServiceMonitor("web", 8080, "http://localhost")
    http_monitor.check()
    http_monitor.ping()
