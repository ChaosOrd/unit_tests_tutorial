from boto import sqs


class SampleSqsMessageHandler(object):

    def __init__(self):
        conn = sqs.connect_to_region("us-west-1")
        self.queue = conn.create_queue('myqueue')

    def handle_message(self, message):
        first_number = message['first_number']
        second_number = message['second_number']

        self.queue.write({
            'result': second_number + first_number
        })