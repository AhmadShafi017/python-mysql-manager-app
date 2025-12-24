import stack as sk

def total_users(connection, db, stack):
    """Calculate total users in database"""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        result = cursor.fetchone()

        print(f"📊 Total users: {result[0]}")

    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        sk.go_back(stack)
    return
