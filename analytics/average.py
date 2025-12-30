import stack as sk

def average_age(connection, db, stack):
    """Calculate average age of users"""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT AVG(age) FROM users")
        result = cursor.fetchone()

        if result[0] is None:
            print("❌ No users in database.")
        else:
            print(f"📊 Average age: {round(result[0], 2)}")

    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        sk.go_back(stack)
    return