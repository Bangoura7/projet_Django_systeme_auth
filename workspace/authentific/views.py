from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,"app/index.html" )

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        email = request.POST["email"]
        password = request.POST["password"]
        passwordl = request.POST["passwordl"]
        # Création de l'utilisateur 
        mon_user = User.objects.create(username, email, password)
        mon_user.first_name = nom
        mon_user.last_name = prenom
        mon_user.save()
        # message pour la création de compte
        messages.success(request, "Votre compte à été créer avec succès")
        return redirect('login')
    return render(request, "app/register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
    return render(request, 'app/login.html')

def logout(request):
    pass
