"""
Publisher script for the Message Broker example.
This script initializes a MessagePublisher instance, which connects to a Redis server
and publishes messages to specified channels using the publish_message method.
"""
import redis

class MessagePublisher:
    def __init__(self, host, port, password):
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            password=password,
            decode_responses=True
        )

    def publish_message(self, channel, message):
        self.redis_client.publish(channel, message)

if __name__ == '__main__':
    redis_host = '87.107.104.18'
    redis_port = 6379
    redis_password = 'Sm39149'

    publisher = MessagePublisher(redis_host, redis_port, redis_password)

    # Example: Publish messages to channels
    publisher.publish_message('channel1', 'Hello from channel 1!')
    publisher.publish_message('channel2', 'Hello from channel 2!')
