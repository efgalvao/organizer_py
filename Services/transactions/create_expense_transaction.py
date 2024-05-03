from account.models import Transaction, AccountReport
import pdb


class CreateExpenseTransaction:
    @staticmethod
    def process(user, params):
        print("---------", params)
        # pdb.set_trace()
        transaction = Transaction.objects.create(
            account=params["account"],
            kind=0,
            value_cents=CreateExpenseTransaction.convert_to_cents(
                params["value_cents"]
            ),
            date=params["date"],
            category=params["category"],
            description=params["description"],
            account_report=CreateExpenseTransaction.fetch_account_report(
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
                reference=CreateExpenseTransaction.parse_reference(date),
            )
            account_report.date = date
            account_report.save()
        except AccountReport.DoesNotExist:
            account_report = AccountReport.objects.create(
                account=account,
                date=date,
                reference=CreateExpenseTransaction.parse_reference(date),
            )
        return account_report

    @staticmethod
    def parse_reference(date):
        return date.strftime("%m%y")
