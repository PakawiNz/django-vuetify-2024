from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import Signal

# the final signal that sent after every migrate and post_migrate is completed
post_final_migrate = Signal()


def trigger_final_migrate(sender, **kwargs):
    if isinstance(sender, MigratorConfig):
        post_final_migrate.send(sender)


class MigratorConfig(AppConfig):
    name = 'migrator'

    def ready(self):
        post_migrate.connect(trigger_final_migrate)
