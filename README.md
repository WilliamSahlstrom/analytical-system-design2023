# Stock Exchange Data Analytics System

## Overview

We aim to build a stock exchange data analytics system with the following components:

- **Data Source:** Utilizing the MarketStack API to fetch stock data for a specified company. The data will be retrieved for a given ticker on a specified stock exchange (e.g., Microsoft Corporation, MSFT, Nasdaq Stock Exchange).

- **Data Retrieval:**
  - Historical and latest end-of-day data will be obtained.
  - Implementation of a Kafka producer to stream this data to a topic.

- **Data Processing:**
  - Utilization of a Kafka consumer to normalize the streaming data.

- **Data Storage:**
  - Storing processed data in a Cassandra database.

- **Periodic Data Update:**
  - Setting up a periodic fetch for daily latest end-of-day data from the API to append to the stored data in the Cassandra database.

- **Data Transformation and Visualization:**
  - Transforming the collected data.
  - Visualizing key metrics such as min, max, and averages.
  - Providing visualizations illustrating how the data has been moving.
  - Generating predictions based on the analyzed data.

## Getting Started

Follow the steps below to set up and run the stock exchange data analytics system:

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>

# Run the first node and keep it in the background up and running
docker run --name cassandra-1 -p 9042:9042 -d cassandra:3.7
INSTANCE1=$(docker inspect --format="{{ .NetworkSettings.IPAddress }}" cassandra-1)
echo "Instance 1: ${INSTANCE1}"

# Run the second node
docker run --name cassandra-2 -p 9043:9042 -d -e CASSANDRA_SEEDS=$INSTANCE1 cassandra:3.7
INSTANCE2=$(docker inspect --format="{{ .NetworkSettings.IPAddress }}" cassandra-2)
echo "Instance 2: ${INSTANCE2}"

# Run the third node
docker run --name cassandra-3 -p 9044:9042 -d -e CASSANDRA_SEEDS=$INSTANCE1,$INSTANCE2 cassandra:3.7
INSTANCE3=$(docker inspect --format="{{ .NetworkSettings.IPAddress }}" cassandra-3)

# Check status in ps
docker exec cassandra-3 nodetool status

# Launch cqlsh 
docker exec -it cassandra-1 cqlsh

# Create keyspace
CREATE KEYSPACE stock_data
  WITH REPLICATION = { 
   'class' : 'NetworkTopologyStrategy',
   'datacenter1' : 3 
  };

# Check keyspaces 
DESCRIBE keyspaces;

# Create table
CREATE TABLE IF NOT EXISTS stock_data.eod_data (
   symbol TEXT,
   exchange TEXT,
   date DATE,
   open DOUBLE,
   high DOUBLE,
   low DOUBLE,
   close DOUBLE,
   volume INT,
   PRIMARY KEY ((symbol, exchange), date)
   ) WITH CLUSTERING ORDER BY (date DESC);

# Show table
SELECT * FROM stock_data.eod_data;

# Kafka setup

cd C:\Kafka\bin\windows

zookeeper-server-start.bat C:\Kafka\config\zookeeper.properties

kafka-server-start.bat c:\Kafka\config\server.properties


