"""Testy walidatora adresów email."""

import pytest
from mailer.validators import EmailValidator

class TestEmailValidator:
    """Testy formatu adresów email."""

    @pytest.mark.parametrize("email,expected", [
        ("user@example.com", True),
        ("user+tag@domain.co.uk", True),
        ("invalid@", False),
        ("@domain.com", False),
        ("user", False),
        ("", False),
    ])
    def test_email_validation(self, email, expected):
        """Sprawdź poprawność walidacji dla różnych formatów adresów."""
        assert EmailValidator.validate(email) == expected