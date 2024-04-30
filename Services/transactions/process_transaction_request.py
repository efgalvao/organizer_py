from datetime import date
from Services.transactions.create_expense_transaction import CreateExpenseTransaction
from Services.transactions.create_income_transaction import CreateIncomeTransaction


class ProcessTransactionRequest:
    def __init__(self, user, params):
        self.user = user
        self.params = params

    def process(self):
        if self.params["kind"] == 0:
            self.process_expense()
        elif self.params["kind"] == 1:
            self.process_income()

    def process_expense(self):
        CreateExpenseTransaction.process(self.user, self.params)

    def process_income(self):
        CreateIncomeTransaction.process(self.user, self.params)
