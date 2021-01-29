from .models import Order
from cashback import Database


class OrderService:
    def __init__(self, database: Database):
        self.database = database

    def get_orders(self, page=None, per_page=None, cpf=None):
        model = {}
        if cpf:
            model['cpf'] = Order.clean_cpf(cpf)

        return int(page) if page else 1, int(per_page) if per_page else 10, self.database.get_orders_by_model(model, int(page) if page else 1, int(per_page) if per_page else 10)

    def save_order(self, order: Order):
        returned = self.database.save_order(order)

        if returned.acknowledged:
            return

        raise RuntimeError()
