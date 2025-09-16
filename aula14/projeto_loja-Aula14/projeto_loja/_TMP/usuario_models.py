from django.db import models
from django.contrib.auth.models import User
from PIL import Image

##
# Modelo Perfil de Usuário
##
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(default='perfil_padrao.jpg', upload_to='imagens_perfil')

    # Informações pessoais
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    cpf = models.CharField(max_length=14, verbose_name="CPF", blank=True, null=True)
    telefone = models.CharField(max_length=15, verbose_name="Telefone", blank=True, null=True)
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento", blank=True, null=True)

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Prefiro não dizer'),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=True, null=True)

    desafio_pergunta = models.CharField(max_length=255, verbose_name="Pergunta de segurança", blank=True, null=True)
    desafio_resposta = models.CharField(max_length=255, verbose_name="Resposta de segurança", blank=True, null=True)

    # Endereço
    cep = models.CharField(max_length=9, verbose_name="CEP", blank=True, null=True)
    bairro = models.CharField(max_length=100, verbose_name="Bairro", blank=True, null=True)
    cidade = models.CharField(max_length=100, verbose_name="Cidade", blank=True, null=True)
    estado = models.CharField(max_length=2, verbose_name="Estado", blank=True, null=True)
    numero = models.CharField(max_length=10, verbose_name="Número", blank=True, null=True)
    complemento = models.CharField(max_length=100, verbose_name="Complemento", blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.imagem:
            img = Image.open(self.imagem.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.imagem.path)

##
# Modelo Aplicação (Tag)
##
class Aplicacao(models.Model):
    tag = models.CharField(max_length=50, verbose_name="Tag")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.tag

##
# Modelo Categoria do Produto
##
class CategoriaProduto(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da Categoria")

    def __str__(self):
        return self.descricao

##
# Modelo Marca
##
class Marca(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Marca")
    descricao = models.TextField(verbose_name="Descrição da Marca", blank=True, null=True)

    def __str__(self):
        return self.nome

##
# Modelo Produto
##
class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Produto")
    descricao = models.TextField(verbose_name="Descrição")
    
    aplicacoes = models.ManyToManyField(
        Aplicacao, blank=True,
        related_name="produtos",
        verbose_name="Tags")

    marca = models.ForeignKey(
        Marca, on_delete=models.SET_NULL,
        null=True, verbose_name="Marca")
    modelo = models.CharField(
        max_length=100,
        verbose_name="Modelo",
        blank=True,
        null=True)

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço")

    imagem = models.ImageField(
        upload_to='produtos',
        blank=True,
        null=True)

    qt_estoque = models.PositiveIntegerField(
        verbose_name="Quantidade em Estoque",
        default=0)

    tamanho = models.CharField(
        max_length=50,
        verbose_name="Tamanho",
        blank=True,
         null=True)

    categoria = models.ForeignKey(
        CategoriaProduto, on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Categoria")

    def __str__(self):
        return self.nome
