from django.contrib import admin
from .models import Post
from .models import Producto
from .models import Orden

admin.site.register(Post)
admin.site.register(Producto)
admin.site.register(Orden)

