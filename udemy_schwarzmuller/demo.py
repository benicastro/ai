import shutil

active_db_file = "app.db"
backup_db_file = "backup.db"

def backup_db():
    shutil.copy(active_db_file, backup_db_file)
    print(f"Backup of {active_db_file} created as {backup_db_file}")

def restore_db():
    shutil.copy(backup_db_file, active_db_file)
    print(f"Restored {backup_db_file} to {active_db_file}")

def main():
    print("1. Backup Database")
    print("2. Restore Database")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        backup_db()
    elif choice == "2":
        restore_db()
    elif choice == "3":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()

