import stack as sk

def update_name(connection, db, stack):
    """
    Update the 'name' of a user in the database
    """

    try:
        user_id = input("Enter the user ID you want to update: ").strip()
        new_name = input("Enter the new name: ").strip()

        # Validate name: only letters
        if not new_name.isalpha():
            print("❌ Name must contain only letters.")
            return

        query = "UPDATE users SET name = %s WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(query, (new_name, user_id))
        connection.commit()

        print(f"✅ User ID {user_id} updated with new name: {new_name}")

    except Exception as e:
        print(f"❌ Database error: {e}")

    finally:
        # Go back to previous page in stack
        sk.go_back(stack)
    return
