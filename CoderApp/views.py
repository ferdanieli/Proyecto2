from django.shortcuts import render, redirect
from CoderApp.models import Curso

def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos,
        'nombre': "Fer"
    }
    return render(request, 'CoderApp/cursos.html', contexto)

def crear_curso(request):
    curso = Curso(nombre="Java", camada=65001)
    curso.save()

    return redirect("/CoderApp/cursos/") # get

def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Fer"}
    return render(request, 'index.html', contexto)
