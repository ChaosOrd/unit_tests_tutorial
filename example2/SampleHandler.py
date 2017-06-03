

class SampleSqsMessageHandler(object):


    def handle_message(self, message, queue):
        first_number = message['first_number']
        second_number = message['second_number']

        queue.write({
            'result': second_number + first_number
        })