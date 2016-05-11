import sqlite3
import datetime
from random import randint

from django.utils import timezone
from django.conf import settings



import sys
import os
#EDIT THIS AS PER YOUR SYSTEM
sys.path.append('/Users/Deebee/Desktop/AttendanceDisplay')
sys.path.append('/Users/Deebee/Desktop/AttendanceDisplay/AttendanceDisplay')
#EDIT THIS AS PER YOUR SYSTEM

os.environ['DJANGO_SETTINGS_MODULE'] = 'AttendanceDisplay.settings'
from django.conf import settings


now = timezone.now()


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)




connection = sqlite3.connect('Attendance.db')
cursor=connection.cursor()
print

date=timezone.now().strftime("%Y/%m/%d")

print "SCRIPT RAN AT YYYY/MM/DD : "+date
print
print("***** Class IDs in San Jose State University *****")
cursor.execute('SELECT classId from classMaster')
classIds=cursor.fetchall()


classTable=["attendCmpe273","attendCmpe277","attendCmpe283"]
num=0
for element in classIds:
	tokenGenerated=random_with_N_digits(7)
	try:
		cursor.execute('INSERT INTO classToken (classId, token,tableName) VALUES (?, ?,?)',(classIds[num][0],tokenGenerated,classTable[num]))
	except sqlite3.IntegrityError as err:
		print(err)
	str1=str(classIds[num][0])
	str2=str(tokenGenerated)
	print("Class ID "+str1+" has token  "+str2+" inserted into database")
	num+=1
numOfClasses=num


print
print


print("***** Student IDs in San Jose State University *****")
cursor.execute('SELECT studentId from studentMaster')
studentIds=cursor.fetchall()
num=0
for student in studentIds:
	print(studentIds[num][0])
	try:
		cursor.execute('INSERT INTO attendCmpe273 (studentId, present, dateValue) VALUES (?,?,?)',(studentIds[num][0],'N',date))
	except sqlite3.IntegrityError as err:
		print(err)
	str1=str(studentIds[num][0])
	str2=str(tokenGenerated)
	print("Student ID "+str1+" has NOT PRESENT and " +date+" inserted into database")
	num+=1
numOfStudents=num


cursor.execute('SELECT * from classToken')
dat=cursor.fetchall()
print(dat)
print

connection.commit()
connection.close()

