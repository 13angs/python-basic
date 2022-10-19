import pika, sys, os, json

class Subscriber:
    def __init__(self, host) -> None:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = connection.channel()

    def on_message_callback(self, ch, method, properties, body) -> None:
        message = json.loads(body)
        print(" [x] Received %r" % message)

    def setup(self, exchange, exchange_type, queue_name, routing_key) -> None:
        self.channel.queue_declare(queue=queue_name)
        self.channel.exchange_declare(exchange=exchange, exchange_type=exchange_type)
        self.channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=routing_key)
        self.channel.basic_qos(prefetch_count=10)
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.on_message_callback, auto_ack=True)
    
    def run(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

def main():
    subscriber = Subscriber('eng-rabbitmq-management')
    subscriber.setup(exchange='hello_exchange', exchange_type='topic', queue_name='hello', routing_key='hello.pika')
    subscriber.run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)