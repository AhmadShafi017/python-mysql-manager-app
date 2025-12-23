

def start(choice,connection,db):
    if choice == '1':                # Add
        name = input("Enter name :")
        age = int(input("Enter age :"))
        email = input("Enter email :")
        db.insert_user(connection, name,age,email)


    elif choice == "4":                # Search



        x = input("what do you want to search ?\n" \
        "1 - All users\n" \
        "2 - Search by Id\n" \
        "3 - Search by name\n" \
        "4 - search by Age\n" \
        "5 - SEarch by email\n")

        id = name = age = email = None

        if x == '1':
            print("All Users:")
            for users in db.fetch_users(connection):
                print(users)

        elif x == '2':
            id = input("Enter id")

        elif x == '3':
            name = input("Enter name ")

        elif x == '4':
            age = input("Enter age")

        elif x == '5':
            email = input("Enter email")

        for users in db.fetch_users(connection,id = id, name = name, age = age, email = email):
            print(users)

        

    elif choice == "2":                # Delete
        db.delete_user(connection)

    elif choice == "3":                 #Update
        id = input("Enter the user id : ")

        x = input("What do you want to update ?\n" \
        "1 - Name\n" \
        "2 - Age\n" \
        "3 - Email\n"
        "4 - Name & Age\n"
        "5 - Name & Email\n"
        "6 - Age & Email\n"
        "7 - Name, Age & Email\n")

        if x == '1':
            name = input("Enter the name : ")

        elif x == '2':
            age = input("Enter age : ")

        elif x == '3':
            email = input("Enter email : ")
        
        elif x == '4':
            name = input("Enter the name : ")
            age = input("Enter age : ")
        
        elif x == '5':
            name = input("Enter the name : ")
            email = input("Enter email : ")

        elif x == '6':
            age = input("Enter age : ")
            email = input("Enter email : ")

        elif x == '7':
            name = input("Enter the name : ")
            age = input("Enter age : ")
            email = input("Enter email : ")    

        db.update_users(connection, id = id, name = name, age = age, email = email)



    elif choice == "5":                # Add Many
        users = [("Chandler", 29, "friends@gmail.com"),
                ("trueman", 35, "trueman31@gmail.com"),
                ("Faruk", 55, "faruk66@gmail.com")]
        db.insert_users(connection,users)

    elif choice == '6':                # Mathmatic function
        x = input("What you want to calculate?\n" \
        "1 - total users\n" \
        "2 - Avarage age\n")

        if x == '1':
            db.total_everything(connection)
        
        elif x == '2':
            db.avarage_everything(connection)


    else:
        print("Invalid input! Try again.")