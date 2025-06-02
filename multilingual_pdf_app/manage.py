#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging


def setup_logging():
    """Configure logging for better debugging."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def main():
    """Run administrative tasks."""
    setup_logging()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multilingual_pdf_app.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        logging.error(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH environment variable."
            " Also, check if you've activated the virtual environment."
        )
        raise ImportError("Django import failed") from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
