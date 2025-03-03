
Analyze the following software requirements and design a component structure.

Requirements: Retrieve the README.md file from the specified GitHub repository and analyze the installation and build instructions.Follow the documented steps to set up the development environment and build the project.
Design Constraints: Ensure compatibility with the listed dependencies and required frameworks. Provide any missing setup instructions if necessary and verify that all build steps are executed correctly.

Return your response in this format:

# System Overview
The system is designed to automate the retrieval and analysis of the README.md file from a specified GitHub repository, focusing on installation and build instructions. By following the retrieved instructions, the system sets up the development environment and builds the project while ensuring compatibility with the mentioned dependencies and frameworks.

# Design Patterns
Singleton Pattern
- Strategy Pattern
- Facade Pattern

# Modules

## RepositoryFetcher
- Functionality: Responsible for retrieving the README.md file from the specified GitHub repository using the GitHub API.
- Interfaces: ICodeRepository, INetworkClient
- Dependencies: requests, PyGithub


## InstructionAnalyzer
- Functionality: Analyzes the content of the README.md file to extract installation and build instructions.
- Interfaces: ITextParser
- Dependencies: markdown2, re


## EnvironmentSetup
- Functionality: Handles the setup of the development environment following the instructions analyzed from the README.md file.
- Interfaces: ISetupInstructions
- Dependencies: virtualenv, pip


## BuildExecutor
- Functionality: Executes the build steps derived from the README.md analysis and verifies successful execution.
- Interfaces: IBuildProcess
- Dependencies: make, cmake


## DependencyChecker
- Functionality: Checks the current development environment for compatibility with the listed dependencies and required frameworks, providing any missing setup instructions if necessary.
- Interfaces: IDependencyManager
- Dependencies: pip

