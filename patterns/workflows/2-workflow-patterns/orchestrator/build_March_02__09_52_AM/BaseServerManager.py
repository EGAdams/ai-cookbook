import os
import subprocess

class BaseServerManager:
    """
    Abstract class that defines the interface for server management operations.
    """
    def start_server(self):
        """Starts the server. To be implemented by subclasses."""
        raise NotImplementedError("start_server() must be implemented by subclasses")

    def stop_server(self):
        """Stops the server. To be implemented by subclasses."""
        raise NotImplementedError("stop_server() must be implemented by subclasses")

    def check_status(self):
        """Checks the status of the server. To be implemented by subclasses."""
        raise NotImplementedError("check_status() must be implemented by subclasses")

    def retrieve_error_logs(self):
        """Retrieves error logs of the server. To be implemented by subclasses."""
        raise NotImplementedError("retrieve_error_logs() must be implemented by subclasses")


# Example Implementation of a Concrete Class
class SimpleServerManager(BaseServerManager):
    def start_server(self):
        print("Starting server...")
        subprocess.run(["systemctl", "start", "myserver"], check=True)

    def stop_server(self):
        print("Stopping server...")
        subprocess.run(["systemctl", "stop", "myserver"], check=True)

    def check_status(self):
        print("Checking server status...")
        result = subprocess.run(["systemctl", "status", "myserver"], capture_output=True, text=True)
        return result.stdout

    def retrieve_error_logs(self):
        print("Retrieving error logs...")
        result = subprocess.run(["journalctl", "-u", "myserver"], capture_output=True, text=True)
        return result.stdout