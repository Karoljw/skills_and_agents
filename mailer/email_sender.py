"""Wysyłanie wiadomości email."""

import smtplib
from dataclasses import dataclass
from email.mime.text import MIMEText

@dataclass
class SendResult:
    """Wynik próby wysłania emaila."""

    success: bool
    error: str | None = None

class EmailSender:
    """Wysyła wiadomości email przy użyciu klienta SMTP."""

    def __init__(self, smtp_client: smtplib.SMTP) -> None:
        """Zainicjuj nadawcę emaili.

        Args:
            smtp_client: Skonfigurowany klient SMTP (może być mockiem w testach).
        """
        self._smtp_client = smtp_client

    def send(self, to_address: str, subject: str, body: str) -> SendResult:
        """Wyślij wiadomość email do jednego odbiorcy.

        Args:
            to_address: Adres email odbiorcy.
            subject: Temat wiadomości.
            body: Treść wiadomości (plain text).

        Returns:
            SendResult z informacją o sukcesie lub błędzie.
        """
        message = MIMEText(body)
        message["Subject"] = subject
        message["To"] = to_address

        try:
            self._smtp_client.sendmail(
                from_addr="noreply@mailer.local",
                to_addrs=[to_address],
                msg=message.as_string(),
            )
            return SendResult(success=True)
        except smtplib.SMTPException as exc:
            return SendResult(success=False, error=str(exc))