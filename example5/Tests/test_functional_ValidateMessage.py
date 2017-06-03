from unittest import TestCase

from mock import patch

from example5.SampleHandler import SampleSqsMessageHandler


class TestSampleHandler(TestCase):

    def setUp(self):
        super(TestSampleHandler, self).setUp()
        self._create_sqs_mock()
        self._create_process_number_mock()

    def _create_process_number_mock(self):
        self.process_number_patcher = patch('example5.SampleHandler.process_number')
        self.process_number_patcher.start()
        process_number_mock = self.process_number_patcher.start()
        process_number_mock.side_effect = [3, 4]

    def _create_sqs_mock(self):
        self.sqs_patcher = patch('example5.SampleHandler.sqs')
        self.sqs_patcher.start()
        sqs_mock = self.sqs_patcher.start()
        connection_mock = sqs_mock.connect_to_region.return_value
        self.queue_mock = connection_mock.create_queue.return_value

    def tearDown(self):
        super(TestSampleHandler, self).tearDown()
        self.process_number_patcher.stop()

    def test_attribute_mocking(self):
        handler = SampleSqsMessageHandler()

        handler.handle_message({
            'first_number': 10,
            'second_number': 14
        })

        self.queue_mock.write.assert_called_once_with({
            'result': 7
        })
