from django.apps import AppConfig


class APIConfig(AppConfig):
    name = 'src.api'
    verbose_name = "API"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
