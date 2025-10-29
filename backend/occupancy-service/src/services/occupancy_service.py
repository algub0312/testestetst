from datetime import datetime, timedelta

class OccupancyService:
    def __init__(self, ttl_minutes: int = 30):
        self.cache: dict[str, dict] = {}
        self.ttl = timedelta(minutes=ttl_minutes)

    def update(self, desk_id: str, occupied: bool, ts: str | None = None, source: str | None = None):
        self.cache[desk_id] = {
            "desk_id": desk_id,
            "occupied": occupied,
            "ts": ts or datetime.utcnow().isoformat() + "Z",
            "source": source or "mqtt",
            "timestamp": datetime.utcnow(),
        }

    def get(self, desk_id: str):
        v = self.cache.get(desk_id)
        if not v: return None
        if datetime.utcnow() - v["timestamp"] > self.ttl: return None
        return v

    def all(self):
        now = datetime.utcnow()
        return {k: v for k, v in self.cache.items() if now - v["timestamp"] <= self.ttl}
