import unittest
from unittest.mock import patch, MagicMock

class TestMySQLServerManager(unittest.TestCase):
    def setUp(self):
        self.manager = MySQLServerManager('mysql')

    @patch('subprocess.run')
    def test_start_server_success(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)
        result = self.manager.start_server()
        self.assertTrue(result)
        mock_run.assert_called_once_with(['systemctl', 'start', 'mysql'], check=False)

    @patch('subprocess.run')
    def test_stop_server_success(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)
        result = self.manager.stop_server()
        self.assertTrue(result)
        mock_run.assert_called_once_with(['systemctl', 'stop', 'mysql'], check=False)

    @patch('subprocess.run')
    def test_check_status(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout='Active: active (running)')
        status = self.manager.check_status()
        self.assertEqual(status, 'Active: active (running)')

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='Error Log Content')
    def test_retrieve_error_logs(self, mock_open, mock_exists):
        logs = self.manager.retrieve_error_logs()
        self.assertEqual(logs, 'Error Log Content')
        mock_open.assert_called_once_with('/var/log/mysql/error.log', 'r')

    @patch('os.path.exists', return_value=False)
    def test_retrieve_error_logs_file_not_exist(self, mock_exists):
        logs = self.manager.retrieve_error_logs()
        self.assertEqual(logs, 'Log file does not exist.')

if __name__ == '__main__':
    unittest.main()