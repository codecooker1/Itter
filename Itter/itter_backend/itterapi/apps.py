from django.apps import AppConfig


class ItterapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'itterapi'

    def ready(self):
        import itterapi.signals