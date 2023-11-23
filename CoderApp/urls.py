from django.urls import path
from CoderApp.views import show_html, crear_curso, mostrar_cursos, crear_curso_form

urlpatterns = [
    path('show/', show_html),
    path('crear_curso/', crear_curso),
    path('curso/', crear_curso_form),
    path('cursos/', mostrar_cursos),
]