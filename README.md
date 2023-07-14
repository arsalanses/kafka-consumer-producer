# Kafka Producer and Consumer Example

<p align="center">
    <img src="./architecture.png" alt="diagram" width="65%">
</p>

This code provides an example of how to create a Kafka producer and consumer in Python using the kafka library. The producer generates fake messages with the current date and time and sends them to a Kafka topic. The consumer reads messages from the topic, extracts the date and time from the message, transforms it to a date string in RFC 3339 format, and sends the transformed message to another Kafka topic.
```
This project uses semantic-release to automate the release process. Semantic-release analyzes commit messages to determine the appropriate version number and automatically generates changelogs and releases.
```
## Requirements
- Python 3.x
- kafka library
- A running Kafka broker

## Usage
1. Install the kafka library using pip install kafka.
2. Start the Kafka broker.
3. Run the producer using python producer.py.
4. Run the consumer using python consumer.py.

## Deployment
Included are two Kubernetes deployment files, producer-deployment-manifest.yml and consumer-deployment-manifest.yml. These files demonstrate how to deploy the Kafka producer and consumer in a Kubernetes cluster.

The files can be deployed by running the following commands:
```sh
kubectl apply -f producer-deployment-manifest.yml
kubectl apply -f consumer-deployment-manifest.yml
```

Each deployment file specifies a container image for the producer and consumer, along with environment variables for the Kafka broker address and topic. In addition, resource limits can be set for each container by specifying the resources property.

Before deploying, be sure to replace the container image names with your own image names that are available in a container registry.
