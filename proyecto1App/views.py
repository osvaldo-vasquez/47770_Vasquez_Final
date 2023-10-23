from django.shortcuts import render, redirect
from django.http import HttpResponse
from proyecto1App.models import libro
from proyecto1App.models import revista
from proyecto1App.models import autor
from proyecto1App.forms import libroFormulario
from proyecto1App.forms import revistaFormulario
from proyecto1App.forms import autorFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def inicio(request):
    return render(request, "proyecto1App/index.html")

def ebooks(request):
    return render(request, "proyecto1App/ebooks.html")

def buscarLibro(request):
    return render(request, "proyecto1App/buscarLibro.html")

def buscar(request):
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         buscar_libro = libro.objects.filter(nombre__icontains = nombre) # Filtra el libro que se está buscando
         return render(request, "proyecto1App/resultadosBusqueda.html", {"nombre": nombre, "Libros":buscar_libro})

    else:
         respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


################Libros Vistas################

class LibroListView(ListView):
  model = libro
  template_name = "proyecto1App/Vistas_Libros/lista.html"

class LibroDetail(DetailView):
  model = libro
  template_name = "proyecto1App/Vistas_Libros/libro_detail.html"

class LibroCreateView(CreateView):
  model = libro
  template_name = "proyecto1App/Vistas_Libros/libro_form.html"
  success_url = reverse_lazy("List")
  fields = ["nombre", "autor", "autor", "editorial", "genero", "sinopsis", "numpag", "fecha_pub", "fecha_compra", "ISBN", "formato"]

class LibroUpdateView(UpdateView):
  model = libro
  template_name = "proyecto1App/Vistas_Libros/libro_edit.html"
  success_url = reverse_lazy("List")
  fields = ["nombre", "autor", "autor", "editorial", "genero", "sinopsis", "numpag", "fecha_pub", "fecha_compra", "ISBN", "formato"]

class LibroDeleteView(DeleteView):
  model = libro
  success_url = reverse_lazy("List")
  template_name = "proyecto1App/Vistas_Libros/libro_confirm_delete.html"

################# Revista Vistas #######################

class RevistaListView(ListView):
  model = revista
  template_name = "proyecto1App/Vistas_Revistas/lista.html"

class RevistaDetail(DetailView):
  model = revista
  template_name = "proyecto1App/Vistas_Revistas/revista_detail.html"

class RevistaCreateView(CreateView):
  model = revista
  template_name = "proyecto1App/Vistas_Revistas/revista_form.html"
  success_url = reverse_lazy("List")
  fields = ["nombre", "titulo", "numero", "web", "genero", "temas", "fecha_pub", "fecha_compra", "formato"]

class RevistaUpdateView(UpdateView):
  model = revista
  template_name = "proyecto1App/Vistas_Revistas/revista_edit.html"
  success_url = reverse_lazy("List")
  fields = ["nombre", "titulo", "numero", "web", "genero", "temas", "fecha_pub", "fecha_compra", "formato"]

class RevistaDeleteView(DeleteView):
  model = revista
  success_url = reverse_lazy("List")
  template_name = "proyecto1App/Vistas_Revistas/revista_confirm_delete.html"


################# Autores Vistas #######################

class AutorListView(ListView):
  model = autor
  template_name = "proyecto1App/Vistas_Autores/lista.html"

class AutorDetail(DetailView):
  model = autor
  template_name = "proyecto1App/Vistas_Autores/autor_detail.html"

class AutorCreateView(CreateView):
  model = autor
  template_name = "proyecto1App/Vistas_Autores/autor_form.html"
  success_url = reverse_lazy("List")
  fields = ["nombre", "apellido", "email", "nacionalidad", "genero", "premios", "biografia"]

class AutorUpdateView(UpdateView):
  model = autor
  template_name = "proyecto1App/Vistas_Autores/autor_edit.html"
  success_url = reverse_lazy("List")
  fields = ["nombre", "apellido", "email", "nacionalidad", "genero", "premios", "biografia"]

class AutorDeleteView(DeleteView):
  model = autor
  success_url = reverse_lazy("List")
  template_name = "proyecto1App/Vistas_Autores/autor_confirm_delete.html"
