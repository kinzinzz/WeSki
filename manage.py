#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PJT.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


AWS_ACCESS_KEY_ID = "AKIAT43HVN7HWBV7FL6C"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "weski-s3"
DATABASE_NAME = "weski_rds"
DATABASE_PASSWORD = "1QaZxSw#4L"
DATABASE_HOST = "weski-rds.cwgh9r5qqdjc.ap-northeast-2.rds.amazonaws.com"
DEBUG = True