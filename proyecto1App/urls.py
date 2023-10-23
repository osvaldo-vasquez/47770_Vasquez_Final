from django.urls import path
from proyecto1App import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.inicio, name = "Inicio"),
    path('buscarLibro/', views.buscarLibro, name = "buscarLibro"),
    path('buscar/', views.buscar),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='proyecto1App/logout.html'), name='Logout'),

]

urlpatterns += [
    #LIBROS
    path('libros/lista/', views.LibroListView.as_view(), name = "List"),
    path('libros/detalle/<int:pk>/', views.LibroDetail.as_view(), name = "Detail"),
    path('libros/nuevo/', views.LibroCreateView.as_view(), name = "New"),
    path('libros/editar/<int:pk>', views.LibroUpdateView.as_view(), name = "Edit"),
    path('libros/eliminar/<int:pk>', views.LibroDeleteView.as_view(), name = "Delete"),
    #REVISTAS
    path('revista/lista/', views.RevistaListView.as_view(), name = "ListRevista"),
    path('revista/detalle/<int:pk>/', views.RevistaDetail.as_view(), name = "DetailRevista"),
    path('revista/nuevo/', views.RevistaCreateView.as_view(), name = "NewRevista"),
    path('revista/editar/<int:pk>', views.RevistaUpdateView.as_view(), name = "EditRevista"),
    path('revista/eliminar/<int:pk>', views.RevistaDeleteView.as_view(), name = "DeleteRevista"),
    #AUTORES
    path('autor/lista/', views.AutorListView.as_view(), name = "ListAutor"),
    path('autor/detalle/<int:pk>/', views.AutorDetail.as_view(), name = "DetailAutor"),
    path('autor/nuevo/', views.AutorCreateView.as_view(), name = "NewAutor"),
    path('autor/editar/<int:pk>', views.AutorUpdateView.as_view(), name = "EditAutor"),
    path('autor/eliminar/<int:pk>', views.AutorDeleteView.as_view(), name = "DeleteAutor"),
    ]
