from datetime import date
from uuid import UUID

from pydantic import BaseModel

from src.models.db.desk_booking import DeskBooking


class DeskBookingCreateResponse(BaseModel):
    """DTO for desk booking creation response.

    Attributes:
        id (UUID): Unique identifier for the desk booking.
        user_id (UUID): Identifier of the user who made the booking.
        desk_id (UUID): Identifier of the desk being booked.
        start_time (date): Start date of the booking.
        end_time (date): End date of the booking.

    """

    id: UUID
    user_id: UUID
    desk_id: UUID
    start_time: date
    end_time: date

    @classmethod
    def from_entity(cls, entity: DeskBooking) -> "DeskBookingCreateResponse":
        """Create a DeskBookingCreateResponse DTO from a DeskBooking entity.

        Args:
            entity: The DeskBooking entity.

        Returns:
            DeskBookingCreateResponse: The created DTO instance.

        """
        return cls(
            id=entity.id,
            user_id=entity.user_id,
            desk_id=entity.desk_id,
            start_time=entity.start_time,
            end_time=entity.end_time,
        )
