import stack as sk
from pages import UPDATE_NAME, UPDATE_AGE, UPDATE_EMAIL

def update(connection, db, stack):
    """
    Update user details: name, age, email
    """

    choice = input("What do you want to update?\n"
                   "1 - Name\n"
                   "2 - Age\n"
                   "3 - Email\n"
                   "0 - Back\n").strip()

    if choice == '1':
        sk.go_to(UPDATE_NAME, stack)
        return

    elif choice == '2':
        sk.go_to(UPDATE_AGE, stack)
        return

    elif choice == '3':
        sk.go_to(UPDATE_EMAIL, stack)

    elif choice == '0':
        sk.go_back(stack)
        return

    else:
        print("❌ Invalid input! Try again.\n")
