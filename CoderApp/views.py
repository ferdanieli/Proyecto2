from django.shortcuts import render
from django.http import HttpResponse
from CoderApp.models import Curso

def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos
    }
    return render(request, 'CoderApp/cursos.html', contexto )

def crear_curso(request):
    curso = Curso(nombre="Python", camada=23800)
    curso.save()

    # return redirect("/app/cursos/") # get

def show_html(request):
    contexto = {}
    return render(request, 'index.html', contexto)
