# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the consumer script and the wait-for-it script into the container
COPY . /app/
#COPY ../wait-for-it.sh /app/

# Install Kafka Python library
RUN pip install --no-cache-dir -r requirements.txt

# Make the wait-for-it.sh script executable
#RUN chmod +x /app/wait-for-it.sh

# Command to wait for Kafka to be ready and then start the consumer
#CMD ["./wait-for-it.sh", "kafka:9092", "--", "python", "consumer.py"]
CMD ["python","-u" ,"consumer_covid_data.py"]