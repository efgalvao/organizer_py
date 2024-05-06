from datetime import date
from .create_expense_transaction import CreateExpenseTransaction
from Services.transactions.create_income_transaction import CreateIncomeTransaction


class ProcessTransactionRequest:
    def __init__(self, user, params):
        self.user = user
        self.params = params

    def process(self):
        print("--- ProcessTransactionRequest", self.user, self.params)

        if self.params["kind"] == "0":
            return self.process_expense()
        elif self.params["kind"] == "1":
            return self.process_income()

    def process_expense(self):
        return CreateExpenseTransaction.process(self.params)

    def process_income(self):
        CreateIncomeTransaction.process(self.user, self.params)
