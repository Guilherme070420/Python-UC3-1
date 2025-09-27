from django.db import models

# Importa o modelo de usuário padrão do Django
from django.contrib.auth.models import User 
from estoque.models import Categoria, Protuto_Tag, Produto

# Importa o Image para redimensionar a imagem
from PIL import Image      

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(default='perfil_padrao.jpg', upload_to='imagens_perfil')

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Salva a imagem primeiro

        img = Image.open(self.imagem.path) # Abre a imagem
        if img.height > 300 or img.width > 300: # Verifica se é maior que 300x300 pixels
            output_size = (300, 300)
            img.thumbnail(output_size) # Redimensiona a imagem
            img.save(self.imagem.path) # Salva a imagem redimensionada


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