# Email and SMS Notification System

This project demonstrates a simple notification system that utilizes RabbitMQ for message queuing and Mongoengine for object-document mapping to MongoDB. The system simulates sending email and SMS notifications to contacts stored in a database.

## System Components

- `producer.py`: Script that generates fake contact data and queues messages in RabbitMQ for sending notifications.
- `consumer_email.py`: Script that listens for email notification requests and processes them.
- `consumer_sms.py`: Script that listens for SMS notification requests and processes them.
- `models.py`: Defines the `Contact` document schema for Mongoengine.

## Requirements

- Python 3
- RabbitMQ
- MongoDB
- Pika (RabbitMQ Python client)
- Mongoengine
- Faker (for generating fake data)

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install RabbitMQ and MongoDB and make sure they are running.
3. Install the required Python packages:
   
   ```sh
   pip install pika mongoengine faker
   ```

## Configuration
1. Ensure RabbitMQ and MongoDB services are up and running.
2. No additional configuration is needed unless your RabbitMQ or MongoDB instance requires specific connection parameters. If so, update the connection details in the scripts accordingly.

## Usage
1. Run `producer.py` to generate fake contacts and queue notification messages.
    ```sh
    python producer.py
    ```
2. Run `consumer_email.py` in a separate terminal to start listening for email notifications.
    ```sh
    python consumer_email.py
    ```    
3. Run `consumer_sms.py` in another terminal to start listening for SMS notifications.
    ```sh
    python consumer_sms.py
    ```  


## How it works
- `producer.py` creates contacts with fake data including full name, email, and phone number, then it decides whether an email or an SMS should be sent based on a random boolean value. The contact's MongoDB ObjectID is then placed into either the `email_queue` or `sms_queue` in RabbitMQ.
- `consumer_email.py` and `consumer_sms.py` listen to their respective queues. When they receive a message, they simulate sending an email or SMS by printing a statement to the console (this is where integration with actual email/SMS sending service would occur). After 'sending' the message, they update the `is_contacted` field of the corresponding `Contact` in MongoDB to `True`.