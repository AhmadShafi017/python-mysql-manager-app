# uploads/upload_json.py

import json
import stack as sk

def upload_from_json(connection, db, stack):
    filename = input("Enter JSON filename (without .json): ").strip()
    filepath = f"{filename}.json"

    try:
        # 1️⃣ Load JSON file
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not data or not isinstance(data, list):
            print("❌ JSON file is empty or invalid format. Expecting a list of objects.")
            sk.go_back(stack)
            return

        json_columns = list(data[0].keys())

        # 2️⃣ Get DB table columns
        cursor = connection.cursor()
        cursor.execute("DESCRIBE users")
        db_columns = [col[0] for col in cursor.fetchall()]

        # Remove auto-generated column
        if "id" in db_columns:
            db_columns.remove("id")

        # 3️⃣ Compare schemas
        if set(json_columns) != set(db_columns):
            print("❌ Column mismatch!")
            print("JSON columns:", json_columns)
            print("DB columns  :", db_columns)
            sk.go_back(stack)
            return

        # 4️⃣ Prepare insert query
        query = f"""
            INSERT INTO users ({",".join(json_columns)})
            VALUES ({",".join(["%s"] * len(json_columns))})
        """

        # Convert JSON objects to tuples in the same order as columns
        rows = [tuple(item[col] for col in json_columns) for item in data]

        cursor.executemany(query, rows)
        connection.commit()

        print(f"✅ {len(rows)} records inserted successfully from JSON.")

    except FileNotFoundError:
        print(f"❌ File '{filepath}' not found.")
    except json.JSONDecodeError:
        print(f"❌ Failed to parse JSON file. Check the format.")
    except Exception as e:
        print("❌ Upload failed:", e)
    finally:
        sk.go_back(stack)
