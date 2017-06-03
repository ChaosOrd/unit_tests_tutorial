from unittest import TestCase

from mock import MagicMock

from example6_bad.Writer import CustomerDbWriter


class TestCustomerDbWriter(TestCase):

    def test_saves_customer_to_db(self):
        writer = CustomerDbWriter()
        connection_mock = MagicMock()
        cursor_mock = connection_mock.db.cursor.return_value

        writer.add_customer(connection_mock, 3, 'Test')

        cursor_mock.execute.assert_called_once_with("""
        INSERT INTO customers (id, name)
        VALUES (:customer_id, :customer_name)
        """, {'customer_id': 3, 'customer_name': 'Test'})