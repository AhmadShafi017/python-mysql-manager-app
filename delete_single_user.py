import stack as sk

def delete_single_user(connection, db, stack):
    try:
        user_id = input("Enter User ID to delete: ")
        
        if not user_id.isdigit():
            print("❌ Invalid ID. Must be a number.")
            return

        user_id = int(user_id)
        query = "DELETE FROM users WHERE id = %s"

        cursor = connection.cursor()
        cursor.execute(query, (user_id,))
        connection.commit()

        if cursor.rowcount == 0:
            print(f"❌ No user found with ID {user_id}.")
        else:
            print(f"✅ User with ID {user_id} deleted.")

    except Exception as e:
        print(f"❌ Database error: {e}")

    finally:
        sk.go_back(stack)
