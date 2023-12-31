import mysql.connector
import re
import os
import configparser

ALLOWED_DOMAINS = ["gmail.com", "outlook.com", "icloud.com", "protonmail.com"]

config_file_path = r"C:\Users\peter\Desktop\config.ini.txt"

def read_db_config(config_file_path):
    config = configparser.ConfigParser()
    config.read(config_file_path)

    return {
        'host': config['database']['DB_HOST'],
        'user': config['database']['DB_USER'],
        'password': config['database']['DB_PASSWORD'],
        'database': config['database']['DB_NAME']
    }

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def view_books(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()

    print("Available Books:")
    for book in books:
        print(f"Book ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Details: {book[3]}")

def view_store(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    locations = cursor.fetchall()

    print("Store Locations:")
    for location in locations:
        print(f"Location Name: {location[1]}")

def view_wishlist(connection, user_id):
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM User WHERE user_id = %s", (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        query = "SELECT b.book_name, b.author FROM Wishlist w JOIN Book b ON w.book_id = b.book_id WHERE w.user_id = %s"
        cursor.execute(query, (user_id,))
        wishlist = cursor.fetchall()

        print("Your Wishlist:")
        if wishlist:
            for item in wishlist:
                print(f"Book Name: {item[0]}, Author: {item[1]}")
        else:
            print("Your wishlist is empty.")
    else:
        print("Invalid user ID. Please enter a valid user ID.")

def add_book_to_wishlist(connection, user_id, book_id):
    cursor = connection.cursor()

    try:
        user_id = int(user_id)
        book_id = int(book_id)
    except ValueError:
        print("Error: User ID and Book ID must be valid integers.")
        return

    query = "INSERT INTO Wishlist (user_id, book_id) VALUES (%s, %s)"
    cursor.execute(query, (user_id, book_id))
    connection.commit()
    print("Book added to your wishlist.")

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    match = re.match(pattern, email)
    
    if match:
        domain = email.split('@')[1]
        if domain in ALLOWED_DOMAINS:
            return True
        else:
            print("Error: This email domain is not allowed for registration.")
            return False
    else:
        print("Error: Invalid email format.")
        return False

def register_user(connection, email, first_name, last_name):
    cursor = connection.cursor()

    if not is_valid_email(email):
        return

    cursor.execute("SELECT email FROM User WHERE email = %s", (email,))
    existing_email = cursor.fetchone()

    if existing_email:
        print("Error: This email is already registered. Please use a different email.")
    else:
        cursor.execute("SELECT COUNT(*) FROM User")
        user_count = cursor.fetchone()[0]

        user_id = f'{user_count + 1:02d}'

        query = "INSERT INTO User (user_id, email, first_name, last_name) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (user_id, email, first_name, last_name))
        connection.commit()
        print(f"User registration successful. Your user ID is: {user_id}")

def main():
    db_config = read_db_config(config_file_path)

    try:
        connection = mysql.connector.connect(**db_config)
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return

    while True:
        clear_screen()
        print("\nMain Menu:")
        print("1. View Books")
        print("2. View Store")
        print("3. My Account")
        print("4. Register User")
        print("5. Exit Program")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_books(connection)
            input("\nPress Enter to continue...")
        elif choice == "2":
            view_store(connection)
            input("\nPress Enter to continue...")
        elif choice == "3":
            clear_screen()
            print("\nMy Account:")
            print("1. View Wishlist")
            print("2. Add Book to Wishlist")
            print("3. Back to Main Menu")

            account_choice = input("Enter your account choice: ")

            if account_choice == "1":
                user_id = input("Enter your user ID: ")
                view_wishlist(connection, user_id)
                input("\nPress Enter to continue...")
            elif account_choice == "2":
                user_id = input("Enter your user ID: ")
                book_id = input("Enter the book ID to add to your wishlist: ")
                add_book_to_wishlist(connection, user_id, book_id)
                input("\nPress Enter to continue...")
            elif account_choice == "3":
                continue
            else:
                print("Invalid account choice. Please try again.")
                input("\nPress Enter to continue...")
        elif choice == "4":
            clear_screen()
            print("\nUser Registration:")
            email = input("Enter your email: ")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            register_user(connection, email, first_name, last_name)
            input("\nPress Enter to continue...")
        elif choice == "5":
            print("Exiting program.")
            connection.close()
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()