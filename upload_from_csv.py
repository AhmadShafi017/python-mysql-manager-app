import csv
import stack as sk

def upload_from_csv(connection , db, stack):
    filename = input("Enter the CSV filename (without extension):").strip()
    full_path = f"{filename}.csv"
    

    try:
        #----------READ CSV----------------------------
        with open(full_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            csv_columns = reader.fieldnames
            
            if not csv_columns:
                print("❌ CSV file has no header.")
                sk.go_back(stack)
                return
            


            #--------------READ DB TABLE COLUMNS---------
            cursor = connection.cursor()
            cursor.execute("DESCRIBE users")
            table_columns = [row[0] for row in cursor.fetchall()]


            #Remove auto-increment ID
            if "id" in table_columns:
                table_columns.remove("id")

            #---------COMPARE COLUMNS-----------
            if set(csv_columns) != set(table_columns):
                print("❌ Column mismatch!")
                print(f"CSV columns   : {csv_columns}")
                print(f"Table columns : {table_columns}")
                sk.go_back(stack)
                return
            
            #--------INSERT DATA-------------
            query = """
                INSERT INTO users (name,age,email)
                VSLUES (%s,%s,%s)
            """

            data = []
            for row in reader:
                data.append((
                    row["name"],
                    int(row["age"]),
                    row["email"]
                ))

            cursor.executemany(query,data)
            connection.commit()
            print(f"✅ {len(data)} records uploaded successfully!")

    except FileNotFoundError:
        print(f"❌ File '{full_path}' not found.")

    except Exception as e:
        print("❌ Error while uploading CSV:", e)

    finally:
        sk.go_back(stack)

