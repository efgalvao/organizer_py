from account.models import Transaction


class UpdateTransaction:
    @staticmethod
    def update(params, transaction_id):
        transaction = Transaction.objects.get(id=transaction_id)
        transaction.description = params["description"]
        transaction.category = params["category"]
        transaction.save()
        return transaction
