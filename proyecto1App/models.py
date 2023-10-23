from django.db import models

# Create your models here.

class libro(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=40)
    numpag = models.IntegerField()
    fecha_pub = models.DateField(default="2023-10-16")
    fecha_compra = models.DateField(default="2023-10-16")
    ISBN = models.CharField(max_length=40)
    formato_op = (
        ('ebook', 'eBook'),
        ('libro_fisico', 'Libro Físico')
    )
    formato = models.CharField(max_length=20, choices=formato_op, default='libro_fisico')
    def __str__(self):
        return f"Título: {self.nombre} - Autor: {self.autor}"

class ebook(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=40)
    numpag = models.IntegerField()
    aplicativo = models.CharField(max_length=40)
    fecha_pub = models.DateField

class autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, default = "autor@correo.com")
    nacionalidad = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    premios = models.CharField(max_length=200)
    biografia = models.CharField(max_length=200, default="Bio")
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido}"


class revista(models.Model):
    nombre = models.CharField(max_length=40)
    titulo = models.CharField(max_length=40, default="revista1")
    numero = models.IntegerField()
    web = models.CharField(max_length=40, default="página web")
    genero = models.CharField(max_length=40)
    temas = models.CharField(max_length=40)
    fecha_pub = models.DateField(default="2023-10-16")
    fecha_compra = models.DateField(default="2023-10-16")
    formato_op = (
        ('digital', 'Digital'),
        ('fisica', 'Física')
    )
    formato = models.CharField(max_length=20, choices=formato_op, default='fisica')
    def __str__(self):
        return f"Título: {self.nombre} - Autor: {self.titulo}"