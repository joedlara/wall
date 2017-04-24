from django.shortcuts import render, HttpResponse, redirect
from .models import Users


def index(request):

	return render(request,'wall/index.html')

def post(request):

	Users.objects.create(f_name = request.POST['f_name'], message = request.POST['message'], comment = request.POST['comment'])

	context = {
	'f_name': request.POST['f_name'],
	'message': request.POST['message'],
	}

	return render(request,'wall/result.html')
