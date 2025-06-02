from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
    path('set-language/', set_language, name='set_language'),  # For switching site language
]

# URLs with i18n support (e.g., /en/, /fr/, /es/)
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('pdfmanager.urls')),  # Include your app’s routes
)

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
