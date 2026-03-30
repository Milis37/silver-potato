from database import DatabaseManager
from finance_tracker import FinanceTracker
from models import TransactionFactory
from datetime import date

def main():
    print("Beauty Salon Finance Tracker (OOP Coursework 2026)")

    db = DatabaseManager()
    # ← CHANGE THESE CREDENTIALS TO YOUR MySQL SERVER
    db.connect(host="localhost", user="root", password="your_password", database="beauty_salon_db")
    db.create_tables()

    tracker = FinanceTracker(db)

    while True:
        print("\n" + "="*50)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Show All Transactions")
        print("5. Export to CSV")
        print("6. Exit")
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            amt = float(input("Amount (€): "))
            desc = input("Description: ")
            cat = input("Category (e.g. Haircut, Product sale): ")
            trans = TransactionFactory.create("income", amt, description=desc, category=cat)
            tracker.add_transaction(trans)
            print("✅ Income added.")

        elif choice == "2":
            amt = float(input("Amount (€): "))
            desc = input("Description: ")
            cat = input("Category (e.g. Rent, Supplies): ")
            trans = TransactionFactory.create("expense", amt, description=desc, category=cat)
            tracker.add_transaction(trans)
            print("✅ Expense added.")

        elif choice == "3":
            print(tracker.generate_summary())

        elif choice == "4":
            for t in tracker.get_transactions():
                print(t)

        elif choice == "5":
            tracker.export_to_csv()

        elif choice == "6":
            db.close()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
