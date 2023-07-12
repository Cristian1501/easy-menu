from .views import HomeView
from django.contrib import admin
from django.urls import path, include
from menu import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path( '',HomeView.as_view(), name='home'),
    path('menu/', include('menu.urls', namespace='menu')),
    path('productos/', views.mostrar_productos, name='mostrar_productos'),

]
