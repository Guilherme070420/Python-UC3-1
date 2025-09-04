from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django
from PIL import Image  # Para redimensionar a imagem

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(default='perfil_padrao.jpg', upload_to='imagens_perfil')

    email = models.EmailField(
        verbose_name="Email",
        blank=True, 
        null=True)
    
    cpf = models.CharField(
        max_length=14, 
        verbose_name="CPF", 
        blank=True, 
        null=True)
    
    telefone = models.CharField(
        max_length=15, 
        verbose_name="Telefone", 
        blank=True, 
        null=True)
    
    dt_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        blank=True,
        null=True)

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Prefiro não dizer'),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=True, null=True)

    desafio_pergunta = models.CharField(max_length=255, verbose_name="Pergunta de segurança", blank=True, null=True)
    desafio_resposta = models.CharField(max_length=255, verbose_name="Resposta de segurança", blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.imagem.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.imagem.path)
