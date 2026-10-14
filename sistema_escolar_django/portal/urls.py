from django.urls import path

from portal import views

urlpatterns = [
    path('index/', views.index),
    path('cadastro/', views.cadastro),
      
        
        #erro encontrado: Dev tentou usar template inexistente
        #correção: Criamos uma view que tem um print referenciando o que deve ter naquela página .
]
