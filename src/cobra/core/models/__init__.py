"""
Model classes for the Cobra application.
"""
from .contact import person, person_number, phone_number
from .contact.organization import Organization
from .finance_types.bank import Bank
from .finance_types.bank_account import BankAccount

__all__ = [
    "Organization",
    "Bank",
    "BankAccount",
    "person",
    "person_number",
    "phone_number",
]  # Public API of the Models package
__author__ = ["Christian Schinkel"]  # Authors of the Models package
__version__ = "0.0.1"  # Version of the Models package
