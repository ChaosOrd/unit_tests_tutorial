from boto import sqs

from example5.ExternalAlgorithm import process_number


class SampleSqsMessageHandler(object):

    def __init__(self):
        conn = sqs.connect_to_region("us-west-1")
        self.queue = conn.create_queue('myqueue')

    def handle_message(self, message):
        first_number = message['first_number']
        second_number = message['second_number']

        self.queue.write({
            'result': process_number(first_number) + process_number(second_number)
        })
