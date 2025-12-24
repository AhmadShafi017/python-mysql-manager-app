# main.py

import database as db
import stack as sk

# page constants
from pages import (
    HOME,
    ADD, ADD_SINGLE_USER, ADD_MULTIPLE_USER,
    DELETE, DELETE_SINGLE_USER, DELETE_MULTIPLE_USER, DELETE_TABLE, DELETE_DATABASE,
    UPDATE, UPDATE_NAME, UPDATE_AGE, UPDATE_EMAIL,
    SEARCH, SEARCH_ALL_USER, SEARCH_BY_ID, SEARCH_BY_NAME, SEARCH_BY_AGE, SEARCH_BY_EMAIL,
    ANALYTICS, TOTAL_USERS, AVERAGE_AGE
)

# main pages
import home


def main():
    connection = db.get_connection()
    stack = []

    if not connection:
        return

    db.create_table(connection)

    # start at HOME
    stack.append(HOME)

    while stack:
        current_page = stack[-1]

        # ---------------- HOME ----------------
        if current_page == HOME:
            home.start(connection, db, stack)

        # ---------------- ADD ----------------
        elif current_page == ADD:
            from add import add
            add(connection, db, stack)

        elif current_page == ADD_SINGLE_USER:
            from add_single_user import add_single_user
            add_single_user(connection, db, stack)

        elif current_page == ADD_MULTIPLE_USER:
            from add_multiple_user import add_multiple_user
            add_multiple_user(connection, db, stack)

        # ---------------- DELETE ----------------
        elif current_page == DELETE:
            from delete import delete
            delete(connection, db, stack)

        elif current_page == DELETE_SINGLE_USER:
            from delete_single_user import delete_single_user
            delete_single_user(connection, db, stack)

        elif current_page == DELETE_MULTIPLE_USER:
             
             from delete_multiple_user import delete_multiple_user
             delete_multiple_user(connection, db, stack)

        elif current_page == DELETE_TABLE:
            from delete_table import delete_table
            delete_table(connection, db, stack)

        elif current_page == DELETE_DATABASE:
            from delete_database import delete_database
            delete_database(connection, db, stack)

        # ---------------- UPDATE ----------------
        elif current_page == UPDATE:
            from update import update
            update(connection, db, stack)

        elif current_page == UPDATE_NAME:
            from update_name import update_name
            update_name(connection, db, stack)

        elif current_page == UPDATE_AGE:
            from update_age import update_age
            update_age(connection, db, stack)

        elif current_page == UPDATE_EMAIL:
            from update_email import update_email
            update_email(connection, db, stack)

        # ---------------- SEARCH ----------------
        elif current_page == SEARCH:
            from search import search
            search(connection, db, stack)

        elif current_page == SEARCH_ALL_USER:
            from search_all_users import search_all_user
            search_all_user(connection, db, stack)

        elif current_page == SEARCH_BY_ID:
            from search_by_id import search_by_id
            search_by_id(connection, db, stack)

        elif current_page == SEARCH_BY_NAME:
            from search_by_name import search_by_name
            search_by_name(connection, db, stack)

        elif current_page == SEARCH_BY_AGE:
            from search_by_age import search_by_age
            search_by_age(connection, db, stack)

        elif current_page == SEARCH_BY_EMAIL:
            from search_by_email import search_by_email
            search_by_email(connection, db, stack)

        # ---------------- ANALYTICS ----------------
        elif current_page == ANALYTICS:
            from analytics import analytics
            analytics(connection, db, stack)

        elif current_page == TOTAL_USERS:
            from total import total_users
            total_users(connection, db, stack)

        elif current_page == AVERAGE_AGE:
            from average import average_age
            average_age(connection, db, stack)

        # ---------------- FALLBACK ----------------
        else:
            print(f"❌ Unknown page: {current_page}")
            sk.go_back(stack)

    connection.close()
    print("👋 Program exited safely")


if __name__ == "__main__":
    main()
