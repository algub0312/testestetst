"""API routes for desk bookings."""

from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import get_booking_service
from src.models.dto.desk_booking_create_request import DeskBookingCreateRequest
from src.models.dto.desk_booking_create_response import DeskBookingCreateResponse
from src.services.desk_booking_service import DeskBookingService

router = APIRouter(prefix="/api/v1/bookings", tags=["bookings"])


@router.post("", status_code=201)
async def create_booking(
    request: DeskBookingCreateRequest,
    service: Annotated[DeskBookingService, Depends(get_booking_service)],
) -> DeskBookingCreateResponse:
    """Create a new desk booking.

    Args:
        request (DeskBookingCreateRequest): The booking creation request data.
        service (DeskBookingService): The desk booking service instance.

    Returns:
        DeskBookingCreateResponse: The created booking response data.

    """
    booking = await service.create_booking(request)
    return booking


@router.get("", status_code=200)
async def list_bookings(
    service: Annotated[DeskBookingService, Depends(get_booking_service)],
) -> list[DeskBookingCreateResponse]:
    """List all desk bookings.

    Args:
        service (DeskBookingService): The desk booking service instance.

    Returns:
        list[DeskBookingCreateResponse]: A list of all desk bookings.

    """
    bookings = await service.list_bookings()
    return bookings
