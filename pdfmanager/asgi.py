import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multilingual_pdf_app.settings')
django.setup()

from channels.auth import AuthMiddlewareStack
# from pdfmanager.routing import websocket_urlpatterns  # if you have WebSocket routes

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),  # Uncomment if needed
})
