import requests


class ApiClient():
    def __init__(self, api_key: str, api_endpoint: str):
        self.api_key = api_key
        self.api_endpoint = api_endpoint

    def get_cashback(self, cpf):
        return requests.get(self.api_endpoint, params={"cpf": cpf}, headers={'token': self.api_key})
