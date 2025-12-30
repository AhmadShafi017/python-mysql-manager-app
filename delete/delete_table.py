import stack as sk
import re

def delete_table(connection, db, stack):
    """
    Delete a table from the database.
    User must type 'yes' to confirm deletion.
    """
    table = input("Enter the table name to delete: ").strip()

    # Basic validation: table name should contain only letters, numbers, and underscore
    if not re.match(r'^[A-Za-z0-9_]+$', table):
        print("❌ Invalid table name.")
        return

    confirm = input(f"⚠️ Are you sure to delete table '{table}'? Type 'yes' to confirm: ").strip()
    if confirm.lower() != "yes":
        print("❌ Operation cancelled.")
        return

    query = f"DROP TABLE {table}"

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(f"✅ Table '{table}' deleted successfully.")
    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        sk.go_back(stack)
