from django.contrib import admin
from .models import libro, ebook, autor, revista

# Register your models here.

admin.site.register(libro)
admin.site.register(ebook)
admin.site.register(autor)
admin.site.register(revista)

