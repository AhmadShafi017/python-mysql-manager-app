import stack as sk
from pages import ADD_SINGLE_USER,ADD_MULTIPLE_USER

def add(connection,db,stack):

    x = input("Chose one : \n" \
    "1 - Add single user\n" \
    "2 - Add multiple users\n" \
    "0 - Back\n").strip()

    if x == '1':
        sk.go_to(ADD_SINGLE_USER,stack)
        return
    
    elif x == '2':
        sk.go_to(ADD_MULTIPLE_USER,stack)
        return
    
    elif x == '0':
        sk.go_back(stack)
        return
    
    else:
        print("❌ Invalid choice! Try again.\n")
    