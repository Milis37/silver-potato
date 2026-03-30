from abc import ABC, abstractmethod
from datetime import date
from typing import Optional

class Transaction(ABC):
    """Abstract base class - Abstraction pillar."""
    def __init__(self, amount: float, trans_date: Optional[date] = None,
                 description: str = "", category: str = ""):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._amount = amount
        self._date = trans_date or date.today()
        self._description = description
        self._category = category

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def date(self) -> date:
        return self._date

    @property
    def description(self) -> str:
        return self._description

    @property
    def category(self) -> str:
        return self._category

    @abstractmethod
    def get_impact(self) -> float:
        """Polymorphic method."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__} | {self._category} | {self._description} | {self._amount:.2f} | {self._date}"


class Income(Transaction):
    def get_impact(self) -> float:
        return self._amount


class Expense(Transaction):
    def get_impact(self) -> float:
        return -self._amount


class TransactionFactory:
    """Factory Method pattern."""
    @staticmethod
    def create(trans_type: str, amount: float, trans_date: Optional[date] = None,
               description: str = "", category: str = "") -> Transaction:
        if trans_type.lower() == "income":
            return Income(amount, trans_date, description, category)
        elif trans_type.lower() == "expense":
            return Expense(amount, trans_date, description, category)
        raise ValueError(f"Unknown transaction type: {trans_type}")
