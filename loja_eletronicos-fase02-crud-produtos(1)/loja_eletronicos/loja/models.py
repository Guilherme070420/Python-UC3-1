import os
from PIL import Image
from django.db import models

# Importa o modelo de usuário padrão do Django
from django.contrib.auth.models import User 
from estoque.models import Categoria, Protuto_Tag, Produto

# Importa o Image para redimensionar a imagem
from PIL import Image      

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imagens_perfil', default='perfil_padrao.jpg')

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Salva a imagem primeiro

        if self.imagem and os.path.exists(self.imagem.path):
            img = Image.open(self.imagem.path)

class Comentario(models.Model):
    
    produto = models.ForeignKey(
        Produto, 
        on_delete=models.CASCADE, 
        related_name='comentarios'
    )

    autor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comentarios'
    )

    texto = models.TextField()

    data_publicacao = models.DateTimeField(auto_now_add=True)

    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return f'Comentário de {self.autor.username} em {self.produto.nome}'

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
        ordering = ['-data_publicacao']