import mysql.connector
from mysql.connector import Error
import streamlit as st

# Function to establish a connection with the MySQL database
def create_connection():
    try:
        # Configure database connection details
        connection = mysql.connector.connect(
            host='localhost',         # Host where MySQL is running (usually localhost for local dev)
            database='linguakids',    # Name of the database to connect to
            user='root',              # Username for MySQL login
            password=''               # Password for MySQL login (empty for local root access)
        )
        # Check if the connection was successfully established
        if connection.is_connected():
            return connection
    except Error as e:
        # Show error message in Streamlit app if connection fails
        st.error(f"Database connection error: {e}")
        return None

# Function to handle user registration
def register_user(username, password):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Check if the username already exists in the database
            cursor.execute('SELECT * FROM users WHERE name = %s', (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                st.error("Username already exists. Please choose a different one.")
                return False
            
            # Insert new user into the database
            cursor.execute('INSERT INTO users (name, password) VALUES (%s, %s)', (username, password))
            connection.commit()  # Save changes to the database
            st.success("Registration successful! You can now log in.")
            return True
        except Error as e:
            st.error(f"Error during registration: {e}")
            return False
        finally:
            connection.close()  # Always close the connection to free resources

# Function to verify user credentials during login
def authenticate_user(username, password):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Check if there's a user with the given username and password
            cursor.execute('SELECT * FROM users WHERE name = %s AND password = %s', (username, password))
            user = cursor.fetchone()  # Returns the user row if found, else None
            return user
        except Error as e:
            st.error(f"Authentication error: {e}")
            return None
        finally:
            connection.close()
