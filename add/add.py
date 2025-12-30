import stack as sk
from pages import ADD_SINGLE_USER,ADD_MULTIPLE_USER,UPLOAD_FROM_CSV,UPLOAD_FROM_JSON,UPLOAD_FROM_EXCEL

def add(connection,db,stack):

    x = input("Chose one : \n" \
    "1 - Add single user\n" \
    "2 - Add multiple users\n" \
    "3 - Upload from CSV\n" \
    "4 - Upload from Json\n" \
    "5 - Upload from Excel\n" \
    "0 - Back\n").strip()

    if x == '1':
        sk.go_to(ADD_SINGLE_USER,stack)
        return
    
    elif x == '2':
        sk.go_to(ADD_MULTIPLE_USER,stack)
        return
    
    elif x == '3':
        sk.go_to(UPLOAD_FROM_CSV,stack)
        return
    
    elif x == '4':
        sk.go_to(UPLOAD_FROM_JSON,stack)
        return
    
    elif x == '5':
        sk.go_to(UPLOAD_FROM_EXCEL,stack)
        return
    
    elif x == '0':
        sk.go_back(stack)
        return
    
    else:
        print("❌ Invalid choice! Try again.\n")
    