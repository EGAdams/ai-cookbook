# RepositoryFetcher Module

## Overview
The `RepositoryFetcher` module is designed to retrieve the `README.md` file from a specified GitHub repository using the GitHub API.

## Interfaces
- **ICodeRepository**: An interface that defines a method to retrieve README content from a GitHub repository.
- **INetworkClient**: An interface that defines a method for making GET requests.

## Class: RepositoryFetcher
### Constructor
```python
__init__(self, token: str, network_client: INetworkClient)
```
- **token**: Authorization token for accessing the GitHub API.
- **network_client**: An instance of a class implementing the `INetworkClient` interface.

### Methods
- #### get_readme(owner: str, repo_name: str) -> str
    Retrieve the content of the `README.md` file from the specified GitHub repository.
    - **Parameters:**
        - `owner`: The username of the repository owner.
        - `repo_name`: The name of the repository.
    - **Returns:** The decoded content of the `README.md` as a string.
    - **Raises:** BadCredentialsException for invalid token or if repository doesn't exist.

## Usage
```python
fetcher = RepositoryFetcher('your_token_here', NetworkClient())
readme_content = fetcher.get_readme('owner', 'repo_name')
print(readme_content)
```