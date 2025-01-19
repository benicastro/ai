import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

active_db_file = "app.db"
backup_db_file = "backup.db"

def backup_db():
    try:
        shutil.copy(active_db_file, backup_db_file)
        logging.info(f"Backup of {active_db_file} created as {backup_db_file}")
    except FileNotFoundError:
        logging.error(f"Error: {active_db_file} not found.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def restore_db():
    try:
        shutil.copy(backup_db_file, active_db_file)
        logging.info(f"Restored {backup_db_file} to {active_db_file}")
    except FileNotFoundError:
        logging.error(f"Error: {backup_db_file} not found.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def main():
    while True:
        print("1. Backup Database")
        print("2. Restore Database")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            backup_db()
        elif choice == "2":
            restore_db()
        elif choice == "3":
            logging.info("Exiting...")
            break
        else:
            logging.warning("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

