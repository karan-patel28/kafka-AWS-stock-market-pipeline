# Kafka Stock Market Data Pipeline with AWS

## Introduction
This repository contains a system for simulating stock market data production and consumption using Kafka, AWS services, and a Python-based simulation. The architecture involves a stock market app simulation producing messages that are consumed by a Kafka consumer, which in turn stores the data on Amazon S3. AWS Glue is used to catalog the data, and Amazon Athena is employed to query the dataset.

## Architecture
The system is designed to handle real-time data flow and storage efficiently. It is composed of the following components:
- **Stock Market App Simulation (Producer):** A Python script that generates simulated stock market data. 
- **Kafka:** Serves as the distributed streaming platform to handle the data pipeline.
- **Kafka Consumer:** A Python script that consumes messages from Kafka and uploads them to S3.
- **Amazon EC2:** Hosts the Kafka broker and manages the streaming data.
- **Amazon S3:** The storage service used to store the consumed messages.
- **AWS Glue:** A service that catalogues and organizes data from S3.
- **Amazon Athena:** An interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL.

## Repository Contents
- **kafka-producer.py** - This script simulates stock market data and produces messages to a Kafka topic.
- **kafka-consumer.py** - This script consumes messages from a Kafka topic and uploads them to an S3 bucket.

## Prerequisites
Before running this system, ensure you have the following:

- An AWS account with access to S3, AWS Glue, and Amazon Athena.
- A Kafka cluster with an accessible broker.
- Python 3.x with the following packages installed:
  - boto3
  - kafka-python
  - pandas

Install the required dependencies with the following command:

```bash
pip install -r requirements.txt
```

## Dataset
You can use any dataset, we are mainly interested in operation side of Data Engineering (building data pipeline)
