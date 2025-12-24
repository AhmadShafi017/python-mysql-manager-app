import stack as sk
from pages import SEARCH_ALL_USER,SEARCH_BY_ID,SEARCH_BY_NAME,SEARCH_BY_AGE,SEARCH_BY_EMAIL

def search(connection,db,stack):

    x = input("what do you want to search ?\n" \
    "1 - All users\n" \
    "2 - Search by Id\n" \
    "3 - Search by name\n" \
    "4 - search by Age\n" \
    "5 - Search by email\n"
    "0 - Back\n")

    if x == '1':
        sk.go_to(SEARCH_ALL_USER,stack)

    elif x == '2':
        sk.go_to(SEARCH_BY_ID,stack)

    elif x == '3':
        sk.go_to(SEARCH_BY_NAME,stack)

    elif x == '4':
        sk.go_to(SEARCH_BY_AGE,stack)

    elif x == '5':
        sk.go_to(SEARCH_BY_EMAIL,stack)

    elif x == '0':
        sk.go_back(stack)

