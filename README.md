# Real Time Time Series Covid Data Streaming using Python, Docker and Kafka
This project demonstrates a real-time data streaming solution using Kafka, Docker, and Python. The goal is to aggregate and stream data in real time. Data is ingested, processed, and consumed from Kafka topics in a Dockerized environment. This project includes a Kafka producer for streaming data, a Kafka consumer for processing the data, and the use of Docker for containerization and orchestration.


## Project Overview 
- Sending data from a Kafka Producer. 
- Receiving the data through a Kafka Consumer. 
- Using Apache Kafka as the messaging backbone for the data streaming. 
- Running all components in isoaled Docker containers. 


## Dataset
The data used for this project is downloaded from Kaggle entitled "Real-time Covid 19 Data" (link: https://www.kaggle.com/datasets/gauravduttakiit/covid-19). The exact filename of the dataset used is: worldwide-aggregate.csv

## Project structure 

├── consumer
│   ├── consumer_covid_data.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yaml
├── my_tree_structure.txt
├── producer
│   ├── data
│   │   └── worldwide-aggregate.csv
│   ├── Dockerfile
│   ├── requirements.txt
│   └── stream_covid_data.py
└── README.md

## Installation
1. Clone the repository:
```bash
 git clone https://github.com/yourusername/yourproject.git
```

2. Run the containers: 
```bash
 docker-compose up --build
```
3. To stop the containers: 
```bash
docker-compose down
```