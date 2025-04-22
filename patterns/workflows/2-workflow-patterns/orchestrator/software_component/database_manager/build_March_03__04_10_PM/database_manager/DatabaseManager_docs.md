# DatabaseManager Module

## Overview
The `DatabaseManager` module provides an interface for performing various database operations such as connecting to a database, creating, deleting, modifying, and searching records. It uses the `mysql-connector-python` library to interact with MySQL databases.

## Interfaces
### IDatabaseConnection
- `connect()` - Establish a connection to the database.
- `disconnect()` - Close the connection to the database.

### IRecordOperation
- `create_record(table, data)` - Insert a new record into the specified table.
- `delete_record(table, identifier)` - Delete a record from the specified table based on the identifier.
- `modify_record(table, identifier, data)` - Modify an existing record in the specified table.
- `search_records(table, criteria)` - Search for records in the specified table based on the given criteria.

## Usage
1. Create an instance of `DatabaseManager` with the necessary database credentials.
2. Call `connect()` to open the database connection.
3. Use the record operations methods as needed.
4. Call `disconnect()` to close the connection when done.

## Example
```python
manager = DatabaseManager(host='localhost', user='root', password='password', database='my_db')
manager.connect()
manager.create_record('my_table', {'name': 'Alice', 'age': 24})
results = manager.search_records('my_table', {'age': 24})
manager.disconnect()
```