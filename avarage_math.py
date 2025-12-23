
def avarage_everything(connection):
    
    x = input("What you want to see the avarage of? \n" \
    "1 - Age \n")


    if x == '1':
        column = "age"
        

    query = f"SELECT AVG({column}) FROM users"

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()

        if result[0] is None:
            print("❌ No data found.")
        else:
            print(f"📊 Average {column}: {round(result[0], 2)}")
        
    
    except Exception as e:
        print("❌ Database error :",e)
