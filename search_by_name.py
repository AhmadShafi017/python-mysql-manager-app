import stack as sk

def search_by_name(connection, db, stack):
    """Search user by name"""
    try:
        name = input("Enter name: ").strip()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE name LIKE %s", (f"%{name}%",))
        rows = cursor.fetchall()

        if not rows:
            print(f"❌ No user found with name '{name}'")
        else:
            for row in rows:
                print(row)

    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        sk.go_back(stack)
    return
