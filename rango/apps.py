from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'rango'

    def ready(self):
        from . import signals