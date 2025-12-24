import stack as sk
from pages import DELETE_SINGLE_USER,DELETE_MULTIPLE_USER,DELETE_TABLE,DELETE_DATABASE



def delete(connection,db,stack):
    x = input("What you want to delete?\n " \
    "1 - User\n" \
    "2 - Multiple users\n" \
    "3 - Table\n" \
    "4 - Database\n" \
    "0 - Back\n" \
    "")


    if x == '1':
        sk.go_to(DELETE_SINGLE_USER,stack)
        return

    elif x == '2':
        sk.go_to(DELETE_MULTIPLE_USER,stack)
        return

    elif x == '3':
        sk.go_to(DELETE_TABLE,stack)
        return

    elif x == '4':
        sk.go_to(DELETE_DATABASE,stack)
        return

    elif x == '0':
        sk.go_back(stack)
        return
    
    else:
        print("Invalid Input")
        return