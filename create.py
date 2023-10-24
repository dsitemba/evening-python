import sqlite3 #database

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEE(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);
''') #table creation
print("Table created successfully")

conn.close() #closing a database
