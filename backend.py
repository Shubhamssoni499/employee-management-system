import mysql.connector
import datetime
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "S1@shubhamsoniji",
    database = "employee_db"
)
print("connection Successful")
# to retrive the daata from database into python
c = mydb.cursor()
c.execute("select * from employees")
for r in c:
    # print(r[1])
    print(r)
c2 = mydb.cursor()
c2.execute("select * from attendance")
for r in c2:
    print(r)
# to insert the data from python into database 
eid = input("Enter Employee ID: ")
did = input("Enter Department ID: ")
rid = str(datetime.datetime.now())

c3 = mydb.cursor()
query = "INSERT INTO attendance(record_id, emp_id, dept_id) VALUES (%s, %s, %s)"
values = (rid, eid, did)
c3.execute(query, values)
mydb.commit()
print("Attendance Recorded Successfully")