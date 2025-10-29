from src.messaging.messaging_manager import MessagingManager
from src.models.db.desk_booking import DeskBooking
from src.models.dto.desk_booking_create_request import DeskBookingCreateRequest
from src.models.dto.desk_booking_create_response import DeskBookingCreateResponse
from src.repositories.booking_repository import DeskBookingRepository


class DeskBookingService:
    """Service for managing desk bookings."""

    def __init__(
        self,
        repo: DeskBookingRepository,
        messaging: MessagingManager,
    ) -> None:
        """Initialize the DeskBookingService.

        Args:
            repo (DeskBookingRepository): The repository for desk bookings.
            messaging (MessagingManager): The messaging manager for handling messages.

        """
        self._repo = repo
        self._messaging = messaging

    async def create_booking(
        self, request: DeskBookingCreateRequest
    ) -> DeskBookingCreateResponse:
        """Create a new desk booking.

        Args:
            request (DeskBookingCreateRequest): The request DTO containing booking details.

        Returns:
            DeskBookingCreateResponse: The response DTO containing created booking details.

        """  # noqa: E501
        booking = self._repo.create(DeskBooking.from_dto(request))
        return DeskBookingCreateResponse.from_entity(booking)

    async def list_bookings(self) -> list[DeskBookingCreateResponse]:
        """List all desk bookings.

        Returns:
            list[DeskBookingCreateResponse]: A list of all desk bookings.

        """
        bookings = self._repo.get_all()
        return [DeskBookingCreateResponse.from_entity(booking) for booking in bookings]
