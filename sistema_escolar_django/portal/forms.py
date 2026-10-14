from django import forms

from models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro','observacao','imagem',]
        #Erro encontrado:Falta das strings dos atributos preechíveis (observacao e imagem)
        #Correção: adição das strings dos atributos preechíveis (observacao e imagem)
