import re


# Add Multiple Users
def insert_users(connection,users:list[tuple[str, int, str]]):
    valid_users = []

     #--------------------------Validation--------------------------------------------------
    for name,age,email in users:

        if not re.match(r"^[A-Za-z ]+$",name):                                       # Name contain character only.
            print(f"❌ Invalid name: '{name}'. Name must contain only letters.")
            continue
        
        if(age < 0 ):                                                               #Age can't be negative
            print("Age can be negative! Invalid error for {name}")
            continue
            
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):                              # Email check
            print("Invalid email format for {name}.")
            continue

        valid_users.append((name,age,email))

    if not valid_users:
        print("No valid users found to add")
        return
    #-----------------------------------------------------------------------------------------------


    query = "INSERT INTO users (name,age,email) VALUES (%s,%s,%s)"

    try:
        cursor = connection.cursor()
        cursor.executemany(query, valid_users)
        connection.commit()
        print(f"{len(users)} users were added to the database!")
        
    except Exception as e:
        print(e)
