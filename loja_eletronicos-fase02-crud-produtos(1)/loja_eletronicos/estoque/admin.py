from django.contrib import admin

from .models import Categoria, Protuto_Tag, Produto

admin.site.register(Categoria)

admin.site.register(Protuto_Tag)

admin.site.register(Produto)