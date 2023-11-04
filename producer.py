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
channel.queue_declare(queue='sms_queue')

# Генерація контактів і поміщення їх в чергу
for _ in range(20):  # згенерувати 20 контактів
    full_name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    preferred_contact_method = 'email' if fake.boolean() else 'sms'

    # Створення контакту
    contact = Contact(
        full_name=full_name,
        email=email,
        phone_number=phone_number,
        preferred_contact_method=preferred_contact_method)
    contact.save()

    # Поміщення ObjectID в чергу
    if contact.preferred_contact_method == 'email':
        channel.basic_publish(
            exchange='',
            routing_key='email_queue',
            body=json.dumps(str(contact.id)))
    else:
        channel.basic_publish(
            exchange='',
            routing_key='sms_queue',
            body=json.dumps(str(contact.id))
        )

# Закриття з'єднання
connection.close()
