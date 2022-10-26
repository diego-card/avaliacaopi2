from pyclbr import Class
from django.db import models

# Create your models here.
    

class Categoria(models.Model):
    nome = models.CharField(max_length=45, null=False)

class PainelTipo(models.Model): 
    nome = models.CharField(max_length=45, null=False)

class StatusSenha(models.Model):
    nome = models.CharField(max_length=45, null=False)

class Senha(models.Model):
    senha = models.IntegerField(null=False)
    hora_data = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipo = models.ForeignKey(PainelTipo, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusSenha, on_delete=models.CASCADE)