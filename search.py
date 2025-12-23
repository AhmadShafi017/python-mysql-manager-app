

# Query all users in Database / Search
def fetch_users(connection,id = None, name = None, age = None, email = None):
    
    condition = []
    value = []


    if id is not None:
        condition.append("id = %s")
        value.append(id)

    if name is not None:
        condition.append("name = %s")
        value.append(name)

    if age is not None:
        condition.append("age = %s")
        value.append(age)

    if email is not None:
        condition.append("email = %s")
        value.append(email)



    query = """
        SELECT * FROM users
    """
    if condition:
        query += "WHERE " + "AND ".join(condition) 

    try:
        cursor = connection.cursor()
        cursor.execute(query,tuple(value))
        rows = cursor.fetchall()
        return rows
    
    except Exception as e:
        print("❌ Search error:",e)
        return []





        