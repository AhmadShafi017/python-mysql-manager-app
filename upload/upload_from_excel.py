# uploads/upload_excel.py

import pandas as pd
import stack as sk


def upload_from_excel(connection, db, stack):
    filename = input("Enter Excel filename (without .xlsx): ").strip()
    filepath = f"{filename}.xlsx"

    try:
        # 1️⃣ Read Excel file
        df = pd.read_excel(filepath)

        if df.empty:
            print("❌ Excel file is empty.")
            sk.go_back(stack)
            return

        excel_columns = list(df.columns)

        # 2️⃣ Get DB table columns
        cursor = connection.cursor()
        cursor.execute("DESCRIBE users")
        db_columns = [col[0] for col in cursor.fetchall()]

        # Remove auto-generated column
        if "id" in db_columns:
            db_columns.remove("id")

        # 3️⃣ Compare schemas
        if set(excel_columns) != set(db_columns):
            print("❌ Column mismatch!")
            print("Excel columns:", excel_columns)
            print("DB columns   :", db_columns)
            sk.go_back(stack)
            return

        # 4️⃣ Prepare insert query
        query = f"""
            INSERT INTO users ({",".join(excel_columns)})
            VALUES ({",".join(["%s"] * len(excel_columns))})
        """

        # Convert dataframe rows to tuples
        rows = [tuple(row) for row in df.itertuples(index=False, name=None)]

        cursor.executemany(query, rows)
        connection.commit()

        print(f"✅ {len(rows)} records inserted successfully from Excel.")

    except FileNotFoundError:
        print(f"❌ File '{filepath}' not found.")
    except ValueError as e:
        print("❌ Excel format error:", e)
    except Exception as e:
        print("❌ Upload failed:", e)
    finally:
        sk.go_back(stack)
