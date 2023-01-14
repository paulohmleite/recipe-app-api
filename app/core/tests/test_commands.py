"""
Test custom Django management commands.
"""

from unittest.mock import patch

from psycopg2 import OperationError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):
        """
        Test waiting for database if database ready.
        :return:
        """
        patched_check.return_value = True
        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])