# UserInterface Module

## Overview
The `UserInterface` module provides a command-line interface that allows users to interact with a database manager. Users can perform various actions such as adding, updating, deleting, and viewing records.

## Interfaces
This module implements the following interfaces:
- `IMenuDisplay`: Responsible for displaying menus and messages to the user.
- `IUserInput`: Responsible for getting user input based on prompts.

## Classes
- `ConsoleMenuDisplay`: Implements the `IMenuDisplay` interface and displays the main menu and messages to the user in the console.
- `ConsoleUserInput`: Implements the `IUserInput` interface for getting input from the user via the console.
- `UserInterface`: The main class that ties together the menu display and user input to create a command-line interface.

## Usage
1. Create instances of `ConsoleMenuDisplay` and `ConsoleUserInput`.
2. Instantiate the `UserInterface` with the created menu display and user input instances.
3. Call the `run` method of `UserInterface` to start the interaction.

## Example
```python
if __name__ == '__main__':
    menu_display = ConsoleMenuDisplay()
    user_input = ConsoleUserInput()
    ui = UserInterface(menu_display, user_input)
    ui.run()
```

## Testing
The module includes unit tests for its components using the `unittest` framework. Tests verify that the menu is displayed and handle both valid and invalid user inputs appropriately.