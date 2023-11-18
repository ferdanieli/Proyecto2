from django.urls import path
from CoderApp.views import show_html, mostrar_cursos

urlpatterns = [
    path('show/', show_html),
    path('cursos/', mostrar_cursos),
]