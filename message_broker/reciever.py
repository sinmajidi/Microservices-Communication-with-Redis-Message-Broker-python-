"""
Receiver script for the Message Broker example.
This script initializes a MessageReceiver instance, which connects to a Redis server,
subscribes to specified channels using the subscribe method, and handles incoming
messages by printing them using the handle_messages method.
"""
import redis

class MessageReceiver:
    def __init__(self, host, port, password):
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            password=password,
            decode_responses=True
        )
        self.pubsub = self.redis_client.pubsub()

    def subscribe(self, channel):
        self.pubsub.subscribe(channel)

    def handle_messages(self):
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                channel = message['channel']
                data = message['data']
                print(f"Received message on channel {channel}: {data}")

if __name__ == '__main__':
    redis_host = '0.0.0.0'
    redis_port = 6379
    redis_password = '***'

    receiver = MessageReceiver(redis_host, redis_port, redis_password)

    # Example: Subscribe to channels
    receiver.subscribe('channel1')
    receiver.subscribe('channel2')

    # Wait for messages
    receiver.handle_messages()
