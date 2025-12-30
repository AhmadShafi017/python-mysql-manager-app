import stack as sk

def search_by_age(connection, db, stack):
    """Search user by age"""
    try:
        age = input("Enter age: ").strip()
        if not age.isdigit():
            print("❌ Age must be a number.")
            return

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE age = %s", (age,))
        rows = cursor.fetchall()

        if not rows:
            print(f"❌ No users found with age {age}")
        else:
            for row in rows:
                print(row)

    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        sk.go_back(stack)
    return
