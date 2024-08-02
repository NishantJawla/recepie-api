"""
Django command to be able to wait for the database
to be available before continuing establishing
connection with database.
"""

import time
from psycopg2 import OperationalError as Psycopg2OperationalError
from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Waiting for database...')
        db_ready = False
        while not db_ready:
            try:
                self.check(databases=['default'])
                db_ready = True
            except (Psycopg2OperationalError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
