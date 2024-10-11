# FIFA Women's World Cup Database Management System
![image](https://github.com/user-attachments/assets/685000de-aa64-4b8d-abd7-d9821e20f246)

## Project Overview

This project is a Python-based GUI application designed to manage and analyze the FIFA Women's World Cup database. The application provides CRUD (Create, Read, Update, Delete) functionality using MySQL and Tkinter for a user-friendly interface. It includes advanced SQL queries for detailed insights and analysis of the tournament data.

## Features

1. **Database Connection and Details**:
   - Displays server and database information to verify successful connections.
   - ![image](https://github.com/user-attachments/assets/63451c82-ae44-4ae4-a059-5999ef8cf717)

   

   
2. **Database Management**:
   - View all databases and tables in the connected MySQL server.
   - Read records from a specified table.
    ![image](https://github.com/user-attachments/assets/2865db27-285e-4bb6-b362-722188d8d590)

3. **Display all Tables in DB**:
   ![image](https://github.com/user-attachments/assets/6b47d492-2a03-4640-b2ee-8fb8b3bc349a)

4. **Enter table name and read/preview records** :
   ![image](https://github.com/user-attachments/assets/83b4ea04-5a0d-4434-8d70-6b89c8928982)
   ![image](https://github.com/user-attachments/assets/1b793dcc-6c5a-46da-b302-3fbfbd210ca7)

5. **CRUD Operations**:
   - **Insert Records**: Add new entries into the database.
   - ![image](https://github.com/user-attachments/assets/e366c056-5d79-4dd0-b11c-fc2fe5ea6f26)
   - ![image](https://github.com/user-attachments/assets/c1f5302b-2372-4f9f-aaea-a500bc3c2476)

   syntax error-
   ![image](https://github.com/user-attachments/assets/e1927e82-dc1e-434c-b2f8-fa8e486d3e1f)
   ![image](https://github.com/user-attachments/assets/131322e0-2ce9-47aa-954d-92ba0db07071)


   - **Update Records**: Modify existing records based on user queries.
   - ![image](https://github.com/user-attachments/assets/07876357-8231-4657-8176-bbbfcfd30238)
   - ![image](https://github.com/user-attachments/assets/76aab0a9-3c2f-4b44-9113-4460429722c9)


   - **Delete Records**: Remove records using specified conditions.
   - ![image](https://github.com/user-attachments/assets/1bc64853-750f-47a8-9eec-7fa230b17f37)
   - ![image](https://github.com/user-attachments/assets/fa8bfd83-e6bf-47c3-ab53-8e8525383cdb)



8. **Custom Query Execution**:
   - Execute complex queries including windows, OLAP, and aggregate functions.
   - ![image](https://github.com/user-attachments/assets/edeb9684-1715-48e3-baa6-09d2c50d47fd)
   - ![image](https://github.com/user-attachments/assets/904d157b-a36e-4b2c-99cd-887c1fa12f58)

   ![image](https://github.com/user-attachments/assets/4e1d1b59-db83-4c18-9b9a-425e1cc3d8bf)

   ![image](https://github.com/user-attachments/assets/e6a8e141-baf6-4959-a46c-a09f17462ad5)

   ![image](https://github.com/user-attachments/assets/fdc6a970-a66e-4a38-a43c-b399daff5176)


## Advanced SQL Queries Implemented

1. **Performance Analysis**:
   - Running total points for teams using OLAP functions.
   
2. **Points Table and Rankings**:
   - Display team rankings based on total points, wins, losses, and draws with ranking per group.

3. **Group-Wise Win Analysis**:
   - Percentile rank calculation for teams' wins within their group.

4. **Stadium Match Analysis**:
   - Display the number of matches played per stadium using CTE (Common Table Expression).

5. **Top Scorer Identification**:
   - Display top scorer details per team using a CTE.

6. **Disciplinary Records**:
   - List players with yellow/red cards sorted by severity.

7. **Team Performance Metrics**:
   - Calculate average yellow cards per win for each team.

## Technologies Used

- **Python**: For GUI development using Tkinter.
- **MySQL**: For database management and advanced query execution.
- **Tkinter**: For creating a user-friendly interface to interact with the database.

## Installation and Setup
![image](https://github.com/user-attachments/assets/407c13a4-92fd-4335-ba6b-c58fce277292)

1. Clone the repository.
2. Install the required Python packages:
   ```bash
   pip install mysql-connector-python
   ```
3. Update the database connection details in the code:
   ```python
   mydb = mysql.connector.connect(
       host = "localhost",
       user = "root",
       password = "your_password",
       database = "fifa_wc"
   )
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Usage

- **Connect to the Database**: Ensure MySQL is running locally and the credentials match.
- **View Databases**: Explore all databases and tables present in the server.
- **CRUD Operations**: Use the interface buttons to perform Insert, Update, Delete, and Read actions on the FIFA World Cup data.
- **Advanced Queries**: Navigate to the 'Execute Complex Query' section to run pre-defined SQL commands for analysis.

## Demo Videos

- Part 1: [Watch the Demo](https://www.loom.com/share/f36681b5c1594a61adb17a0262220df9?sid=f3c9ebfd-491a-44c5-95e3-3ea723ba3a32)
- Part 2: [Watch the Demo](https://www.loom.com/share/89562758c65444c38c62ef90af6cae85?sid=a9a11801-e3e8-4387-af1c-8aceae63851d)

## Contributors

- Ankan Mazumdar ([email](mailto:amazumdar@hawk.iit.edu))
- Ping-Chun Shih ([email](mailto:pshih@hawk.iit.edu))
- Sandra Alrifai ([email](mailto:salrifai@hawk.iit.edu))
- Shivani Shrivastav ([email](mailto:sshrivastav@hawk.iit.edu))

---
