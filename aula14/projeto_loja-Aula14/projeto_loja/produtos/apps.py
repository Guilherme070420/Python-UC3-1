from django.apps import AppConfig

class MinhaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'minha_app'

class ProdutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtos'

class EstoqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estoque'
