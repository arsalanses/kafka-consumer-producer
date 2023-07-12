from kafka import KafkaProducer
from datetime import datetime
import json
import time
import os

kafka_server = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
producer = KafkaProducer(bootstrap_servers=[kafka_server])

topic = os.environ.get('KAFKA_TOPIC', 'input')

message = {'date': datetime.now().isoformat()}
encoded_message = json.dumps(message).encode('utf-8')
producer.send(topic, encoded_message)
print(f"Sent message: {message}")

producer.flush()
