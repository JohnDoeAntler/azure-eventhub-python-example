from azure.eventhub import EventHubConsumerClient
import json

def main():
    CONNECTION_STR = 'Endpoint=sb://*****************************************************************************************************************************************************'

    consumer_client = EventHubConsumerClient.from_connection_string(
        conn_str=CONNECTION_STR,
        consumer_group='$Default',
    )

    with consumer_client as c:
        print("connected")
        on_event = lambda _, message: print(message)
        # on_event = lambda _, message: print(json.loads(next(message.body))['messageID'])
        c.receive(on_event=on_event, starting_position="-1")

if __name__ == '__main__':
    main()

