from django.apps import AppConfig


class BsfappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bsfapp'

    def ready(self):
        import bsfapp.signals
