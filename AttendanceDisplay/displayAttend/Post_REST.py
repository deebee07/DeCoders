from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import sqlite3
import json





'''
SAMPLE JSON for postAttendance API
{"IMEINum":"DDDDDDDDDD", "Token":2990736}
'''
dateVal=timezone.now().strftime("%Y/%m/%d")
print "DATE VAL HAI"
print dateVal

@api_view([ 'POST'])

def markAttendance(request):
	if request.method == 'POST':
		from django.utils import timezone 
		now = timezone.now()
		print type(request.body)
		j = json.loads(request.body)
		connection = sqlite3.connect('Attendance.db')
		cursor=connection.cursor()
		cursor.execute('SELECT tableName from classToken where token ='+str(j['Token']))
		try:
			table_name=cursor.fetchall()[0][0]
		except IndexError:
			return Response({'Detail': 'No such TableName in Database'})
		cursor.execute('SELECT * from classToken')
		print cursor.fetchall()
		cursor.execute('SELECT ImeiNum,studentId from studentMaster')
		imei_nums=cursor.fetchall()
		flag= False

		for row in imei_nums:
			if row[0]==j['IMEINum']:
				flag=True
				studentID=row[1]
				break

		if flag:
			cursor.execute('UPDATE '+table_name+' set present=?, time=? where studentId=? ',("Y",now,studentID))
			print "IASIIDAIDS AM HERE"
			cursor.execute('SELECT present,time from '+table_name+' where studentId= '+str(studentID))
			temp=cursor.fetchall()
			connection.commit()
			connection.close()
			return Response({'Detail': temp})
		else:
			connection.commit()
			connection.close()
			return Response({'Detail': 'No such Unique ID in Database'})
		connection.commit()
		connection.close()
	raise Http404

'''
SAMPLE JSON for postAttendance API
{"IMEINum":"DDDDDDDDDD", "Token":3032353}
'''

@api_view([ 'POST'])
def checkoutStudent(request):
	if request.method == 'POST':
		from django.utils import timezone 
		now = timezone.now()
		print type(request.body)
		j = json.loads(request.body)
		connection = sqlite3.connect('Attendance.db')
		cursor=connection.cursor()
		cursor.execute('SELECT tableName from classToken where token ='+str(j['Token']))
		try:
			table_name=cursor.fetchall()[0][0]
		except IndexError:
			return Response({'Detail': 'No such TableName in Database'})
		cursor.execute('SELECT * from classToken')
		print cursor.fetchall()
		cursor.execute('SELECT ImeiNum,studentId from studentMaster')
		imei_nums=cursor.fetchall()

		flag= False

		for row in imei_nums:
			if row[0]==j['IMEINum']:
				flag=True
				studentID=row[1]
				break

		if flag:
			print "sadaasdsadasda"
			cursor.execute('UPDATE '+table_name+' set checkouttime=? where studentId=?',(now,studentID))
			cursor.execute('SELECT present,checkouttime from '+table_name+' where studentId= '+str(studentID))
			temp=cursor.fetchall()
			connection.commit()
			connection.close()
			return Response({'Detail': temp})
		else:
			return Response({'Detail': 'No such Unique ID in Database'})		
		connection.commit()
		connection.close()
	raise Http404


'''
SAMPLE JSON for registerStudent API
{
"studentId":9991,
"IMEINum":"DDDDDDDDDD"
}
'''

@api_view([ 'POST'])
def registerStudent(request):
	if request.method == 'POST':
		j = json.loads(request.body)
		studentId= int(j['studentId'])
		connection = sqlite3.connect('Attendance.db')
		cursor=connection.cursor()
		cursor.execute('UPDATE studentMaster set ImeiNum=? where studentId=?',(j['IMEINum'],studentId))
		cursor.execute('SELECT ImeiNum from studentMaster where studentId = '+str(studentId))
		try:
			class_tuple=cursor.fetchall()[0][0]
		except IndexError:
			return Response({'Detail': 'No such Student in Database'})
		connection.commit()
		connection.close()
		return Response({'Detail': 'IMEINum Stored in the Database of the student'})
	raise Http404
