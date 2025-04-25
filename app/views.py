from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Cliente

class ClienteCreateView(CreateView):
    model = Cliente
    fields = "__all__"
    template_name = "form_cliente.html"
    success_url = reverse_lazy("lista_clientes")  # Certifique-se que na urls.py a rota tem o nome "lista_clientes"

class ClienteListView(ListView):
    model = Cliente
    template_name = "Lista_clientes.html"