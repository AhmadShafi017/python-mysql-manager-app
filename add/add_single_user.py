import stack as sk

def add_single_user(connection,db,stack):

    name = input("Enter name :").strip()
    age = int(input("Enter age :"))
    email = input("Enter email :").strip()

      # ----------------- Validation -----------------
    if not name.isalpha():
        print("❌ Name must contain only letters!")
        return

    if age < 0:
        print("❌ Age cannot be negative!")
        return

    if "@" not in email:
        print("❌ Invalid email format!")
        return
    # --------------------------------------------
    
    query = """
    INSERT INTO users(name, age, email) 
    VALUES (%s,%s,%s)
    """

    try:
        cursor = connection.cursor()
        cursor.execute(query,(name,age,email))
        connection.commit()
        print(f"✅ User: {name} was added to your database!")

    except Exception as e:
        print("❌ Database error:",e)

    sk.go_back(stack)