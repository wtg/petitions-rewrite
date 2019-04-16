from django.apps import AppConfig


class IndexConfig(AppConfig):
    name = "index"

    def ready(self):
        import index.signals
