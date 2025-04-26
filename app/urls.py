from django.urls import path, include
from .views import ClienteCreateView, ClienteListView, ClienteUpdateView

urlpatterns = [
    path('form_clientes/', ClienteCreateView.as_view()),
    # Add other URL patterns here as needed
    path('lista_clientes/', ClienteListView.as_view(), name='lista_clientes'),
    path('form_clientes/<int:pk>/', ClienteUpdateView.as_view()),
]