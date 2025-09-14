import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL
);
""")
conn.commit()


# ---------------- FUNCTIONS ---------------- #

def add_user():
    print("\n--- Add New User ---")
    name = input("Enter name: ")
    email = input("Enter email: ")
    age = input("Enter age: ")

    try:
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                       (name, email, age))
        conn.commit()
        print(f"✅ User {name} added successfully!")
    except Exception as e:
        print("Error adding user:", e)


def show_all_users():
    print("\n--- All Users ---")
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    if rows:
        print("ID | Name | Email | Age")
        print("=" * 40)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    else:
        print("No users found.")


def update_user():
    show_all_users()
    print("\n--- Update User ---")
    try:
        user_id = int(input("Enter user ID to update: "))
        new_name = input("New name (leave blank to keep current): ")
        new_email = input("New email (leave blank to keep current): ")
        new_age = input("New age (leave blank to keep current): ")

        # Fetch current user
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        if not user:
            print(f"❌ User with ID {user_id} does not exist!")
            return

        # Keep old values if new ones not entered
        updated_name = new_name if new_name else user[1]
        updated_email = new_email if new_email else user[2]
        updated_age = new_age if new_age else user[3]

        cursor.execute("UPDATE users SET name=?, email=?, age=? WHERE id=?", 
                       (updated_name, updated_email, updated_age, user_id))
        conn.commit()

        print(f"✅ User {user_id} updated successfully!")
    except Exception as e:
        print("Error updating user:", e)


def delete_user():
    show_all_users()
    print("\n--- Delete User ---")
    try:
        user_id = int(input("Enter user ID to delete: "))
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()

        if cursor.rowcount == 0:
            print(f"❌ User with ID {user_id} does not exist!")
        else:
            print(f"✅ User {user_id} deleted successfully!")
    except Exception as e:
        print("Error deleting user:", e)


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
