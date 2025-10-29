from datetime import date
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel

from src.models.dto.desk_booking_create_request import DeskBookingCreateRequest


class DeskBooking(SQLModel, table=True):
    """Database model for a desk booking.

    Attributes:
        id (UUID): Unique identifier for the desk booking.
        user_id (UUID): Identifier of the user who made the booking.
        desk_id (UUID): Identifier of the desk being booked.
        start_time (date): Start date of the booking.
        end_time (date): End date of the booking.

    """

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    user_id: UUID
    desk_id: UUID
    start_time: date
    end_time: date

    @classmethod
    def from_dto(cls, dto: DeskBookingCreateRequest) -> "DeskBooking":
        """Create a DeskBooking instance from a DeskBookingCreateRequest DTO.

        Args:
            dto (DeskBookingCreateRequest): The DTO containing booking details.

        Returns:
            DeskBooking: The created DeskBooking instance.

        """
        return cls(
            user_id=dto.user_id,
            desk_id=dto.desk_id,
            start_time=dto.start_time,
            end_time=dto.end_time,
        )
