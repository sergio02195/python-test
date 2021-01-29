import re


class Order():
    def __init__(self, code: int, cpf, value: int, date: str, status=None, cashback=None):
        self.code = code
        self.cpf = Order.clean_cpf(cpf)
        self.value = value
        self.date = date

        if status:
            self.status = status
        if cashback:
            self.cashback = cashback
            self.cashback_value = (cashback/100) * value

    def check_status(self):
        self.status = 'Em validação'

        if self.cpf == 15350946056:
            self.status = 'Aprovado'

        return self

    def clean_cpf(cpf):
        return int(re.sub(r'[^\d]+', '', str(cpf)))

    def apply_cashback(self):
        if self.value in range(0, 1001):
            self.cashback = 10
        elif self.value in range(1001, 1501):
            self.cashback = 15
        elif self.value > 1500:
            self.cashback = 20

        return self

    def from_dto(order):
        return Order(order['code'], order['cpf'], order['value'], order['date'], order['status'], order['cashback'])

    def get_mongo_dto(self):
        return {
            'code': self.code,
            'date': self.date,
            'cpf': self.cpf,
            'status': self.status,
            'value': self.value,
            'cashback': self.cashback
        }
