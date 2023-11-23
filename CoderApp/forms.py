from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()


class BuscarFormCurso(forms.Form):
    nombre = forms.CharField()


