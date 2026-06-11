"""Contact package initialization."""

# Importing contact Types:
from .address import Address
from .e_mail_address import EmailAddress
from .organization import Organization
from .person_number import PersonNumber
from .person import Person
from .phone_number import PhoneNumber

__all__ = [
    "Address",
    "EmailAddress",
    "Organization",
    "PersonNumber",
    "Person",
    "PhoneNumber",
    ]  # Public API of the Contact package
__author__ = ["Christian Schinkel"]  # Authors of the Contact package
__version__ = "0.0.1"  # Version of the Contact package
