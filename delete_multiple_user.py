import stack as sk

def delete_multiple_user(connection, db, stack):
    """
    Delete multiple users by IDs provided by the user.
    IDs should be comma-separated, e.g., 2,5,7
    """

    user_input = input("Enter User IDs to delete (comma-separated): ")
    try:
        # Convert input into a list of integers
        user_ids = [int(uid.strip()) for uid in user_input.split(",") if uid.strip().isdigit()]

        if not user_ids:
            print("❌ No valid IDs entered.")
            return

        query = "DELETE FROM users WHERE id IN ({})".format(",".join(["%s"] * len(user_ids)))
        cursor = connection.cursor()
        cursor.execute(query, tuple(user_ids))
        connection.commit()

        if cursor.rowcount == 0:
            print("❌ No users were deleted. Check the IDs.")
        else:
            print(f"✅ {cursor.rowcount} users deleted successfully.")

    except Exception as e:
        print(f"❌ Database error: {e}")

    finally:
        sk.go_back(stack)
