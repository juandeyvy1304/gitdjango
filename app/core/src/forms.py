from django import forms
from .pqrsf import pqrsf

#creamos las clases con los formularios

class ContactForm(forms.Form):
    tipomsj = forms.ChoiceField(label="Tipo de peticion", required=True, choices=pqrsf , widget=forms.Select(attrs={'class':'form-control', 'placeholder':'escribe tu nombre'}))
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'escribe tu nombre'}))
    apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'escribe tu apellido'}))
    correo = forms.EmailField(label="Correo electronico", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'escribe tu correo electronico'}))
    mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'rows':'5', 'placeholder':'escriba tu mensaje'}))
