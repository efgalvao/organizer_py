from account.models import Account


class InvestmentServices:
    @staticmethod
    def fetch_investments_for_account(account_id, user_id):
        if not InvestmentServices.account_belongs_to_user(account_id, user_id):
            return []
        investments = Account.objects.get(id=account_id).investments()
        return investments

    @staticmethod
    def account_belongs_to_user(account_id, user_id):
        account = Account.objects.get(id=account_id)
        return account.user.pk == user_id
