from unittest import TestCase

from mock import patch

from example4.SampleHandler import SampleSqsMessageHandler


class TestSampleHandler(TestCase):

    def setUp(self):
        super(TestSampleHandler, self).setUp()
        self._create_sqs_mock()
        self._create_number_to_add_mock()

    def _create_sqs_mock(self):
        self.sqs_patcher = patch('example4.SampleHandler.sqs')
        self.sqs_patcher.start()
        sqs_mock = self.sqs_patcher.start()
        connection_mock = sqs_mock.connect_to_region.return_value
        self.queue_mock = connection_mock.create_queue.return_value

    def _create_number_to_add_mock(self):
        self.num_to_add_patcher = patch('example4.SampleHandler.NUMBER_TO_ADD', 5)
        self.num_to_add_patcher.start()

    def tearDown(self):
        super(TestSampleHandler, self).tearDown()
        self.sqs_patcher.stop()
        self.num_to_add_patcher.stop()

    def test_attribute_mocking(self):
        handler = SampleSqsMessageHandler()

        handler.handle_message({
            'first_number': 10
        })

        self.queue_mock.write.assert_called_once_with({
            'result': 15
        })
