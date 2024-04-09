from users.models import Financing


class FinancingServices:
    @staticmethod
    def fetch_financings_for_user(user):
        financings = Financing.objects.filter(user=user)
        return financings

    @staticmethod
    def create_financing(user, params):
        print(params)
        financing = Financing.objects.create(
            name=params["name"],
            installments=params["installments"],
            borrowed_value_cents=FinancingServices.convert_to_cents(
                params["borrowed_value_cents"]
            ),
            user_id=user.id,
        )
        return financing

    @staticmethod
    def convert_to_cents(value):
        return int(value * 100)

    # @staticmethod
    # def update_category(user, params, category_id):
    #     category = Category.objects.get(id=category_id, user_id=user.id)
    #     category.name = params["name"]
    #     category.save()
    #     return category
