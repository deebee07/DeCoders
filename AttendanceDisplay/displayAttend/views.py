
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
import sqlite3
from django.http import Http404



from django.utils import timezone

# Create your views here.
date=timezone.now().strftime("%Y/%m/%d")
now = timezone.now()

def home(request):
	connection = sqlite3.connect('Attendance.db')
	cursor=connection.cursor()
	
	cursor.execute('SELECT * from classMaster')
	classes=cursor.fetchall()

	cursor.execute('SELECT tableName from classToken')
	classes_tables=cursor.fetchall()
	print "date in views is "
	print date
	connection.commit()
	connection.close()


	return render_to_response("displayAttend/home.html", {'classes_list':classes,'range': range(5),'classes_tables':classes_tables,'date':date}

		)



def attend(request):
	connection = sqlite3.connect('Attendance.db')
	nowLat = timezone.now()
	cursor=connection.cursor()
	entered_class=request.GET['class']
	cursor.execute('SELECT * from classMaster where classId = ?',entered_class)
	class_tuple=cursor.fetchall()

	cursor.execute('SELECT tableName from classToken where classId = ?',entered_class)
	table_name=cursor.fetchall()[0][0]
	cursor.execute('SELECT * from studentMaster')
	students=cursor.fetchall()

	cursor.execute('SELECT studentId, time,checkouttime from '+table_name+' where dateValue = ? AND present=?',(date,"N"))
	absent_students=cursor.fetchall()
	num1=len(absent_students)
	cursor.execute('SELECT * from '+table_name)
	test=cursor.fetchall()
	print "TABLE ATTENDANCE WALIIIIIIII"
	print test

	

	cursor.execute('SELECT studentId, time,checkouttime from '+table_name+' where dateValue = ? AND present=?',(date,"Y"))
	present_students=cursor.fetchall()
	print present_students
	num2=len(present_students)
	num=num1+num2
	sendBool=0
	if num>=1:
		sendBool=1
	connection.commit()
	connection.close()
	return render_to_response("displayAttend/attend.html", {'class_tuple':class_tuple,'date':nowLat, 'table_name':table_name,'students':students,'present_students':present_students,'absent_students':absent_students,'sendBool':sendBool})


def studentAttend(request):
	entered_studentId=request.GET['studentID']
	nowLat = timezone.now()
	entered_class=request.GET['classID']
	print "BAlllllleeee"
	print entered_studentId
	print entered_class
	connection = sqlite3.connect('Attendance.db')
	cursor=connection.cursor()
	cursor.execute('SELECT tableName from classToken where classId = ?',entered_class)
	table_name=cursor.fetchall()[0][0]
	print table_name

	
	cursor.execute('SELECT studentId, present, dateValue from '+str(table_name)+' where studentId = '+str(entered_studentId))
	history=cursor.fetchall()

	print "HISIISISIAISISAIISIIDSASSAISIDIASIDISAISIIAISSAIIS"
	print history
	cursor.execute('SELECT * from classMaster where classId = '+str(entered_class))
	class_info=cursor.fetchall()
	print "CLASSS INFOOO"
	print class_info
	cursor.execute('SELECT * from studentMaster where studentId = '+str(entered_studentId))
	student_info=cursor.fetchall()
	print "S INFOOO"
	print student_info
	connection.commit()
	connection.close()
	return render_to_response("displayAttend/studentattend.html", {'history':history,'date':nowLat, 'class_info':class_info,'student_info':student_info,'range': range(3),})



'''
##################################################
FALSE PRESENTS

	cursor.execute('UPDATE '+table_name+' set present=?, time=? where studentId=9991',("Y",now))
	cursor.execute('UPDATE '+table_name+' set present=?, time=? where studentId=9992',("Y",now))
	cursor.execute('UPDATE '+table_name+' set present=?, time=? where studentId=9993',("Y",now))
	

##################################################
'''


	#'present_students':present_students,'absent_students':absent_students,