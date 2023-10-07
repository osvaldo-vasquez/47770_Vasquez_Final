from django import forms

class libroFormulario(forms.Form):
    nombre = forms.CharField()
    autor = forms.CharField()
    editorial = forms.CharField()
    genero = forms.CharField()
    sinopsis = forms.CharField()
    numpag = forms.IntegerField()
    fecha_pub = forms.DateField()
    fecha_compra = forms.DateField()
    ISBN = forms.CharField()


