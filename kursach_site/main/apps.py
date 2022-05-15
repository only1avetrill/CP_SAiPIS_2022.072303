from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


class InterstoreAppConfig(AppConfig):
    name = "main"
    verbose_name = "Выбор подрядчиков на озеленение"
