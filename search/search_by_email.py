import stack as sk

def search_by_email(connection, db, stack):
    """Search user by email"""
    try:
        email = input("Enter email: ").strip()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        row = cursor.fetchone()

        if not row:
            print(f"❌ No user found with email {email}")
        else:
            print(row)

    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        sk.go_back(stack)
    return
