from unittest import TestCase

from example1.SampleHandler import SampleSqsMessageHandler


class TestSampleHandler(TestCase):

    def test_returns_true_if_message_ok(self):
        handler = SampleSqsMessageHandler()
        self.assertTrue(handler.validate_message({
            'project_name': 'rius',
            'session_id': 123
        }))

    def test_returns_false_if_no_project_name(self):
        handler = SampleSqsMessageHandler()
        self.assertFalse(handler.validate_message({
            'session_id': 123
        }))

    def test_returns_false_if_no_session_id(self):
        handler = SampleSqsMessageHandler()
        self.assertFalse(handler.validate_message({
            'project_name': 'rius'
        }))

    def test_raises_exception_when_non_numeric_session_id(self):
        handler = SampleSqsMessageHandler()

        self.assertRaises(TypeError, handler.validate_message, {
            'project_name': 'rius',
            'session_id': 'fghfgh'
        })