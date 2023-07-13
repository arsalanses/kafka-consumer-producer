# from prometheus_client import CollectorRegistry, Counter, push_to_gateway
from kafka import KafkaProducer
from datetime import datetime
import json
import os

# messages_produced = Counter('my_kafka_app_messages_produced', 'Number of messages produced')

# def produce_message():
#     messages_produced.inc()

# registry = CollectorRegistry()

kafka_server = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
producer = KafkaProducer(bootstrap_servers=[kafka_server])

topic = os.environ.get('KAFKA_TOPIC', 'input')

message = {'date': datetime.now().isoformat()}
encoded_message = json.dumps(message).encode('utf-8')
producer.send(topic, encoded_message)
# produce_message()
# push_to_gateway('http://pushgateway:9091', job='my_kafka_app', registry=registry)
print(f"Sent message: {message}")

producer.flush()
