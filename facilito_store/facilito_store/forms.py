

from django import forms

class FormularioRegistro(forms.Form):
    
    username = forms.CharField(required=True,min_length=4,max_length=10, widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'username',
        'placeholder':'usuario'
    }))
    
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
        'class':'form-control',
        'id':'email',
        'placeholder':'correo@dominio.com'
    }))
    
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':'password',
    }))
    
