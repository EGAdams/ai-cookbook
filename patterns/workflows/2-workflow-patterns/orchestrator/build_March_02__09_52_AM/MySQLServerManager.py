import os
import subprocess

class BaseServerManager:
    def start_server(self):
        raise NotImplementedError

    def stop_server(self):
        raise NotImplementedError

    def check_status(self):
        raise NotImplementedError

    def retrieve_error_logs(self):
        raise NotImplementedError

class MySQLServerManager(BaseServerManager):
    def __init__(self, mysql_service_name):
        self.mysql_service_name = mysql_service_name

    def start_server(self):
        result = subprocess.run(['systemctl', 'start', self.mysql_service_name], check=False)
        return result.returncode == 0

    def stop_server(self):
        result = subprocess.run(['systemctl', 'stop', self.mysql_service_name], check=False)
        return result.returncode == 0

    def check_status(self):
        result = subprocess.run(['systemctl', 'status', self.mysql_service_name], capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else None

    def retrieve_error_logs(self):
        log_path = '/var/log/mysql/error.log'  # Default MySQL error log path
        if os.path.exists(log_path):
            with open(log_path, 'r') as log_file:
                return log_file.read()
        return 'Log file does not exist.'
    
    def clear_logs(self):
        log_path = '/var/log/mysql/error.log'  # Default MySQL error log path
        try:
            if os.path.exists(log_path):
                with open(log_path, 'w') as log_file:
                    log_file.truncate(0)
                return True
        except Exception as e:
            print(f"Error clearing logs: {e}")
        return False