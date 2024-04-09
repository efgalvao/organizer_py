from users.models import Category


class CategoryServices:
    @staticmethod
    def fetch_categories_for_user(user):
        categories = Category.objects.filter(user=user)
        return categories

    @staticmethod
    def create_category(user, params):
        category = Category.objects.create(
            name=params["name"], user_id=user.id)
        return category

    @staticmethod
    def update_category(user, params, category_id):
        category = Category.objects.get(id=category_id, user_id=user.id)
        category.name = params["name"]
        category.save()
        return category
