

class SampleSqsMessageHandler(object):

    def validate_message(self, message):
        if 'project_name' not in message:
            return False
        if 'session_id' not in message:
            return False

        if not isinstance(message['session_id'], int):
            raise TypeError('Session id is not integer')

        return True
