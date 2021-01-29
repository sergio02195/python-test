from dependency_injector import containers, providers
from cashback import UserService, OrderService, Database, ApiClient

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    api_client = providers.Singleton(
        ApiClient,
        api_key=config.api_key,
        api_endpoint=config.api_endpoint,
    )

    database = providers.Singleton(
        Database,
        connect_string=config.connect_string
    )

    user_service = providers.Factory(
        UserService,
        database=database,
    )

    order_service = providers.Factory(
        OrderService,
        database=database,
    )