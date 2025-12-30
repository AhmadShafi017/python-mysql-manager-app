import stack as sk
import re

def delete_database(connection, db, stack):
    """
    Delete a database after user confirmation.
    """
    database_name = input("Enter the database name to delete: ").strip()

    # Basic validation: database name should contain only letters, numbers, underscore
    if not re.match(r'^[A-Za-z0-9_]+$', database_name):
        print("❌ Invalid database name.")
        return

    confirm = input(f"⚠️ Are you sure to delete the database '{database_name}'? Type 'yes' to confirm: ").strip()
    if confirm.lower() != "yes":
        print("❌ Operation cancelled.")
        return

    query = f"DROP DATABASE {database_name}"

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(f"✅ Database '{database_name}' deleted successfully.")
    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        sk.go_back(stack)
