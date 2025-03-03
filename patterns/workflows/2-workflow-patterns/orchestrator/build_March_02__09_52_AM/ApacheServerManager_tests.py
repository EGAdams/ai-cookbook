import unittest
from unittest.mock import patch, mock_open

class TestApacheServerManager(unittest.TestCase):
    @patch('subprocess.run')
    def test_start_server(self, mock_run):
        manager = ApacheServerManager()
        manager.start_server()
        mock_run.assert_called_once_with(['apachectl', 'start'], check=True)

    @patch('subprocess.run')
    def test_stop_server(self, mock_run):
        manager = ApacheServerManager()
        manager.stop_server()
        mock_run.assert_called_once_with(['apachectl', 'stop'], check=True)

    @patch('subprocess.run')
    def test_check_status(self, mock_run):
        mock_run.return_value.stdout = 'Apache is running'
        manager = ApacheServerManager()
        manager.check_status()
        mock_run.assert_called_once_with(['apachectl', 'status'], check=True, capture_output=True, text=True)

    @patch('builtins.open', new_callable=mock_open, read_data='Error message\nAnother error')
    @patch('os.path.exists', return_value=True)
    def test_retrieve_error_logs(self, mock_exists, mock_open):
        manager = ApacheServerManager()
        with patch('builtins.print') as mock_print:
            manager.retrieve_error_logs('/var/log/apache2/error.log')
            mock_print.assert_called_once_with('Error message\nAnother error')

    @patch('os.path.exists', return_value=False)
    def test_retrieve_error_logs_non_existent(self, mock_exists):
        manager = ApacheServerManager()
        with patch('builtins.print') as mock_print:
            manager.retrieve_error_logs('/var/log/apache2/error.log')
            mock_print.assert_called_once_with('Log file does not exist: /var/log/apache2/error.log')


if __name__ == '__main__':
    unittest.main()