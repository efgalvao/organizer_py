from account.models import Transaction, Account
from .transactions.process_transaction_request import ProcessTransactionRequest
from .transactions.update_transaction import UpdateTransaction


class TransactionServices:
    @staticmethod
    def fetch_transactions_for_account(account_id, user_id):
        if not TransactionServices.account_belongs_to_user(account_id, user_id):
            return []
        transactions = Transaction.objects.filter(account_id=account_id)
        return transactions

    @staticmethod
    def create_transaction(user, params):
        transaction = ProcessTransactionRequest(user, params).process()
        return transaction

    @staticmethod
    def account_belongs_to_user(account_id, user_id):
        account = Account.objects.get(id=account_id)
        return account.user.pk == user_id

    @staticmethod
    def update_transaction(params, transaction_id):
        transaction = UpdateTransaction.update(params, transaction_id)
        return transaction
