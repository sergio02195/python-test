from json import JSONEncoder


class OrderEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
