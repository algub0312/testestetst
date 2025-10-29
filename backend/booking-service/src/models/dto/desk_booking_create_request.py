from datetime import date
from uuid import UUID

from pydantic import BaseModel


class DeskBookingCreateRequest(BaseModel):
    """DTO for creating a desk booking request.

    Attributes:
        user_id (UUID): Identifier of the user making the booking.
        desk_id (UUID): Identifier of the desk to be booked.
        start_time (date): Start date of the booking.
        end_time (date): End date of the booking.

    """

    user_id: UUID
    desk_id: UUID
    start_time: date
    end_time: date
