import stack as sk

def upload_from_csv(connection , db, stack):
    x = input("Upload CSV")

    try:
        with open("x.csv") as f:
            print(f.read)
    except Exception as e:
        print(f"\n{x}.csv File must be in the same folder\n",e)

    sk.go_back(stack)