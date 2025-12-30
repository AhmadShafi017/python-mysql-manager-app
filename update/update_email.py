import stack as sk
import re

def update_email(connection, db, stack):
    """
    Update the 'email' of a user in the database
    """

    try:
        user_id = input("Enter the user ID you want to update: ").strip()
        new_email = input("Enter the new email: ").strip()

        # Validate email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            print("❌ Invalid email format.")
            return

        query = "UPDATE users SET email = %s WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(query, (new_email, user_id))
        connection.commit()

        print(f"✅ User ID {user_id} updated with new email: {new_email}")

    except Exception as e:
        print(f"❌ Database error: {e}")

    finally:
        sk.go_back(stack)
    return
