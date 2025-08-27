from django.db import models
from django.contrib.auth.models import User # Importa o modelo de usuário padrão do Django
from PIL import Image # Importa o Image para redimensionar a imagem

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

##
# Modelo - Contatos (Aula 11.02.02)
##
class ContactRequest(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    mensagem = models.TextField(verbose_name="Mensagem")
    
    # Campos de data
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    data_atualizacao = models.DateTimeField(auto_now=True, 
                    verbose_name="Enviado em")
    
    def __str__(self):
        return f"Contato de {self.name} - {self.email}"