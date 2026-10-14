from django.contrib import admin
from django.urls import include, path
import portal.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(portal.urls))
    
    #Erro encontrado: Ausência do "path" que contém o include
    #Correção: Criação do "path" que contém o include. Assim, a importação da home, e suas páginas subsequenetes, foi criada.
]
