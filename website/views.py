from django.shortcuts import render
from django.core.mail import send_mail

def home (request):
	return render(request, 'home.html', {})

def blog (request):
		return render(request, 'blog.html', {})

def blogdetails (request):
	if request.method=="POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send email
		send_mail(
			message_name, #subject
			message, #message
			message_email, #from email
			['info.cinedo@gmail.com'], #to email
			fail_silently=False,
			)

		return render(request, 'blogdetails.html', {'message_name': message_name})

	else:
		#return the page 
		return render(request, 'blogdetails.html', {})

def supcreators (request):
	if request.method=="POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send email
		send_mail(
			message_name, #subject
			message, #message
			message_email, #from email
			['info.cinedo@gmail.com'], #to email
			fail_silently=False,
			)

		return render(request, 'supcreators.html', {'message_name': message_name})

	else:
		#return the page 
		return render(request, 'supcreators.html', {})

def crowdfunding (request):
	if request.method=="POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send email
		send_mail(
			message_name, #subject
			message, #message
			message_email, #from email
			['info.cinedo@gmail.com'], #to email
			fail_silently=False,
			)

		return render(request, 'crowdfunding.html', {'message_name': message_name})

	else:
		#return the page 
		return render(request, 'crowdfunding.html', {})

def crowddetails (request):
	if request.method=="POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send email
		send_mail(
			message_name, #subject
			message, #message
			message_email, #from email
			['info.cinedo@gmail.com'], #to email
			fail_silently=False,
			)

		return render(request, 'crowddetails.html', {'message_name': message_name})

	else:
		#return the page 
		return render(request, 'crowddetails.html', {})

def movies (request):
		return render(request, 'movies.html', {})

def genre (request):
		return render(request, 'genre.html', {})

def pagedetails (request):
		return render(request, 'pagedetails.html', {})

def eshop (request):
		return render(request, 'eshop.html', {})

def item (request):
		return render(request, 'item.html', {})