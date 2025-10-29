from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mqtt_host: str = "mosquitto"
    mqtt_port: int = 1883
    mqtt_topic: str = "desks/+/occupancy"
    rabbitmq_url: str | None = None
    ttl_minutes: int = 30

    class Config:
        env_prefix = ""
        case_sensitive = False
