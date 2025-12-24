from pages import TOTAL_USERS, AVERAGE_AGE
import stack as sk

from pages import TOTAL_USERS,AVERAGE_AGE

def analytics(connection, db, stack):

    x = input("What you want to calculate?\n" \
    "1 - total users\n" \
    "2 - Avarage age\n" \
    "0 - Back\n")

    if x == '1':
        sk.go_to(TOTAL_USERS,stack)
        return
        
    
    elif x == '2':
        sk.go_to(AVERAGE_AGE,stack)
        return

    elif x == '0':
        sk.go_back(stack)
        return

    else:
        print("Invalid input! Try again.")
        