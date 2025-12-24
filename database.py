# All of our imports
import os
from dotenv import load_dotenv
import mysql.connector



# Load the variable from .env
load_dotenv()

# setup / Initialize database
def get_connection():

    try:
        connection = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
        )
        print(f"Connected to database")
        return connection
    
    except mysql.connector.Error as e:
        print(f"❌ Database connection error", e)
        return None

# Create a table in database
def create_table(connection):
    query = """
        CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        name VARCHAR(100) NOT NULL,
        age INT,
        email VARCHAR(200) UNIQUE
        )AUTO_INCREMENT = 101
    """
    try: 
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("✅ Table was created!")

    except mysql.connector.Error as e:
        print("❌ Table creation failed: ", e)



