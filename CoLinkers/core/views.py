from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'core/home.html')

def about(request):
	return render(request, 'core/about.html')

def events(request):
	return render(request, 'core/events.html')

def gallery(request):
	return render(request, 'core/gallery.html')

def contact(request):
	return render(request, 'core/contact.html')

def signup(request):
	return render(request, 'core/signup.html')