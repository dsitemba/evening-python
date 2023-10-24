import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("UPDATE EMPLOYEE set SALARY = 80000.00 where ID=1")
conn.commit() #saving the database
cursor = conn.execute("SELECT id,name,age,address,salary from EMPlOYEE")
for row in cursor:
    print("ID =",row[0])
    print("NAME =",row[1])
    print("AGE =",row[2])
    print("ADDRESS =",row[3])
    print("SALARY =",row[4])

print("Operation done successfully")
conn.close()
