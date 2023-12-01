from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.template.defaultfilters import register
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from CoderApp.models import Curso
from CoderApp.forms import CursoForm, BuscarFormCurso



class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "CoderApp/cursos_1.html"

class CursoDetalle(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "CoderApp/curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    success_url = "/CoderApp/cursos/listar"
    template_name = "CoderApp/crear_curso.html"
    fields = ["nombre", "camada"]

class CursoActualizacion(UpdateView):
    model = Curso
    success_url = "/CoderApp/cursos/listar"
    template_name = "CoderApp/crear_curso.html"
    fields = ["nombre", "camada"]

class CursoEliminar(DeleteView):
    model = Curso
    success_url = "/CoderApp/cursos/listar"
    template_name = "CoderApp/eliminar_curso.html"

def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos,
        'nombre': "Fer",
        "form": BuscarFormCurso(),
    }
    return render(request, 'CoderApp/cursos.html', contexto)

def crear_curso(request):
    curso = Curso(nombre="Java", camada=65001)
    curso.save()

    return redirect("/CoderApp/cursos.html")  # get


def crear_curso_form(request):
    if request.method == "POST":
        curso_formulario = CursoForm(request.POST)

        if curso_formulario.is_valid():
            informacion = curso_formulario.cleaned_data
            curso_crear = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso_crear.save()
            return redirect("/CoderApp/cursos/")

    curso_formulario = CursoForm()
    contexto = {
        "form": curso_formulario
    }

    return render(request, "CoderApp/crear_curso.html", contexto)

def buscar_camada(request):
    try:
       nombre = request.GET["nombre"]
       cursos = Curso.objects.filter(nombre__icontains=nombre)
       contexto = {
           "cursos": cursos,
           "nombre": "Fer",
           "form": BuscarFormCurso(),
       }

       return render(request, "CoderApp/cursos.html", contexto)

    except MultiValueDictKeyError:
        return redirect("/CoderApp/cursos/")


def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Fer"}
    return render(request, 'index.html', contexto)

