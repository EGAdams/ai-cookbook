
# https://chatgpt.com/share/67c4ae07-3ed0-8006-b147-e16efe491265
import sys
from ApacheServerManager import ApacheServerManager



def main_menu(server_manager):
    while True:
        print("\nApache Server Manager Menu:")
        print("1. Start Server")
        print("2. Stop Server")
        print("3. Check Status")
        print("4. Retrieve Error Logs")
        print("5. Clear Apache Server Logs")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            server_manager.start_server()
        elif choice == "2":
            server_manager.stop_server()
        elif choice == "3":
            server_manager.check_status()
        elif choice == "4":
            server_manager.retrieve_error_logs()
        elif choice == "5":
            if server_manager.clear_logs():
                print("Apache server logs cleared successfully.")
            else:
                print("Failed to clear Apache server logs.")
        elif choice == "6":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    server_manager = ApacheServerManager()
    main_menu(server_manager)