from .models.order import Order
from pymongo import MongoClient
from .models import User


class Database():
    def __init__(self, connect_string: str):
        self.db = MongoClient(connect_string)

    def get_user_by_email(self, email) -> User:
        return User.from_dto(
            self.db.schema.users.find_one({'email': email})
        )

    def get_user_by_id(self, id):
        return self.db.schema.users.find_one({'_id': id})

    def save_user(self, user: User):
        return self.db.schema.users.insert_one(user.get_mongo_dto())

    def save_order(self, order: Order):
        return self.db.schema.orders.insert_one(order.get_mongo_dto())

    def count_dealers_by_cpf(self, cpf):
        results = self.db.schema.users.find({'cpf': cpf})
        return results.count(True)

    def get_orders_by_model(self, model, page, per_page):
        orders = self.db.schema.orders.find(model).sort(
            "date").skip((page-1)*per_page).limit(per_page)
        return [Order.from_dto(order) for order in orders]
