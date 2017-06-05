from unittest import TestCase
from mock import MagicMock

from example2.SampleHandler import SampleSqsMessageHandler


class TestSampleHandler(TestCase):

    def test_handle_writes_sum_to_queue(self):
        handler = SampleSqsMessageHandler()
        queue_mock = MagicMock()

        handler.handle_message({
            'first_number': 3,
            'second_number': 2
        }, queue_mock)

        queue_mock.write.assert_called_once_with({
            'result': 5
        })