"""Testy wysyłania emaili (z mockowanym klientem SMTP)."""

import smtplib
from unittest.mock import Mock
import pytest
from mailer.email_sender import EmailSender

class TestEmailSender:
    """Testy sukcesu i błędu przy wysyłaniu emaili."""

    @pytest.fixture
    def mock_smtp(self) -> Mock:
        """Zwróć zamockowany klient SMTP."""
        return Mock(spec=smtplib.SMTP)

    def test_send_email_to_single_subscriber(self, mock_smtp):
        """Poprawna wysyłka powinna zwrócić SendResult z success=True."""
        sender = EmailSender(smtp_client=mock_smtp)
        result = sender.send("user@example.com", "Subject", "Body")

        assert result.success
        assert mock_smtp.sendmail.called

    def test_send_email_failure(self, mock_smtp):
        """Błąd SMTP powinien zostać przechwycony i zwrócony jako SendResult."""
        mock_smtp.sendmail.side_effect = smtplib.SMTPException("connection failed")
        sender = EmailSender(smtp_client=mock_smtp)

        result = sender.send("user@example.com", "Subject", "Body")

        assert not result.success
        assert result.error is not None