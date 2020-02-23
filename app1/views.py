from django.shortcuts import render
from django.http import HttpResponse

def Dis_data1(request):
	data = '<h1>This is APP1.</h2>'
	return HttpResponse(data)