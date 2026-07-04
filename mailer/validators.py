"""Walidacja adresów email."""

import re

class EmailValidator:
    """Waliduje format adresu email na podstawie uproszczonego wzorca RFC 5322."""

    PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    @staticmethod
    def validate(email: str) -> bool:
        """Sprawdź, czy podany ciąg znaków jest poprawnym adresem email.

        Args:
            email: Adres email do walidacji.

        Returns:
            True, jeśli format jest poprawny, False w przeciwnym razie.
        """
        if not email or not isinstance(email, str):
            return False
        return bool(re.match(EmailValidator.PATTERN, email.strip()))