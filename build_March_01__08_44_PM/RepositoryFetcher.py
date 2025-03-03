import requests
from github import Github, BadCredentialsException

class ICodeRepository:
    def get_readme(self, owner: str, repo_name: str) -> str:
        """Retrieve README content from the specified repository."""
        raise NotImplementedError

class INetworkClient:
    def get(self, url: str, headers: dict = None) -> dict:
        """Make a GET request to the specified URL."""
        raise NotImplementedError

class RepositoryFetcher(ICodeRepository):
    def __init__(self, token: str, network_client: INetworkClient):
        self.token = token
        self.network_client = network_client
        self.github_client = Github(token)

    def get_readme(self, owner: str, repo_name: str) -> str:
        repo = self.github_client.get_repo(f'{owner}/{repo_name}')
        return repo.get_readme().decoded_content.decode('utf-8')

class NetworkClient(INetworkClient):
    def get(self, url: str, headers: dict = None) -> dict:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()