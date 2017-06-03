from unittest import TestCase
from mock import MagicMock, patch

from example3.SampleHandler import SampleSqsMessageHandler


class TestSampleHandler(TestCase):

    def test_no_mocking(self):
        handler = SampleSqsMessageHandler()

        handler.handle_message({
            'first_number': 3,
            'second_number': 2
        })

    @patch('example3.SampleHandler.sqs')
    def test_decorator_mocking(self, sqs_mock):
        handler = SampleSqsMessageHandler()
        connection_mock = sqs_mock.connect_to_region.return_value
        queue_mock = connection_mock.create_queue.return_value

        handler.handle_message({
            'first_number': 3,
            'second_number': 2
        })

        queue_mock.write.assert_called_once_with({
            'result': 5
        })