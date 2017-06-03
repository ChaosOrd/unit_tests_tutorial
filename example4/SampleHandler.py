from boto import sqs

NUMBER_TO_ADD = 4


class SampleSqsMessageHandler(object):

    def __init__(self):
        conn = sqs.connect_to_region("us-west-1")
        self.queue = conn.create_queue('myqueue')

    def handle_message(self, message):
        first_number = message['first_number']

        self.queue.write({
            'result': first_number + NUMBER_TO_ADD
        })