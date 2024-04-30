from account.models import Transaction


class CreateExpenseTransaction:
    @staticmethod
    def process(user, params):
        transaction = Transaction.objects.create(
            user=user,
            account=params["account"],
            kind=0,
            amount_cents=CreateExpenseTransaction.convert_to_cents(params["amount"]),
            date=params["date"],
        )
        return transaction

    @staticmethod
    def convert_to_cents(value):
        return int(float(value) * 100)
