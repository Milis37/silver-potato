import csv
from typing import List
from models import Transaction, TransactionFactory
from database import DatabaseManager


class FinanceTracker:
    """Main business logic class - demonstrates Composition & Aggregation."""
    def __init__(self, db_manager: DatabaseManager):
        self._db = db_manager
        self._transactions: List[Transaction] = []
        self.load_from_db()

    def load_from_db(self):
        data = self._db.load_transactions()
        for row in data:
            trans = TransactionFactory.create(
                row['trans_type'],
                float(row['amount']),
                row['trans_date'],
                row.get('description', ''),
                row.get('category', '')
            )
            self._transactions.append(trans)

    def add_transaction(self, transaction: Transaction):
        self._transactions.append(transaction)
        self._db.insert_transaction(transaction)

    def get_total_income(self) -> float:
        return sum(t.get_impact() for t in self._transactions if isinstance(t, Income))

    def get_total_expense(self) -> float:
        return abs(sum(t.get_impact() for t in self._transactions if isinstance(t, Expense)))

    def get_profit(self) -> float:
        return sum(t.get_impact() for t in self._transactions)  # polymorphism in action

    def generate_summary(self) -> str:
        return (f"Beauty Salon Finance Summary\n"
                f"{'='*40}\n"
                f"Total Income     : {self.get_total_income():10.2f} €\n"
                f"Total Expenses   : {self.get_total_expense():10.2f} €\n"
                f"Net Profit       : {self.get_profit():10.2f} €\n"
                f"Total Transactions: {len(self._transactions)}\n")

    def export_to_csv(self, filename: str = "finance_report.csv"):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Type', 'Amount', 'Date', 'Description', 'Category', 'Impact'])
            for t in self._transactions:
                writer.writerow([t.__class__.__name__, t.amount, t.date,
                                 t.description, t.category, t.get_impact()])
        print(f"✅ Report exported to {filename}")

    def get_transactions(self):
        return self._transactions
