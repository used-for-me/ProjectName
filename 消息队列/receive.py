import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()  # type:pika.adapters.blocking_connection.BlockingChannel
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("received:%r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="hello", on_message_callback=callback)
print("wait")
channel.start_consuming()