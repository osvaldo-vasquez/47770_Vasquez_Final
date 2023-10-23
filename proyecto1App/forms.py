from django import forms
from .models import libro
from .models import revista

class libroFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre del libro')
    autor = forms.CharField(label='Autor')
    editorial = forms.CharField(label='Editorial')
    genero = forms.CharField(label='Género')
    sinopsis = forms.CharField(label='Sinópsis')
    numpag = forms.IntegerField(label='Número de páginas')
    fecha_pub = forms.DateField(label='Fecha de publicación (mm/dd/aaaa)')
    fecha_compra = forms.DateField(label='Fecha de compra (mm/dd/aaaa)')
    ISBN = forms.CharField(label='ISBN')
    formato = forms.ChoiceField(choices=libro.formato_op, required=True, widget=forms.RadioSelect, label='Formato')

class revistaFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre de la revista')
    titulo = forms.CharField(label='Título del número')
    numero = forms.IntegerField(label='Número')
    web =  forms.CharField(label='Página web')
    genero = forms.CharField(label='Género')
    temas = forms.CharField(label='Temas')
    fecha_pub = forms.DateField(label='Fecha de publicación (mm/dd/aaaa)')
    fecha_compra = forms.DateField(label='Fecha de compra (mm/dd/aaaa)')
    formato = forms.ChoiceField(choices=revista.formato_op, required=True, widget=forms.RadioSelect, label='Formato')

class autorFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    email = forms.EmailField(label='e-mail')
    nacionalidad =  forms.CharField(label='Nacionalidad')
    genero = forms.CharField(label='Género')
    premios = forms.CharField(label='Premios')
    biografia = forms.CharField(label='Biografia')