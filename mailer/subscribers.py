"""Zarządzanie listą subskrybentów."""

from mailer.validators import EmailValidator

class DuplicateSubscriberError(Exception):
    """Zgłaszany, gdy subskrybent już istnieje na liście."""

class SubscriberManager:
    """Przechowuje i zarządza listą subskrybentów newslettera."""

    def __init__(self) -> None:
        """Zainicjuj pustą listę subskrybentów."""
        self._subscribers: list[str] = []

    def add(self, email: str) -> None:
        """Dodaj subskrybenta do listy.

        Args:
            email: Adres email subskrybenta.

        Raises:
            ValueError: Jeśli adres email ma niepoprawny format.
            DuplicateSubscriberError: Jeśli email już jest na liście.
        """
        if not EmailValidator.validate(email):
            raise ValueError(f"Niepoprawny adres email: {email}")
        if email in self._subscribers:
            raise DuplicateSubscriberError(f"Email już zapisany: {email}")
        self._subscribers.append(email)

    def remove(self, email: str) -> bool:
        """Usuń subskrybenta z listy.

        Args:
            email: Adres email do usunięcia.

        Returns:
            True, jeśli subskrybent istniał i został usunięty, False w przeciwnym razie.
        """
        if email in self._subscribers:
            self._subscribers.remove(email)
            return True
        return False

    def list_all(self) -> list[str]:
        """Zwróć listę wszystkich subskrybentów.

        Returns:
            Kopia listy adresów email subskrybentów.
        """
        return list(self._subscribers)