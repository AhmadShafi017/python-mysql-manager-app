# All of our imports
import os
from dotenv import load_dotenv
import mysql.connector
import re
from insert import insert_user
from search import fetch_users
from delete import delete_user
from update import update_users
from multiple_users import insert_users
from total_math import total_everything
from avarage_math import avarage_everything


# Load the variable from .env
load_dotenv()

# setup / Initialize database
def get_connection(db):

    try:
        connection = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = db
        )
        print(f"Connected to {db} database")
        return connection
    
    except mysql.connector.Error as e:
        print(f"Error : {e}")
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
        print("Table was created!")

    except mysql.connector.Error as e:
        print("Table creation failed: ",e)













