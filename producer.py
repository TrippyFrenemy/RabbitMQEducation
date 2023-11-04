from model import Contact
from faker import Faker
import pika
import json


# Генерація фейкових даних
fake = Faker()

# Встановлення з'єднання з RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Оголошення черги
channel.queue_declare(queue='email_queue')

# Генерація контактів і поміщення їх в чергу
for _ in range(10):  # згенерувати 10 контактів
    full_name = fake.name()
    email = fake.email()

    # Створення контакту
    contact = Contact(full_name=full_name, email=email)
    contact.save()

    # Поміщення ObjectID в чергу
    channel.basic_publish(exchange='',
                          routing_key='email_queue',
                          body=json.dumps(str(contact.id)))

# Закриття з'єднання
connection.close()
