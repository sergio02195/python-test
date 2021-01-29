
from .user_service import UserService
from .api_client import ApiClient
from .container import Container
from .order_service import OrderService
from flask import request, make_response
from dependency_injector.wiring import Provide
from flask_jwt import jwt_required
from cashback import User, Order, OrderEncoder
import json
from pymongo.errors import DuplicateKeyError


@jwt_required()
def list_order(order_service: OrderService = Provide[Container.order_service]):
    try:
        page, per_page, orders = order_service.get_orders(cpf=request.args.get(
            'cpf'), page=request.headers.get('X-page'), per_page=request.headers.get('X-per-page'))
        response = make_response(json.dumps(orders, cls=OrderEncoder))
        response.headers['Content-Type'] = 'application/json'
        response.headers['X-page'] = page
        response.headers['X-per-page'] = per_page
        return response
    except (KeyError, DuplicateKeyError) as e:
        return '', 400
    except:
        return 'oops, something went wrong!', 500


@jwt_required()
def create_order(order_service: OrderService = Provide[Container.order_service], user_service: UserService = Provide[Container.user_service]):
    try:
        body = request.get_json()
        order = (Order(body['code'], body['cpf'], body['value'],
                       body['date'])).check_status().apply_cashback()

        count = user_service.count_dealers_by_cpf(order.cpf)

        if count > 0:
            order_service.save_order(order)
            return '', 201

        return '', 400

    except (KeyError, DuplicateKeyError) as e:
        return '', 400
    except:
        return 'oops, something went wrong!', 500


@jwt_required()
def create_user(user_service: UserService = Provide[Container.user_service]):
    try:
        body = request.get_json()
        user = User(body['email'], body['password'],
                    body['cpf'], body['full_name'])
        user_service.save_user(user)

        return '', 201
    except (KeyError, DuplicateKeyError) as e:
        return '', 400
    except:
        return 'oops, something went wrong!', 500


@jwt_required()
def get_all_cacheback(api_client: ApiClient = Provide[Container.api_client]):

    cpf = request.args.get('cpf')

    if not cpf:
        return 'cpf necessario', 400

    return api_client.get_cashback(cpf).json()
