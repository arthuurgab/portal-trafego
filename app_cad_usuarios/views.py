from django.shortcuts import render

def cad_usuarios(request):
    return render(request, "cad_usuarios/cad_usuarios.html")
