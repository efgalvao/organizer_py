from django.test import TestCase
from ..models import AccountReport, Account
from django.contrib.auth.models import User


class AccountReportTestCase(TestCase):
    def setUp(self):
        user = User.objects.create()

        account = Account.objects.create(
            name="Test Account",
            balance_cents=10000,
            user_id=user.pk,
            kind=0,
        )
        AccountReport.objects.create(
            account_id=account.pk,
            date="2021-01-01",
            reference="0121",
            account_balance_cents=10000,
            month_balance_cents=10000,
            month_incomes_cents=0,
            month_expenses_cents=0,
            month_invested_cents=0,
            month_dividends_cents=0,
        )

    def test_account_report_str(self):
        account_report = AccountReport.objects.get(reference="0121")
        self.assertEqual(str(account_report), "0121")

    def test_account_current_report(self):
        account = Account.objects.get(name="Test Account")
        account_report = account.current_report()
        self.assertEqual(account_report.reference, "0121")
