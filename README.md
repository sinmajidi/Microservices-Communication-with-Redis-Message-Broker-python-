# Microservices Communication with Redis Message Broker

This example demonstrates a simple microservices architecture using Flask, where two microservices communicate asynchronously through a Redis message broker. The microservices are implemented in `app1.py` and `app2.py`, and the Redis connection details are stored in `config.py`.

## Files

### `app1.py`

`app1.py` represents the first microservice, which sends a message to the 'message_channel' in the Redis message broker.

#### Usage:

1. Ensure that Redis is running on your localhost.
2. Set the Redis password in `config.py`.
3. Run the following command in the terminal:

   ```bash
   python app1.py
1- Access the ```bashfollowing endpoint to send a message:
    
    http://localhost:5001/send_message

### `app2.py`

app2.py represents the second microservice, which listens for messages on the 'message_channel' and updates the received message.

Usage:
1- Ensure that Redis is running on your localhost.

2 -Set the Redis password in config.py.

3- Run the following command in the terminal:


    python app2.py
Access the following endpoint to check the received message:
    
    http://localhost:5002/receive_message
    
### `config.py`
config.py stores the Redis connection details.

    # config.py
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_PASSWORD = "PASSWORD"
    
    
### How it Works
1-app1.py sends a message to the 'message_channel' in the Redis message broker.

2-app2.py listens for messages on the 'message_channel', processes them, and updates the received message.