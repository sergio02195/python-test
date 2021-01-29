import bcrypt


class User:
    def __init__(self, email, cpf, full_name, password=None, hash=None):
        self.email = email
        self.id = email
        self.cpf = cpf
        self.full_name = full_name

        if password:
            self.hashed = bcrypt.hashpw(password.encode(
                "unicode_escape"), bcrypt.gensalt())

        if hash:
            self.hashed = hash

    def from_dto(user):
        return User(user['email'], user['cpf'], user['full_name'], hash=user['password'])

    def get_mongo_dto(self):
        return {
            'email': self.email,
            'password': self.hashed,
            'cpf': self.cpf,
            'full_name': self.full_name
        }
