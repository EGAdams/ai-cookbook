The following Python code is used to instruct an autonomous AI agent system to build a server manager system:
```python
if __name__ == "__main__":
    orchestrator = SoftwareOrchestrator()

    # Example: Building a server manager system
    requirements = (
        "Design and implement a Server Manager system that provides functionality to start, stop, and check the status of servers. "
        "The system should allow for retrieving server error logs. "
        "Create a base ServerManager interface or abstract class that defines these operations. "
        "Implement specific managers for MySQL and Apache servers by extending the base ServerManager. "
        "Ensure that each server manager correctly handles process management and error retrieval."
    )

    constraints = (
        "The system should follow SOLID principles to allow easy extension for other server types in the future. "
        "Implement the system in Python and ensure it is compatible with Linux-based server environments. "
        "Use subprocess or OS-specific commands for starting, stopping, and checking the status of the servers. "
        "Provide unit tests to verify the correct functionality of each component. "
    )

    result = orchestrator.design_software_component(
        requirements=requirements, constraints=constraints
    )
```

Using the preceeding source code as a guide, write the Python code that will create a database manager system for MySQL.  The database manager should be able to create, delete, search and modify database records.  

There shall be a menu presented to the user for each operation for example:
```
1. create record
2. delete records with certain criterion
3. modify records with certain criterion
4. search records
... etc.
```

The output of the data should be in the following format and be outputted to the file `output.md` with pretty format for the table like this for example:
<style>
    table {
        border-collapse: collapse;
        width: 100%;
        border: 1px solid white;
    }
    th {
        background-color: #333; /* Dark grey */
        color: white;
        padding: 10px;
        border: 1px solid black;
    }
    td {
        background-color: #ddd; /* Light grey */
        color: black;
        padding: 10px;
        border: 1px solid black;
    }
</style>

<table>
    <tr>
        <th>Column 1</th>
        <th>Column 2</th>
        <th>Column 3</th>
    </tr>
    <tr>
        <td>Value 1</td>
        <td>Value 2</td>
        <td>Value 3</td>
    </tr>
    <tr>
        <td>Value 4</td>
        <td>Value 5</td>
        <td>Value 6</td>
    </tr>
</table>


Please write the new main function for the Software Orchestrator to build the new Database manager.


