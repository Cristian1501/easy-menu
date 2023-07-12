from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView,BlogDeleteView
from menu import views

app_name='menu'

urlpatterns = [
    
    path('', BlogListView.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name="delete"),
    path('productos/', views.mostrar_productos, name='mostrar_productos'),
    path('agregar_al_carrito/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
        
]
