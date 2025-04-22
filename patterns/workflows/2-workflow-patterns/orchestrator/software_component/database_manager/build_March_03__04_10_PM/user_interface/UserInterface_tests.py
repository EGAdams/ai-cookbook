import unittest
from unittest.mock import MagicMock

class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.menu_display = ConsoleMenuDisplay()
        self.user_input = ConsoleUserInput()
        self.ui = UserInterface(self.menu_display, self.user_input)

    def test_show_menu(self):
        self.menu_display.show_menu()  # Just to check that it runs without error.

    def test_invalid_choice(self):
        self.user_input.get_input = MagicMock(return_value='6')  # Simulate invalid input
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.ui.run()
            mocked_print.assert_any_call("Invalid choice. Please try again.")

    def test_exit_choice(self):
        self.user_input.get_input = MagicMock(return_value='5')  # Simulate exit input
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.ui.run()
            mocked_print.assert_any_call("Exiting...")

if __name__ == '__main__':
    unittest.main()