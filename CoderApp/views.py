from django.shortcuts import render
from django.http import HttpResponse
from CoderApp.models import Curso

def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos
    }
    return render(request, 'CoderApp/cursos.html', contexto)

def crear_curso(request):
    curso = Curso(nombre="Python", camada=47785)
    curso.save()
    contexto = {"curso": curso}

    return render(request, 'index.html', contexto)

def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Fer"}
    return render(request, 'index.html', contexto)
