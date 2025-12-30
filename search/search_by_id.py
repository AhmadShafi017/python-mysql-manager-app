import stack as sk

def search_by_id(connection, db, stack):
    """Search user by ID"""
    try:
        user_id = input("Enter user ID: ").strip()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()

        if not row:
            print(f"❌ No user found with ID {user_id}")
        else:
            print(row)

    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        sk.go_back(stack)
    return
