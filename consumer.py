import pika
from model import Contact
import json


# Функція-заглушка для імітації відправлення email
def send_email(contact_id):
    print(f"Sending email to contact ID: {contact_id}")
    # Припустимо тут відбувається логіка відправлення email
    return True


# Callback функція для обробки повідомлення
def callback(ch, method, properties, body):
    contact_id = json.loads(body)
    if send_email(contact_id):
        # Оновлення статусу контакту після імітації відправлення email
        Contact.objects(id=contact_id).update_one(set__is_email_sent=True)
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Встановлення з'єднання з RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# Оголошення черги
channel.queue_declare(queue='email_queue')

# Підписка на чергу
channel.basic_consume(queue='email_queue',
                      on_message_callback=callback,
                      auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
