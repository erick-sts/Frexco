from django.shortcuts import render, redirect
from controle.forms import UsuariosForm
from controle.forms import Usuarios
from django.contrib.auth.hashers import make_password

# Create your views here.

def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = UsuariosForm()
    return render(request, 'form.html', data)

def consulta(request):
    data = {}
    data['db'] = Usuarios.objects.all()
    return render(request, 'consulta.html', data)

def create(request):
    form = UsuariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    form.senha = make_password(form.senha)