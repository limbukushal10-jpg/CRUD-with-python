

# ---------------- MAIN APP LOOP ---------------- #

def main():
    print("Welcome to Simple CRUD App! ✅")
    while True:
        print("\n==============================")
        print("       SIMPLE CRUD APP")
        print("==============================")
        print("1. Add User")
        print("2. Show All Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            show_all_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
