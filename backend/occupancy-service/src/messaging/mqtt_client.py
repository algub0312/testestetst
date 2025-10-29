import json, threading
import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, host: str, port: int, topic: str, on_payload):
        self.host, self.port, self.topic = host, port, topic
        self.on_payload = on_payload
        self.client = mqtt.Client(protocol=mqtt.MQTTv311)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.connected = False

    def start(self):
        self.client.connect(self.host, self.port, keepalive=60)
        t = threading.Thread(target=self.client.loop_forever, daemon=True)
        t.start()

    def _on_connect(self, client, userdata, flags, rc, properties=None):
        self.connected = (rc == 0)
        print(f"[MQTT] connected → subscribing to '{self.topic}'")
        client.subscribe(self.topic, qos=1)

    def _on_message(self, client, userdata, msg):
        try:
            print(f"[MQTT] got {msg.topic} -> {msg.payload}")
            data = json.loads(msg.payload.decode("utf-8"))
            
            if "desk_id" not in data:
                parts = msg.topic.split("/")
                if len(parts) >= 3: data["desk_id"] = parts[1]
            self.on_payload(data)
        except Exception as e:
            print(f"[MQTT] error processing message: {e}")
