from uuid import UUID

from sqlmodel import Session, select

from src.models.db.desk_booking import DeskBooking


class DeskBookingRepository:
    """Repository for managing DeskBooking entities in the database."""

    def __init__(self, session: Session) -> None:
        """Initialize the repository with a database session."""
        self._session = session

    def create(self, booking: DeskBooking) -> DeskBooking:
        """Create a new DeskBooking in the database.

        Args:
            booking (DeskBooking): The DeskBooking entity to create.

        Returns:
            DeskBooking: The created DeskBooking entity with updated fields.

        """
        self._session.add(booking)
        self._session.commit()
        self._session.refresh(booking)
        return booking

    def get_by_id(self, booking_id: UUID) -> DeskBooking | None:
        """Retrieve a DeskBooking by its ID.

        Args:
            booking_id (UUID): The ID of the DeskBooking to retrieve.

        Returns:
            DeskBooking | None: The DeskBooking entity if found, else None.

        """
        return self._session.get(DeskBooking, booking_id)

    def get_all(self) -> list[DeskBooking]:
        """Retrieve all DeskBooking entities from the database.

        Returns:
            list[DeskBooking]: A list of all DeskBooking entities.

        """
        return list(self._session.exec(select(DeskBooking)).all())
