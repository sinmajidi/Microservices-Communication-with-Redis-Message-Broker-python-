"""
Simple Flask microservice (App1) that sends a message to a Redis message broker.
This microservice initializes a Flask application and a Redis client to publish a message
to the 'message_channel' using the /send_message endpoint.
"""
from flask import Flask, jsonify
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD
from redis import Redis

app = Flask(__name__)
redis_client = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True
)

@app.route('/send_message', methods=['GET'])
def send_message():
    message = 'Hello from App1!'
    redis_client.publish('message_channel', message)
    return jsonify({'message': 'Message sent from App1'})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
