from account.models import Transaction, Account
from .transactions.process_transaction_request import ProcessTransactionRequest


class TransactionServices:
    @staticmethod
    def fetch_transactions_for_account(account_id, user_id):
        if not TransactionServices.account_belongs_to_user(account_id, user_id):
            return []
        transactions = Transaction.objects.filter(account_id=account_id)
        return transactions

    @staticmethod
    def create_transaction(user, params):
        # print(params, AccountServices.convert_to_cents(params["balance_cents"]))
        # account = Transaction.objects.create(
        #     name=params["name"],
        #     kind=params["kind"],
        #     balance_cents=AccountServices.convert_to_cents(params["balance_cents"]),
        #     user_id=user.id,
        # )
        transaction = ProcessTransactionRequest(user, params)
        return transaction

    # @staticmethod
    # def update_account(user, params, account_id):
    #     account = Account.objects.get(id=account_id)
    #     account.name = params["name"]
    #     account.kind = params["kind"]
    #     account.balance_cents = AccountServices.convert_to_cents(
    #         params["balance_cents"]
    #     )
    #     account.save()
    #     return account

    @staticmethod
    def account_belongs_to_user(account_id, user_id):
        account = Account.objects.get(id=account_id)
        return account.user.pk == user_id
