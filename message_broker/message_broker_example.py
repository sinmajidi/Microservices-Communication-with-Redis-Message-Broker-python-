import redis


class MessageBroker:
    """
    Simple Python class representing a message broker using Redis as the backend.

    The MessageBroker class provides methods to publish messages to channels and
    subscribe to channels to handle incoming messages asynchronously.
    """

    def __init__(self, host, port, password):
        """
        Initialize the MessageBroker with the provided Redis connection details.

        Parameters:
        - host (str): Redis server hostname or IP address.
        - port (int): Redis server port.
        - password (str): Redis server password.
        """
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            password=password,
            decode_responses=True
        )
        self.pubsub = self.redis_client.pubsub()

    def publish_message(self, channel, message):
        """
        Publish a message to the specified channel.

        Parameters:
        - channel (str): The channel to which the message will be published.
        - message (str): The message to be published.
        """
        self.redis_client.publish(channel, message)

    def subscribe(self, channel):
        """
        Subscribe to the specified channel to handle incoming messages.

        Parameters:
        - channel (str): The channel to subscribe to.
        """
        self.pubsub.subscribe(channel)

    def handle_messages(self):
        """
        Handle incoming messages asynchronously.

        This method listens for messages on the subscribed channels and prints
        received messages along with the channel they originated from.
        """
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                channel = message['channel']
                data = message['data']
                print(f"Received message on channel {channel}: {data}")


if __name__ == '__main__':
    # Redis server details
    redis_host = '87.107.104.18'
    redis_port = 6379
    redis_password = 'Sm39149'

    # Create a MessageBroker instance
    broker = MessageBroker(redis_host, redis_port, redis_password)

    # Example: Subscribe to channels
    broker.subscribe('channel1')
    broker.subscribe('channel2')

    # Example: Publish messages to channels
    broker.publish_message('channel1', 'Hello from channel 1!')
    broker.publish_message('channel2', 'Hello from channel 2!')

    # Wait for messages
    broker.handle_messages()
