import unittest
from unittest.mock import Mock
from repository_fetcher import RepositoryFetcher, NetworkClient

class TestRepositoryFetcher(unittest.TestCase):
    def setUp(self):
        # Assuming your GitHub token is 'your_token_here'
        self.token = 'your_token_here'
        self.mock_network_client = Mock(spec=NetworkClient)
        self.fetcher = RepositoryFetcher(self.token, self.mock_network_client)

    def test_get_readme_success(self):
        self.mock_network_client.get = Mock(return_value='Sample README content')
        result = self.fetcher.get_readme('owner', 'repo_name')
        self.assertEqual(result, 'Sample README content')

    def test_get_readme_no_repo(self):
        with self.assertRaises(BadCredentialsException):
            self.fetcher.get_readme('invalid_owner', 'invalid_repo')

if __name__ == '__main__':
    unittest.main()