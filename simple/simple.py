import redis

# Replace these values with your Redis server information
redis_host = '0.0.0.0'
redis_port = 6379  # Default Redis port
redis_password = "***"  # Set to None if no password is required

# Create a connection to the Redis server
redis_connection = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password,
    decode_responses=True  # Decode responses to UTF-8 for string values
)
# Test the connection by setting and retrieving a key
test_key = 'test_key'
test_value = 'Hello, Redis!'

# Set a key-value pair
redis_connection.set(test_key, test_value)

# Retrieve the value for the key
retrieved_value = redis_connection.get(test_key)

# Print the retrieved value
print(f"Value for key '{test_key}': {retrieved_value}")

# remove a key
redis_connection.delete(test_key)
# Close the connection (optional)
redis_connection.close()