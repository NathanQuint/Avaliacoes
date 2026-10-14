from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(
        request,
        'portal/index.html'
        #Erro encontrado: Especificação do caminho template/, redundância, afinal o "render" automaticamente procura a pasta template.
        #Correção: Exclusão da parte template/.
    )

def cadastro (request): 
    print("preciso mostrar a página cadastro.html")
    return HttpResponse ("Página de cadastro")