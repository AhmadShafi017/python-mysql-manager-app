import stack as sk
from pages import ADD, DELETE, UPDATE, SEARCH, ANALYTICS

def start(connection, db, stack):


    choice = input(
        "Enter Option\n"
        "1 - Add\n"
        "2 - Delete\n"
        "3 - Update\n"
        "4 - Search\n"
        "5 - Analytic Function\n"
        "0 - Exit\n"
    ).strip()

    if choice == '1':
        sk.go_to(ADD, stack)
        return

    elif choice == '2':
        sk.go_to(DELETE, stack)
        return

    elif choice == '3':
        sk.go_to(UPDATE, stack)
        return

    elif choice == '4':
        sk.go_to(SEARCH, stack)
        return

    elif choice == '5':
        sk.go_to(ANALYTICS, stack)
        return

    elif choice == '0':
        confirm = input("Are you sure you want to exit?\n" \
        "(y/n: \t)").lower()
        if confirm == 'y':
            stack.clear()
        return
            

    else:
        print("❌ Invalid input! Try again.\n")
        return
