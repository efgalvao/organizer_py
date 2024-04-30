from account.models import Transaction


class CreateIncomeTransaction:
    @staticmethod
    def process(user, params):
        transaction = Transaction.objects.create(
            user=user,
            account=params["account"],
            kind=0,
            amount_cents=CreateIncomeTransaction.convert_to_cents(params["amount"]),
            date=params["date"],
        )
        return transaction

    @staticmethod
    def convert_to_cents(value):
        return int(float(value) * 100)
