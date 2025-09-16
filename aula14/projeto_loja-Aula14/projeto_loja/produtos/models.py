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
class Categoria(models.Model):
    identificacao = models.CharField(max_length=100, 
        verbose_name="Identificacao", 
        help_text="Informe a identificação da categoria",
        unique=True,
    )
    
    descricao = models.TextField (
        verbose_name="Descrição",
        help_text="Informe a descrição da categoria",
        default="N/A",
    )
    
    def __str__(self):
        return self.identificacao
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

##
# Tag
##
class Protuto_Tag(models.Model):
    identificacao = models.CharField(max_length=100, 
        verbose_name="Identificacao", 
        help_text="Informe a identificação da tag",
        unique=True)
    
    descricao = models.TextField (
        verbose_name="Descrição",
        help_text="Informe a descrição da categoria",
        default="N/A",
    )
    
    def __str__(self):
        return self.identificacao
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
##
# Produto
##
class Produto(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do produto",
        help_text="Nome do produto"
        )
    
    descricao = models.TextField(
        verbose_name="Descrição",
        help_text="Descrição detalhada do produto",
        default="N/A"
        )
    
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Preço",
        help_text="Preço de venda do produto",
        default=0.0
    )
    
    estoque = models.PositiveIntegerField(
        default=0, 
        verbose_name="Qt de produtos",
        help_text="Quantidade do produto em estoque"
    )

    disponivel = models.BooleanField(        
        default=True, 
        verbose_name="Produto Disponivel",
        help_text="Indica se o produto está disponível para venda"
    )
    
    imagem = models.ImageField(
        upload_to='produtos/', 
        blank=True, 
        null=True, 
        help_text="Imagem de exibição do produto"
    )

    # Campos de data
    data_criacao = models.DateTimeField(
        verbose_name="Data de criação",
        auto_now_add=True
    )
    
    data_atualizacao = models.DateTimeField(
        verbose_name="Data de atualização",
        auto_now=True
    )
   

    # Aqui está a relação! Cada produto pertence a uma categoria. (Aula 11.02.02)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,  # <-- Permite que o valor no banco de dados seja NULO
        blank=True, # <-- Permite que o campo no admin/formulários fique em branco 
        related_name="produtos"
    )
    
    tag = models.ManyToManyField (
        Protuto_Tag,
        related_name="produto_tags"
    )
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']