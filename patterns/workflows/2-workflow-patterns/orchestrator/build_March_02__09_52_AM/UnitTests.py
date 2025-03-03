import unittest
from MySQLServerManager import MySQLServerManager
from ApacheServerManager import ApacheServerManager

class TestServerManagers(unittest.TestCase):
    def setUp(self):
        self.mysql_manager = MySQLServerManager( 'mysql' )
        self.apache_manager = ApacheServerManager()

    def test_start_server(self):
        mysql_started = self.mysql_manager.start()
        apache_started = self.apache_manager.start()
        self.assertTrue(mysql_started, "MySQL server should start successfully.")
        self.assertTrue(apache_started, "Apache server should start successfully.")

    def test_stop_server(self):
        mysql_stopped = self.mysql_manager.stop()
        apache_stopped = self.apache_manager.stop()
        self.assertTrue(mysql_stopped, "MySQL server should stop successfully.")
        self.assertTrue(apache_stopped, "Apache server should stop successfully.")

    def test_check_status(self):
        mysql_status = self.mysql_manager.check_status()
        apache_status = self.apache_manager.check_status()
        self.assertIn(mysql_status, ["running", "stopped"], "MySQL server status should be valid.")
        self.assertIn(apache_status, ["running", "stopped"], "Apache server status should be valid.")

    def test_retrieve_error_logs(self):
        mysql_logs = self.mysql_manager.retrieve_error_logs()
        apache_logs = self.apache_manager.retrieve_error_logs()
        self.assertIsInstance(mysql_logs, list, "MySQL error logs should be a list.")
        self.assertIsInstance(apache_logs, list, "Apache error logs should be a list.")

if __name__ == '__main__':
    unittest.main()