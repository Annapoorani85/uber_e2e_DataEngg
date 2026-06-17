from azure.eventhub import EventHubProducerClient, EventData

producer = EventHubProducerClient.from_connection_string(
    conn_str="<connection-string>",
    eventhub_name="<eventhub-name>"
)

batch = producer.create_batch()
batch.add(EventData("Hello Event Hub"))

producer.send_batch(batch)
producer.close()