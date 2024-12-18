from importlib import import_module

from channels.generic.websocket import WebsocketConsumer
from django.conf import settings
from django.urls import re_path


def route_apps(apps_settings):
    routes = []

    for app_name in apps_settings:
        if not (settings.BASE_DIR / 'apps' / app_name / 'routes.py').exists():
            continue

        module = import_module(f'apps.{app_name}.routes')
        app_routes: list = getattr(module, 'routes', None)
        if not isinstance(app_routes, list):
            raise Exception(f'The "apps/{app_name}/routes.py" should have "routes" as a list.')

        for suffix, consumer in app_routes:
            routes.append(re_path(f'ws/{app_name}/{suffix}', consumer.as_asgi()))

    return routes


class NotFoundConsumer(WebsocketConsumer):
    async def connect(self):
        self.close()


websocket_urlpatterns = [
    *route_apps(settings.PROJECT_APPS),
    re_path(r".*", NotFoundConsumer.as_asgi()),
]
