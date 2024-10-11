# FIFA Women's World Cup Database Management System

## Project Overview

This project is a Python-based GUI application designed to manage and analyze the FIFA Women's World Cup database. The application provides CRUD (Create, Read, Update, Delete) functionality using MySQL and Tkinter for a user-friendly interface. It includes advanced SQL queries for detailed insights and analysis of the tournament data.

## Features

1. **Database Connection and Details**:
   - Displays server and database information to verify successful connections.
   
2. **Database Management**:
   - View all databases and tables in the connected MySQL server.
   - Read records from a specified table.

3. **CRUD Operations**:
   - **Insert Records**: Add new entries into the database.
   - **Update Records**: Modify existing records based on user queries.
   - **Delete Records**: Remove records using specified conditions.

4. **Custom Query Execution**:
   - Execute complex queries including windows, OLAP, and aggregate functions.

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

- Part 1: [Watch the Demo](path_to_video_part1)
- Part 2: [Watch the Demo](path_to_video_part2)

## Contributors

- Ankan Mazumdar ([email](mailto:amazumdar@hawk.iit.edu))
- Ping-Chun Shih ([email](mailto:pshih@hawk.iit.edu))
- Sandra Alrifai ([email](mailto:salrifai@hawk.iit.edu))
- Shivani Shrivastav ([email](mailto:sshrivastav@hawk.iit.edu))

---
