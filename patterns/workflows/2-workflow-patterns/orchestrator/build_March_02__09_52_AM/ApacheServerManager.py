import os
import subprocess

class BaseServerManager:
    def start_server(self):
        raise NotImplementedError("This method should be overridden.")
    
    def stop_server(self):
        raise NotImplementedError("This method should be overridden.")
    
    def check_status(self):
        raise NotImplementedError("This method should be overridden.")
    
    def retrieve_error_logs(self):
        raise NotImplementedError("This method should be overridden.")


class ApacheServerManager(BaseServerManager):
    def start_server(self):
        try:
            subprocess.run(['apachectl', 'start'], check=True)
            print("Apache server started successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error starting Apache server: {e}")

    def stop_server(self):
        try:
            subprocess.run(['apachectl', 'stop'], check=True)
            print("Apache server stopped successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error stopping Apache server: {e}")

    def check_status(self):
        try:
            result = subprocess.run(['apachectl', 'status'], check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error checking Apache server status: {e}")

    def retrieve_error_logs(self, log_path='/var/log/apache2/error.log'):
        if os.path.exists(log_path):
            with open(log_path, 'r') as log_file:
                logs = log_file.read()
                print(logs)
        else:
            print(f"Log file does not exist: {log_path}")

    def clear_logs(self, log_path='/var/log/apache2/error.log'):
        try:
            if os.path.exists(log_path):
                with open(log_path, 'w') as log_file:
                    log_file.truncate(0)
                return True
        except Exception as e:
            print(f"Error clearing logs: {e}")
        return False
