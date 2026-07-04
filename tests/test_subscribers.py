"""Testy zarządzania subskrybentami."""

import pytest
from mailer.subscribers import DuplicateSubscriberError, SubscriberManager

class TestSubscriberManager:
    """Testy dodawania, usuwania i listowania subskrybentów."""

    @pytest.fixture
    def manager(self) -> SubscriberManager:
        """Zwróć nowy, pusty SubscriberManager na potrzeby każdego testu."""
        return SubscriberManager()

    def test_add_subscriber(self, manager):
        """Dodanie poprawnego adresu email powinno go umieścić na liście."""
        manager.add("user@example.com")
        assert "user@example.com" in manager.list_all()

    def test_add_invalid_email_raises(self, manager):
        """Dodanie niepoprawnego adresu email powinno zgłosić ValueError."""
        with pytest.raises(ValueError):
            manager.add("invalid-email")

    def test_add_duplicate_raises(self, manager):
        """Dodanie tego samego adresu dwa razy powinno zgłosić błąd duplikatu."""
        manager.add("user@example.com")
        with pytest.raises(DuplicateSubscriberError):
            manager.add("user@example.com")

    def test_remove_subscriber(self, manager):
        """Usunięcie istniejącego subskrybenta powinno zwrócić True."""
        manager.add("user@example.com")
        assert manager.remove("user@example.com") is True
        assert "user@example.com" not in manager.list_all()

    def test_remove_nonexistent_subscriber(self, manager):
        """Usunięcie nieistniejącego subskrybenta powinno zwrócić False."""
        assert manager.remove("ghost@example.com") is False