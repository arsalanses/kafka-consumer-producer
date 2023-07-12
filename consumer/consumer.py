from kafka import KafkaConsumer, KafkaProducer
from datetime import datetime
import json
import os

input_topic = os.environ.get('KAFKA_TOPIC', 'input')
output_topic = os.environ.get('KAFKA_TOPIC', 'output')

kafka_server = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
producer = KafkaProducer(bootstrap_servers=[kafka_server])
consumer = KafkaConsumer(input_topic, bootstrap_servers=[kafka_server])

for message in consumer:
    message_value = json.loads(message.value.decode('utf-8'))
    print(f"message: {message_value}")
    input_date = datetime.fromisoformat(message_value['date'])
    output_date = input_date.isoformat('T') + 'Z'
    output_message = {'date': output_date}
    print(f"Transformed message: {output_message}")
    producer.send(output_topic, json.dumps(output_message).encode('utf-8'))

producer.flush()
