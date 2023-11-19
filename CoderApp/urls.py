from django.urls import path
from CoderApp.views import show_html, crear_curso

urlpatterns = [
    path('show/', show_html),
    path('crear_curso/', crear_curso),
]