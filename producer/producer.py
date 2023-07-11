from kafka import KafkaProducer
from datetime import datetime
import json
import time
import os

kafka_server = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
producer = KafkaProducer(bootstrap_servers=[kafka_server])

topic = os.environ.get('KAFKA_TOPIC', 'input')

while True:
    message = {'date': datetime.now().isoformat()}
    encoded_message = json.dumps(message).encode('utf-8')
    producer.send(topic, encoded_message)
    print(f"Sent message: {message}")

    time.sleep(2)

# producer.flush()
