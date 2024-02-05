from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse


def cad_usuarios(request):
    if request.method == 'GET':
        return render(request, "cad_usuarios/cad_usuarios.html")
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirm_senha = request.POST.get('confirm_senha')

        verification_user = User.objects.filter(username=nome).first()
        if verification_user:
            message = "Já existe um usuário com esse username! Por favor escolha outro."
            messages.error(request, message)
            return render(request, 'cad_usuarios/cad_usuarios.html')
        if senha != confirm_senha:
            message = "As senhas fornecidas são diferentes."
            messages.error(request, message)
            return render(request, 'cad_usuarios/cad_usuarios.html')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        return HttpResponseRedirect(reverse('login'))

