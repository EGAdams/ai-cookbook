import sys
# import MySQLServerManager from build_March_02__09_52_AM.MySQLServerManager
from MySQLServerManager import MySQLServerManager


def main_menu(server_manager):
    while True:
        print("\nMySQL Server Manager Menu:")
        print("1. Start Server")
        print("2. Stop Server")
        print("3. Check Status")
        print("4. Retrieve Error Logs")
        print("5. Clear MySQL server logs")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if server_manager.start_server():
                print("MySQL server started successfully.")
            else:
                print("Failed to start MySQL server.")
        elif choice == "2":
            if server_manager.stop_server():
                print("MySQL server stopped successfully.")
            else:
                print("Failed to stop MySQL server.")
        elif choice == "3":
            status = server_manager.check_status()
            if status:
                print("Server Status:\n" + status)
            else:
                print("Failed to retrieve server status.")
        elif choice == "4":
            logs = server_manager.retrieve_error_logs()
            print("Error Logs:\n" + logs)
        elif choice == "5":
            if server_manager.clear_logs():
                print("MySQL server logs cleared successfully.")
            else:
                print("Failed to clear MySQL server logs.")

        elif choice == "6":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    mysql_service_name = "mysql"  # Modify as needed
    server_manager = MySQLServerManager(mysql_service_name)
    main_menu(server_manager)
