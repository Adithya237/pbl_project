# multilingual_pdf_app/__init__.py

# Optional: Enable default app config
# Ensures the app config class in pdfmanager is used properly
default_app_config = "pdfmanager.apps.PdfmanagerConfig"

__version__ = "1.0.0"

# Optional: Trigger startup checks or logging here
import logging

logger = logging.getLogger(__name__)
logger.info("Multilingual PDF App is starting up.")
#hi bye

