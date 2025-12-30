# add_multiple_user.py
import stack as sk
import re

def add_multiple_user(connection, db, stack):
    """Add multiple users interactively with validation"""
    try:
        n = int(input("How many users do you want to add? "))
        if n <= 0:
            print("❌ Number must be greater than 0.")
            return
    except ValueError:
        print("❌ Invalid number.")
        return

    users = []
    for i in range(n):
        print(f"\nUser {i+1}:")
        name = input("Enter name: ").strip()
        if not name.isalpha():
            print("❌ Name must contain only letters.")
            continue

        try:
            age = int(input("Enter age: ").strip())
            if age < 0:
                print("❌ Age cannot be negative.")
                continue
        except ValueError:
            print("❌ Age must be a number.")
            continue

        email = input("Enter email: ").strip()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("❌ Invalid email format.")
            continue

        users.append((name, age, email))

    if not users:
        print("❌ No valid users to add.")
        sk.go_back(stack)
        return

    try:
        query = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)"
        cursor = connection.cursor()
        cursor.executemany(query, users)
        connection.commit()
        print(f"✅ {len(users)} users added successfully!")
    except Exception as e:
        print(f"❌ Database error: {e}")

    sk.go_back(stack)
