

# Delete

def delete_user(connection):

    x = input("What do you want to delete?\n" \
    "1 - User\n" \
    "2 - Table\n" \
    "3 - Database")

    cursor = connection.cursor()
    
    try:

        if x == '1':
            id = input("Enter User Id : ")
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query,(id,))
            connection.commit()

            print(f"✅ User with ID {id} deleted.")

        elif x == "2":
            table = input("Enter the table name : ")

            confirm = input(f"⚠️ Are you sure to delete table '{table}'?")
            if confirm.lower() != "yes":
                print("❌ Operation cancelled.")
                return
            
            query = f"DROP TABLE {table}"
            cursor.execute(query)
            connection.commit()

            print(f"✅ Table {table} deleted.")

        elif x == '3':
            database = input("Enter the Database name : ")

            confirm = input(f"⚠️ Are you sure to delete database {database}?")
            if confirm.lower() != "yes":
                print("❌ Operation cancelled.")
                return
            query = "DROP DATABASE {database}"
            cursor.execute(query)
            connection.commit()

    except Exception as e:
        print(print("❌ Database error:", e))
   
        



    

  