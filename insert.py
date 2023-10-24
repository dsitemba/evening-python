import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(11,'JEFF',34,'CALIFONIA',25000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(12,'ALLEN',46,'NORWAY',50000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(13,'MARK',22,'NEWYORK',67000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(14,'BRENDA',26,'KENYA',22000.00)");

conn.commit()
print("Records inserted successfully")
conn.close() #closing a database