from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, "register.html")

# Create your views here.
def login(request):
    return render(request, "login.html")

# Create your views here.
def home(request):
    return render(request, "home.html")