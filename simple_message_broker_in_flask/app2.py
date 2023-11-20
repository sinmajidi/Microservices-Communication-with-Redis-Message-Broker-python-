# Asynchronous Message Receiver using Flask and Redis

# Import necessary libraries
import threading
from flask import Flask, jsonify
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD
from redis import Redis

# Create a Flask application
app = Flask(__name__)

# Connect to Redis using the provided configuration
redis_client = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True
)


# Define a route to receive messages
@app.route('/receive_message', methods=['GET'])
def receive_message():
    # Retrieve the received message from Redis
    message = redis_client.get('received_message')

    # Check if a message is available
    if message:
        # If a message is present, delete it from Redis and respond with the message
        redis_client.delete('received_message')
        return jsonify({'received_message': message})
    else:
        # If no message is available, respond with a notification
        return jsonify({"message": "There isn't any message"})

# Define a function to handle incoming messages asynchronously
def handle_messages():
    # Subscribe to the 'message_channel' in Redis
    pubsub = redis_client.pubsub()
    pubsub.subscribe('message_channel')

    # Listen for incoming messages
    for message in pubsub.listen():
        if message['type'] == 'message':
            # When a message is received, store it in Redis for later retrieval
            data = message['data']
            redis_client.set('received_message', data)


# Main entry point
if __name__ == '__main__':
    # Start a background thread to handle incoming messages asynchronously
    threading.Thread(target=handle_messages, daemon=True).start()

    # Run the Flask application on port 5002 with debugging enabled
    app.run(port=5002, debug=True)
