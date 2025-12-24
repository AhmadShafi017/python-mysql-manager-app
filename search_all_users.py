import stack as sk

def search_all_user(connection, db, stack):
    """Fetch all users"""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        if not rows:
            print("❌ No users found.")
        else:
            for row in rows:
                print(row)

    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        sk.go_back(stack)
    return
