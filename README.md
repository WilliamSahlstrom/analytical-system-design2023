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
