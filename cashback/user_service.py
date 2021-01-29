import bcrypt
from .database import Database
from .models import User
from dependency_injector.wiring import inject


class UserService():
    @inject
    def __init__(self, database: Database):
        self.database = database

    def get_user_by_id(self, id) -> User:
        return self.database.get_user_by_id(id)

    def get_user_by_email(self, email) -> User:
        return self.database.get_user_by_email(email)

    def count_dealers_by_cpf(self, cpf) -> int:
        return self.database.count_dealers_by_cpf(cpf)

    def validate_user(self, email, password):
        try:
            user = self.database.get_user_by_email(email)
            valid = bcrypt.checkpw(password.encode(
                "unicode_escape"), user.hashed)

            if valid:
                return user
            return False
        except:
            return False

    def save_user(self, user: User):
        returned = self.database.save_user(user)

        if returned.acknowledged:
            return

        raise RuntimeError()
