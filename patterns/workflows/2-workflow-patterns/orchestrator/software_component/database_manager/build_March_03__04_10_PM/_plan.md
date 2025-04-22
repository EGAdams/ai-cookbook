
Analyze the following software requirements and design a component structure.

Requirements: Design and implement a MySQL Database Manager system that allows users to create, delete, search, and modify database records interactively through a menu. The system should provide options such as:
1. Create a record
2. Delete records based on a given criterion
3. Modify records based on a given criterion
4. Search for records

The system should generate output in Markdown format and save it to a file named 'output.md'. The table should be formatted with:
- A **dark gray background with white text** for the headers.
- **Light gray rows with black text** for readability.
- A **thin white border** separating columns and enclosing the table.
Use **HTML and CSS within Markdown** to achieve this formatting.
Design Constraints: The system should adhere to SOLID principles, ensuring future extensibility. It should be implemented in Python and support Linux-based MySQL servers. Utilize appropriate Python libraries such as `mysql-connector-python` for database operations. Ensure robust error handling and user input validation. Provide unit tests for verifying database operations and file output correctness.

Return your response in this format:

# System Overview
The MySQL Database Manager is a command-line based application that allows users to interact with a MySQL database through a simple menu-driven interface. Users can create, delete, modify, and search for records in the database. The output of the operations is formatted in Markdown and saved to a file called 'output.md', ensuring that the data is easily readable and well-structured. The system is built with a focus on using SOLID principles to ensure maintainability and future extensibility, and it provides robust error handling and input validation to enhance user experience.

# Design Patterns
MVC (Model-View-Controller)
- Factory Pattern for record creation
- Singleton Pattern for database connection management
- Command Pattern for user actions

# Modules

## DatabaseManager
- Functionality: Handles all database operations, including connect, disconnect, create, delete, modify, and search records.
- Interfaces: IDatabaseConnection, IRecordOperation
- Dependencies: mysql-connector-python


## UserInterface
- Functionality: Provides a command-line interface for users to interact with the database manager through a menu.
- Interfaces: IMenuDisplay, IUserInput
- Dependencies: 


## MarkdownFormatter
- Functionality: Formats output data in Markdown with the specified style, including generating the table structure.
- Interfaces: IMarkdownOutput
- Dependencies: 


## ErrorHandler
- Functionality: Handles error logging and user feedback for any exceptions in the database operations or user inputs.
- Interfaces: IErrorLogging
- Dependencies: 

