from django.shortcuts import render, HttpResponse, redirect
from .models import User as ORM
import Login.Controller.AuthCore


# Create your views here.
def Login(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            try:
                user = ORM.objects.get(username=username)
            except ORM.DoesNotExist:
                return
            if user.password == password:
                return redirect(request, '')

        return render(request, 'pages/login.html')
