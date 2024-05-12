from account.models import Transaction, AccountReport


class CreateIncomeTransaction:
    @staticmethod
    def process(params):
        transaction = Transaction.objects.create(
            account=params["account"],
            kind=params["kind"],
            value_cents=CreateIncomeTransaction.convert_to_cents(params["value_cents"]),
            date=params["date"],
            category=params["category"],
            description=params["description"],
            account_report=CreateIncomeTransaction.fetch_account_report(
                params["account"], params["date"]
            ),
        )
        return transaction

    @staticmethod
    def convert_to_cents(value):
        return int(float(value) * 100)

    @staticmethod
    def fetch_account_report(account, date):
        try:
            account_report = AccountReport.objects.get(
                account=account,
                reference=CreateIncomeTransaction.parse_reference(date),
            )
            account_report.date = date
            account_report.save()
        except AccountReport.DoesNotExist:
            account_report = AccountReport.objects.create(
                account=account,
                date=date,
                reference=CreateIncomeTransaction.parse_reference(date),
            )
        return account_report

    @staticmethod
    def parse_reference(date):
        return date.strftime("%m%y")
