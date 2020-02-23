from django.shortcuts import render
from django.http import HttpResponse

def Dis_data2(request):
	data = '<h1>This is APP2.</h2>'
	return HttpResponse(data)