import sys
from typing import Protocol

class IMenuDisplay(Protocol):
    def show_menu(self):  
        """Displays the main menu options to the user."""

    def display_message(self, message: str):
        """Displays a message to the user."""

class IUserInput(Protocol):
    def get_input(self, prompt: str) -> str:
        """Gets input from the user based on a prompt."""

class ConsoleMenuDisplay(IMenuDisplay):
    def show_menu(self):
        print("Welcome to the Database Manager!\n")
        print("Please select an option:")
        print("1. Add Record")
        print("2. Update Record")
        print("3. Delete Record")
        print("4. View Records")
        print("5. Exit")

    def display_message(self, message: str):
        print(message)

class ConsoleUserInput(IUserInput):
    def get_input(self, prompt: str) -> str:
        return input(prompt)

class UserInterface:
    def __init__(self, menu_display: IMenuDisplay, user_input: IUserInput):
        self.menu_display = menu_display
        self.user_input = user_input

    def run(self):
        while True:
            self.menu_display.show_menu()
            choice = self.user_input.get_input("Enter your choice: ")

            if choice == '1':
                self.menu_display.display_message("Adding record...")
                # Add record logic here
            elif choice == '2':
                self.menu_display.display_message("Updating record...")
                # Update record logic here
            elif choice == '3':
                self.menu_display.display_message("Deleting record...")
                # Delete record logic here
            elif choice == '4':
                self.menu_display.display_message("Viewing records...")
                # View records logic here
            elif choice == '5':
                self.menu_display.display_message("Exiting...")
                break
            else:
                self.menu_display.display_message("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu_display = ConsoleMenuDisplay()
    user_input = ConsoleUserInput()
    ui = UserInterface(menu_display, user_input)
    ui.run()