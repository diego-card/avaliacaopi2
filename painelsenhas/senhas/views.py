from django.shortcuts import render
from senhas.models import Senha


# Create your views here.
def index(request):
    data = Senha.objects.all()
    senha = {
        "senhas": data
    }
    return render(request, 'index.html', senha)

def exibir(request):
    
    data = Senha.objects.all()
    senha = {
        "senhas": data
    }
    return render(request, 'senhas.html', senha)
