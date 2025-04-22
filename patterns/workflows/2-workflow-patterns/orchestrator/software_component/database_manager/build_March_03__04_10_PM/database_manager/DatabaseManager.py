import mysql.connector
from mysql.connector import Error

class IDatabaseConnection:
    def connect(self):
        raise NotImplementedError
    def disconnect(self):
        raise NotImplementedError

class IRecordOperation:
    def create_record(self, table, data):
        raise NotImplementedError
    def delete_record(self, table, identifier):
        raise NotImplementedError
    def modify_record(self, table, identifier, data):
        raise NotImplementedError
    def search_records(self, table, criteria):
        raise NotImplementedError

class DatabaseManager(IDatabaseConnection, IRecordOperation):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Successfully connected to the database.")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

    def create_record(self, table, data):
        try:
            cursor = self.connection.cursor()
            columns = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            query = f'INSERT INTO {table} ({columns}) VALUES ({values})'
            cursor.execute(query, tuple(data.values()))
            self.connection.commit()
            print("Record created successfully.")
        except Error as e:
            print(f"Error creating record: {e}")

    def delete_record(self, table, identifier):
        try:
            cursor = self.connection.cursor()
            query = f'DELETE FROM {table} WHERE id = %s'
            cursor.execute(query, (identifier,))
            self.connection.commit()
            print("Record deleted successfully.")
        except Error as e:
            print(f"Error deleting record: {e}")

    def modify_record(self, table, identifier, data):
        try:
            cursor = self.connection.cursor()
            updates = ', '.join([f'{key} = %s' for key in data.keys()])
            query = f'UPDATE {table} SET {updates} WHERE id = %s'
            cursor.execute(query, tuple(data.values()) + (identifier,))
            self.connection.commit()
            print("Record modified successfully.")
        except Error as e:
            print(f"Error modifying record: {e}")

    def search_records(self, table, criteria):
        try:
            cursor = self.connection.cursor(dictionary=True)
            condition = ' AND '.join([f'{key} = %s' for key in criteria.keys()])
            query = f'SELECT * FROM {table} WHERE {condition}'
            cursor.execute(query, tuple(criteria.values()))
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error searching records: {e}")
            return []