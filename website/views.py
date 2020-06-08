from django.shortcuts import render
from django.core.mail import send_mail

def home (request):
	return render(request, 'website/home.html', {})

def blog (request):
		return render(request, 'website/blog.html', {})

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

		return render(request, 'website/blogdetails.html', {'message_name': message_name})

	else:
		#return the page
		return render(request, 'website/blogdetails.html', {})

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

		return render(request, 'website/supcreators.html', {'message_name': message_name})

	else:
		#return the page
		return render(request, 'website/supcreators.html', {})

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

		return render(request, 'website/crowdfunding.html', {'message_name': message_name})

	else:
		#return the page
		return render(request, 'website/crowdfunding.html', {})

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

		return render(request, 'website/crowddetails.html', {'message_name': message_name})

	else:
		#return the page
		return render(request, 'website/crowddetails.html', {})

def movies (request):
		return render(request, 'website/movies.html', {})

def genre (request):
		return render(request, 'website/genre.html', {})

def pagedetails (request):
		return render(request, 'website/pagedetails.html', {})

def eshop (request):
		return render(request, 'website/eshop.html', {})

def item (request):
		return render(request, 'website/item.html', {})
