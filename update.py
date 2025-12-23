

# Update 
def update_users(connection, id = id, name = None, age = None, email = None):

    if name is None and age is None and email is None:
        print("Nothing to update! ")
        return
    
    field = []
    value = []


    if name is not None:
        field.append("name = %s")
        value.append(name)

    if age is not None:
        if age < 0 or age > 100:
            print("Age is unrealistic! ")
            return    
    
        field.append("age = %s")
        value.append(age)

    if email is not None:
        import re
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("❌ Invalid email format")
            return

        field.append("email = %s")
        value.append(email)

    query=f"""                         
    UPDATE users
    SET {', '.join(field)}
    WHERE id = %s
    """

    value.append(id)


    try:
        cursor = connection.cursor()
        cursor.execute(query, tuple(value))
        connection.commit()

        if cursor.rowcount == 0:
            print("❌ No user found with that ID")
        else:
            print("✅ User updated successfully")

    except Exception as e:
        print("❌ Database error:",e)