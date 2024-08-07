from django.shortcuts import render

#Importa listview para trabalhar com classes
from django.views.generic import ListView, CreateView

#Imporeta o reverse_lazy
from django.urls import reverse_lazy

#Importa o model para selecionar a tabela
from .models import Alunos


# Create your views here.
class AlunosListViews(ListView):
    model = Alunos

#Classe de cadastro
class AlunosCreateView(CreateView):
    model = Alunos

    # Quais são os campos que o usuario ira preencher
    fields = ["nome", "curso", "turma"]

    # Redireciona caso aja sucesso
    # Precisa deficnir o name  na url
    # fAZEMOS REFERENCIA ATRAVES DO NAME
    success_url = reverse_lazy('alunos_list')

