# produtos/models.py (aula 10)

from django.db import models

##
# Primeira versão do model adicionado na aula 10
##
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True) # Campo para imagem
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome