from fastapi import FastAPI
from src.config.settings import Settings
from src.services.occupancy_service import OccupancyService
from src.messaging.mqtt_client import MQTTClient

settings = Settings()
app = FastAPI(title="Occupancy Service")

# singleton service
occupancy_service = OccupancyService(ttl_minutes=settings.ttl_minutes)

def on_mqtt_payload(data: dict):
    # validare minimă
    desk_id = data.get("desk_id")
    occ = data.get("occupied")
    ts = data.get("ts")
    source = data.get("source")
    if desk_id is None or occ is None:
        print("[MQTT] invalid payload", data); return
    occupancy_service.update(desk_id, bool(occ), ts, source)

mqtt_client = MQTTClient(settings.mqtt_host, settings.mqtt_port,
                         settings.mqtt_topic, on_mqtt_payload)

from src.routers.occupancy import router as occupancy_router, bind_service
bind_service(occupancy_service)
app.include_router(occupancy_router)

@app.on_event("startup")
def _startup():
    print("Starting occupancy service...")
    mqtt_client.start()
    print("✓ Service ready")

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "mqtt_connected": mqtt_client.connected,
        "desks_tracked": len(occupancy_service.all()),
    }
