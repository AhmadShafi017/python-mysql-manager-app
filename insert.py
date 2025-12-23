import re

# Insert
def insert_user(connection,name:str,age:int,email:str):

    #------------------------Validation-----------------------

    if not re.match(r"^[A-Za-z ]+$",name):        # Name contain character only.
        print(f"❌ Invalid name: '{name}'. Name must contain only letters.")
        return
     
    if(age < 0 ):                          # Age can't be negative
        print(f"❌ Invalid age for '{name}'. Age cannot be negative.")
        return
    
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):   # email check
        print(f"❌ Invalid email format for '{name}': {email}")
        return
    
    #---------------------------------------------------------------


    query = """
    INSERT INTO users(name, age, email) 
    VALUES (%s,%s,%s)
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query,(name,age,email))
        connection.commit()
        print(f"User: {name} was added to your database!")
    except Exception as e:
        print("❌ Database error:",e)