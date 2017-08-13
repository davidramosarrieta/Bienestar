from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = 'src.commons'
    verbose_name = "Commons"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
