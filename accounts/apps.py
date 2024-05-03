from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = 'Gerenciamento de Contas'
    verbose_name_plural = 'Contas de Usuários' 