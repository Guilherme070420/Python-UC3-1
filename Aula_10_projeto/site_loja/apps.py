from django.apps import AppConfig


class SiteLojaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_loja'

    # Aula 10
    def ready(self):
        import site_loja.signals # Importa o arquivo de signals



