from organizer.models import Account


class AccountServices:
    @staticmethod
    def fetch_accounts_for_user(user):
        accounts = Account.objects.filter(user=user)
        return accounts

    @staticmethod
    def create_account(user, params):
        print(params, AccountServices.convert_to_cents(params["balance_cents"]))
        account = Account.objects.create(
            name=params["name"],
            kind=params["kind"],
            balance_cents=AccountServices.convert_to_cents(params["balance_cents"]),
            user_id=user.id,
        )
        return account

    @staticmethod
    def convert_to_cents(value):
        return int(value * 100)

    @staticmethod
    def update_account(user, params, account_id):
        account = Account.objects.get(id=account_id)
        account.name = params["name"]
        account.kind = params["kind"]
        account.balance_cents = AccountServices.convert_to_cents(
            params["balance_cents"]
        )
        account.save()
        return account
