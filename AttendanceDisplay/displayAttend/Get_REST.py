from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import sqlite3
import json




@api_view(['GET'])


def processTokenRequests(request,class_id):


	if request.method == 'GET':
		connection = sqlite3.connect('Attendance.db')
		cursor=connection.cursor()
		cursor.execute('SELECT token from classToken where classId = ?',class_id)
		class_tuple=cursor.fetchall()
		connection.commit()
		connection.close()
		response = []
		try:
			response.append({'token': class_tuple[0][0]})
		except:
			raise Http404

		return Response(response)



@api_view(['GET'])
def getClassCodes(request):
	if request.method == 'GET':
		connection = sqlite3.connect('Attendance.db')
		cursor=connection.cursor()
		cursor.execute('SELECT classCode from classMaster')
		class_tuples=cursor.fetchall()
		connection.commit()
		connection.close()
		response = []
		numrows = len(class_tuples)
		for x in range(numrows):
			if x==numrows-1:
				try:
					response.append({'classid': class_tuples[x][0]})
				except:
					raise Http404
			else:
				try:
					response.append({'classid': class_tuples[x][0]},)
				except:
					raise Http404
		return Response(response)
	return Response(response)
