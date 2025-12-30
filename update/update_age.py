import stack as sk

def update_age(connection, db, stack):
    """
    Update the 'age' of a user in the database
    """

    try:
        user_id = input("Enter the user ID you want to update: ").strip()
        new_age = input("Enter the new age: ").strip()

        # Validate age: must be a positive integer
        if not new_age.isdigit() or int(new_age) < 0:
            print("❌ Age must be a positive integer.")
            return

        query = "UPDATE users SET age = %s WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(query, (int(new_age), user_id))
        connection.commit()

        print(f"✅ User ID {user_id} updated with new age: {new_age}")

    except Exception as e:
        print(f"❌ Database error: {e}")

    finally:
        sk.go_back(stack)
    return
