import unittest
from unittest.mock import patch, MagicMock

class TestBaseServerManager(unittest.TestCase):
    def setUp(self):
        self.server_manager = SimpleServerManager()

    @patch('subprocess.run')
    def test_start_server(self, mock_run):
        self.server_manager.start_server()
        mock_run.assert_called_once_with(["systemctl", "start", "myserver"], check=True)

    @patch('subprocess.run')
    def test_stop_server(self, mock_run):
        self.server_manager.stop_server()
        mock_run.assert_called_once_with(["systemctl", "stop", "myserver"], check=True)

    @patch('subprocess.run')
    def test_check_status(self, mock_run):
        mock_run.return_value.stdout = 'active (running)'
        status = self.server_manager.check_status()
        self.assertEqual(status, 'active (running)')
        mock_run.assert_called_once_with(["systemctl", "status", "myserver"], capture_output=True, text=True)

    @patch('subprocess.run')
    def test_retrieve_error_logs(self, mock_run):
        mock_run.return_value.stdout = 'Error log details'
        logs = self.server_manager.retrieve_error_logs()
        self.assertEqual(logs, 'Error log details')
        mock_run.assert_called_once_with(["journalctl", "-u", "myserver"], capture_output=True, text=True)

if __name__ == '__main__':
    unittest.main()