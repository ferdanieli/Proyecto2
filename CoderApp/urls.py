from django.urls import path
from CoderApp.views import show_html, crear_curso, mostrar_cursos

urlpatterns = [
    path('show/', show_html),
    path('crear_curso/', crear_curso),
    path('cursos/', mostrar_cursos),
]