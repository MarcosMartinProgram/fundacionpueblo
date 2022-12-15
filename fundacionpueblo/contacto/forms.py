from django import forms

class formulariocontacto(forms.Form):
    nombre=forms.CharField(label='Nombre', required=True)
    email=forms.CharField(label='e-mail', required=True)
    contenido=forms.CharField(label='Contenido', widget=forms.Textarea)