import unittest
from unittest.mock import MagicMock
from mysql.connector import Error

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.db_manager = DatabaseManager('localhost', 'user', 'pass', 'test_db')
        self.db_manager.connect = MagicMock()
        self.db_manager.disconnect = MagicMock()
        self.db_manager.connection = MagicMock()  

    def test_create_record(self):
        self.db_manager.create_record('test_table', {'name': 'John', 'age': 30})
        self.db_manager.connection.cursor.return_value.execute.assert_called_once()  

    def test_delete_record(self):
        self.db_manager.delete_record('test_table', 1)
        self.db_manager.connection.cursor.return_value.execute.assert_called_once()  

    def test_modify_record(self):
        self.db_manager.modify_record('test_table', 1, {'name': 'Jane', 'age': 25})
        self.db_manager.connection.cursor.return_value.execute.assert_called_once()  

    def test_search_records(self):
        self.db_manager.search_records('test_table', {'age': 30})
        self.db_manager.connection.cursor.return_value.execute.assert_called_once()  

    def tearDown(self):
        self.db_manager.disconnect()

if __name__ == '__main__': 
    unittest.main()
