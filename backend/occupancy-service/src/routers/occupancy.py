from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/occupancy", tags=["occupancy"])
_service = None
def bind_service(s): 
    global _service
    _service = s

@router.get("/")
def list_all(): return _service.all()

@router.get("/{desk_id}")
def get_one(desk_id: str):
    v = _service.get(desk_id)
    if not v: raise HTTPException(404, "desk not found or stale")
    return v
