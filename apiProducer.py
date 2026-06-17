from fastapi import FastAPI, Request
from azure.eventhub import EventHubProducerClient, EventData
import json

app = FastAPI()

producer = EventHubProducerClient.from_connection_string(
    conn_str="<connection-string>",
    eventhub_name="<eventhub-name>"
)

@app.post("/publish")
async def publish(request: Request):
    payload = await request.json()

    batch = producer.create_batch()
    batch.add(EventData(json.dumps(payload)))

    producer.send_batch(batch)

    return {"status": "sent"}