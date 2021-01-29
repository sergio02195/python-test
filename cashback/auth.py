from .container import Container
from .user_service import UserService
from dependency_injector.wiring import Provide, inject


@inject
def authenticate(username: str, password: str, user_service: UserService = Provide[Container.user_service]):
    return user_service.validate_user(username, password)


@inject
def identity(payload, user_service: UserService = Provide[Container.user_service]):
    email = payload['identity']
    return user_service.get_user_by_email(email)
