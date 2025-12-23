import database as db
import home

# Main Function
def main():
    connection = db.get_connection("testdb")

    try:
        # Create my table
        if connection:
            db.create_table(connection)

            while True:

                choice = input("Enter Option\n (" \
                "1 - Add,\n" \
                "2 - Delete,\n " \
                "3 - Update,\n " \
                "4 - Search,\n " \
                "5 - Add Many,\n" \
                "6 - calculation\n")

                home.start(choice,connection,db)

                x = input("Want to see more features?\n "
                "11 - Yes\n"
                "00 - Exit.\n")
                if x == '00':
                    print("Exiting...\n")
                    break

                elif x == '11':
                    continue

                else:
                    print("Invalid input! Try again.\n")

                
                    

    finally:
        connection.close()
    

if __name__=="__main__":
    main()