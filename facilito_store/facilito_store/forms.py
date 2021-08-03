
from django import forms

class FormularioRegistro(forms.Form):
    username = forms.CharField(required=True,min_length=4,max_length=10)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)