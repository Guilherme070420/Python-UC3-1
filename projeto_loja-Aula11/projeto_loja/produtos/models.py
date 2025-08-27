# produtos/models.py (aula 10)

from django.db import models

##
# Primeira versão do model adicionado na aula 10
##
# class Produto(models.Model):
#     nome = models.CharField(max_length=100)
#     descricao = models.TextField()
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     imagem = models.ImageField(upload_to='produtos/', blank=True, null=True) # Campo para imagem

#     def __str__(self):
#         return self.nome


##
# Modelo - Categoria (Aula 11.02.02)
##
class Category(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Categoria")
    
    def __str__(self):
        return self.name


##
# Aula 11 - 11.01.01
##
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    # Campos de data
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    # Aqui está a relação! Cada produto pertence a uma categoria. (Aula 11.02.02)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,  # <-- Permite que o valor no banco de dados seja NULO
        blank=True, # <-- Permite que o campo no admin/formulários fique em branco 
        related_name="products")

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome