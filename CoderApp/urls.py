from django.urls import path
from CoderApp.views import show_html, crear_curso, crear_curso_form, buscar_camada, CursoList, \
    CursoDetalle, CursoCreacion, CursoActualizacion, CursoEliminar, mostrar_cursos

# CursoCreacion

urlpatterns = [
    path('show/', show_html),
    path('crear_curso/', crear_curso),
    path('curso/', crear_curso_form),
    path('cursos/', mostrar_cursos),
    path('buscar/', buscar_camada),
    path('cursos/listar/', CursoList.as_view(), name="CursoList"),
    path('curso/<int:pk>', CursoDetalle.as_view(), name="CursoDetail"),
    path('crear', CursoCreacion.as_view(), name="CursoCreate"),
    path('editar/<int:pk>', CursoActualizacion.as_view(), name="CursoEditar"),
    path('eliminar/<int:pk>', CursoEliminar.as_view(), name="CursoEliminar"),
]