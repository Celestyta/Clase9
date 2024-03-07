from django.shortcuts import render
from .models import Usuario

def crear_usuario(request):
    nuevo_usuario = Usuario(nombre="Juan", apellido="Perez", email="juanperez@example.com")
    nuevo_usuario.save()
    return render(request, 'resultado.html', {'usuario': nuevo_usuario})