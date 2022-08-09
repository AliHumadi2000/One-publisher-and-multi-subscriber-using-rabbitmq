from pika.exchange_type import ExchangeType
import pika

# create connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
# create channe from the connection
channel = connection.channel()
# declare exchange
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)
# declare queue , we won't give name cause each subscriber will have its name
queue = channel.queue_declare(queue='')
# bind the queue
channel.queue_bind(exchange='pubsub', queue=queue.method.queue)
def callback(ch, method, properties, body):
    print("subscriber1 Recieved %r " % body)

channel.basic_consume(
    queue=queue.method.queue, on_message_callback=callback, auto_ack=True
)
print("Waitng for message clik CTRL+C to exit")
channel.start_consuming()
