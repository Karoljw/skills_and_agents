"""Prosta aplikacja Flask do zarządzania subskrybentami."""

import os
from flask import Flask, render_template, request, redirect, url_for
from mailer.subscribers import DuplicateSubscriberError, SubscriberManager

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)
subscriber_manager = SubscriberManager()

@app.route("/", methods=["GET"])
def index():
    """Wyświetl stronę główną z listą subskrybentów i formularzem zapisu."""
    return render_template("index.html", subscribers=subscriber_manager.list_all())

@app.route("/subscribe", methods=["POST"])
def subscribe():
    """Dodaj nowego subskrybenta na podstawie danych z formularza."""
    email = request.form.get("email", "")
    error = None

    try:
        subscriber_manager.add(email)
    except ValueError:
        error = "Niepoprawny format adresu email."
    except DuplicateSubscriberError:
        error = "Ten adres email jest już zapisany."

    if error:
        return render_template(
            "index.html",
            subscribers=subscriber_manager.list_all(),
            error=error,
        )
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)