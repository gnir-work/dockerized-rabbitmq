import time
from pika import BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel 

QUEUE_NAME = "basic_channel"

def on_message_recieve(ch: BlockingChannel, method, properties, body: str):
    """
    Callback which handles one message each time.
    """
    print("Handling message...")
    time.sleep(1)
    print(f"Handled message: {body}")


def run_worker(connection: BlockingConnection):
    """
    Runs the worker after we have established a connect.
    
    :param connection: The established connection.
    """
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)

    channel.basic_consume(
        on_message_callback=on_message_recieve,
        auto_ack=True,
        queue=QUEUE_NAME
    )

    channel.start_consuming()

if __name__ == "__main__":
    while True:
        try:
            time.sleep(1)
            connection = BlockingConnection(ConnectionParameters('rabbitmq'))
            break
        except Exception:
            print("Rabbitmq is down!")
    
    run_worker(connection)
