import sqlite3

#connection=sqlite3.connect(':memory:')
connection = sqlite3.connect('Attendance.db')
cursor=connection.cursor()


cursor.execute('CREATE TABLE classMaster (classId INTEGER UNIQUE, classCode CHAR(10), classFaculty CHAR(20), classStrength INTEGER, RaspSn CHAR(20) )')
cursor.execute('CREATE TABLE studentMaster (studentId INTEGER UNIQUE, studentName CHAR(20),classId INTEGER, ImeiNum CHAR(20) UNIQUE DEFAULT NULL)')


cursor.execute('CREATE TABLE attendCmpe273 (studentId INTEGER, present CHAR(2), dateValue CHAR(10),time DEFAULT NULL,checkouttime DEFAULT NULL, PRIMARY KEY (studentId,dateValue))')
cursor.execute('CREATE TABLE attendCmpe277 (studentId INTEGER, present CHAR(2), dateValue CHAR(10),time DEFAULT NULL,checkouttime DEFAULT NULL, PRIMARY KEY (studentId,dateValue))')
cursor.execute('CREATE TABLE attendCmpe283 (studentId INTEGER, present CHAR(2), dateValue CHAR(10),time DEFAULT NULL,checkouttime DEFAULT NULL, PRIMARY KEY (studentId,dateValue))')


cursor.execute('CREATE TABLE classToken (classId INTEGER UNIQUE, token INTEGER UNIQUE, tableName CHAR(20))')


for t in [(1,'CMPE273','Mr. Sithu Aung',7,'000000008d0f9a33'),(2,'CMPE277','Mr. Chandrasekar Vuppalapati',10,'000000008d0f9b13'),(3,'CMPE283','Mr. Mike Larkin',14,'000000008d0a9b33')]:
    cursor.execute('insert into classMaster values (?,?,?,?,?)', t)


for stu in [(9991,'Richard',1),(9992,'Devashish',1),(9993,'Charmi',1),(9994,'Mahitha',1),(9995,'Rewant',1),(9996,'Piyush',1),(9997,'Rohan',1)]:
    cursor.execute('insert into studentMaster (studentId, studentName,classId) VALUES (?,?,?)', stu)


print("***** Classes avaliable in San Jose State University *****")
cursor.execute('SELECT * from classMaster')
data=cursor.fetchall()
print(data)

print
print("***** Students in San Jose State University *****")
cursor.execute('SELECT * from studentMaster')
data1=cursor.fetchall()
print(data1)
print

cursor.execute('SELECT * from classToken')
dat=cursor.fetchall()
print(dat)
print


print("********* Master Database of All Classes & Students in San Jose State University Created *********")
print

connection.commit()
connection.close()

print "Connection closed"

