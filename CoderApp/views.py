from django.shortcuts import render, redirect
from CoderApp.models import Curso
from CoderApp.forms import CursoForm


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

    return redirect("/CoderApp/cursos/")  # get


def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Fer"}
    return render(request, 'index.html', contexto)


def crear_curso_form(request):
    if request.method == "POST":
        curso_formulario = CursoForm(request.POST)

        if curso_formulario.is_valid():
            informacion = curso_formulario.cleaned_data
            curso_crear = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso_crear.save()
            return redirect("/CoderApp/cursos")

    curso_formulario = CursoForm()
    contexto = {
        "form": curso_formulario
    }

    return render(request, "CoderApp/crear_curso.html", contexto)
