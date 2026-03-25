# silver-potato
Py Kursinis

src/models/transaction.py    ← Transaction ABC + Income + Expense
src/models/service.py        ← BeautyService (composition)
src/models/staff.py          ← Staff (aggregation)
src/models/report.py         ← Report ABC + Daily/Weekly/Monthly
src/factory/transaction_factory.py  ← Factory Method pattern
src/managers/salon.py        ← BeautySalon Singleton
src/managers/file_manager.py ← CSV read/write
src/cli/menu.py              ← Terminal menus
main.py                      ← Entry point
tests/ (4 files, 48 tests)
REPORT.md                    ← Full coursework report
