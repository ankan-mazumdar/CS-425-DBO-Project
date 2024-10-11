
# import mysql.connector

# con = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=""
#     # auth_plugin='mysql_native_password'
# )

# print(con)

# if con:
#     print("Connection Successful")
# else:
#     print("Connection Unsuccessful")
import tkinter as tk
from tkinter import messagebox
import mysql.connector    
def connect_mysql():
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Ankan@2020",
        database = "fifa_wc"
        )  
        print("Connection successsful")       
        return mydb
    except mysql.connector.Error as e:
        print("Error:",e)
connect_mysql    

def fetch_all_databases():
    mydb = connect_mysql()
    print("Databases on the server:")
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for (database_name,) in mycursor:
        print(database_name)
    mycursor.close()
    mydb.close()


def fetch_all_tables():
    mydb = connect_mysql()
    if mydb is not None:
        try:
            mycursor = mydb.cursor()
            mycursor.execute("SHOW TABLES")
            print("Tables in the database:")
            for (table_name,) in mycursor:
                print(table_name)
            mycursor.close()
        except mysql.connector.Error as e:
            print("Error:", e)
        finally:
            mydb.close()
    else:
        print("Database connection was not established.")


def read_data(table):
    mydb = connect_mysql()
    if mydb is not None:
        try:
            mycursor = mydb.cursor()
            query = f"SELECT * FROM {table}"
            mycursor.execute(query)
            for row in mycursor.fetchall():
                print(row)
            mycursor.close()
        except mysql.connector.Error as e:
            print("Error:", e)
        finally:
            mydb.close()
    else:
        print("Database connection was not established.")


#read_data()

def insert_data():
    query = input("Please enter your INSERT query: ")
    try:
        mydb = connect_mysql()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute(query)
            mydb.commit()
            print(mycursor.rowcount, "record(s) inserted.")
            mycursor.close()
           
        else:
            print("Failed to establish a database connection.")
    except Error as e:
        print(f"Error executing INSERT query: {e}")

def update_data():
    query = input("Please enter your UPDATE query: ")
    try:
        mydb = connect_mysql()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute(query)
            mydb.commit()
            print(mycursor.rowcount, "record(s) updated.")
            mycursor.close()
         
        else:
            print("Failed to establish a database connection.")
    except Error as e:
        print(f"Error executing UPDATE query: {e}")

def delete_data():
    query = input("Please enter your DELETE query: ")
    try:
        mydb = connect_mysql()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute(query)
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted.")
            mycursor.close()
          
        else:
            print("Failed to establish a database connection.")
    except Error as e:
        print(f"Error executing DELETE query: {e}")

def custom_query():
    query = input("Please enter your SQL query (semicolon-separated for multiple queries): ")
    try:
        mydb = connect_mysql()
        if mydb:
            mycursor = mydb.cursor()
            # Split the input query by semicolon to get individual queries
            queries = query.split(';')
            for q in queries:
                if q.strip():  # Check if the query is not empty
                    mycursor.execute(q)
                    result = mycursor.fetchall()
                    if result:
                        for row in result:
                            print(row)
                    else:
                        print("No results found for query:", q)
            mycursor.close()
        else:
            print("Failed to establish a database connection.")
    except mysql.connector.Error as e:
        print(f"Error executing SQL query: {e}")



def perform_crud():
    while True:
        print("System Menu: Select any of these operations you want to perform.such as 0 for show databases")
        print("[0] Show databases")
        print("[1] Show tables")
        print("[2] Create/Insert records")
        print("[3] Read/Select records")
        print("[4] Update records")
        print("[5] Delete records")
        print("[6] Execute custom query")
        print("[7] Exit")
        
        operation = input("Enter the operation number: ")
        
        if operation == '0':
            fetch_all_databases()
        elif operation == '1':
            fetch_all_tables()
        elif operation == '2':
            insert_data()
        elif operation == '3':
            table_name = input("Which table do you want to view? ")
            read_data(table_name)
        elif operation == '4':
            update_data()
        elif operation == '5':
            delete_data()
        elif operation == '6':
            custom_query()
        elif operation == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid operation selected. Please choose a valid option.")


if __name__ == "__main__":
    perform_crud()
