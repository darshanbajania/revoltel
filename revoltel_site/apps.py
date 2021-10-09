from django.apps import AppConfig


class RevoltelSiteConfig(AppConfig):
    name = 'revoltel_site'

    def ready(self):
        from . import signals