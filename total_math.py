
def total_everything(connection):
    
    x = input("What you want to see? \n" \
    "1 - total user\n")

    

    if x == '1':
        column = "id"
        label = "users"
        

    query = f"SELECT COUNT({column}) FROM users"

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
    
        if result [0] is None:
            print("❌ No data found.")
        else:
             print(f"📊 Total {label}: {result[0]}")

    except Exception as e:
        print("❌ Database error:",e)