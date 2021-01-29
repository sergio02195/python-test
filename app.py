from flask import Flask
from flask_jwt import JWT
from cashback import Container, routes, auth
import yaml


container = Container()
container.config.from_yaml('config.yml')
container.wire(modules=[routes, auth])

with open('config.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

app = Flask(__name__)
app.container = container
app.config['SECRET_KEY'] = config['jwt_secret_key']

jwt = JWT(app, auth.authenticate, auth.identity)

app.add_url_rule('/dealer', 'dealer',
                 view_func=routes.create_user, methods=['POST'])
app.add_url_rule('/order', 'order',
                 view_func=routes.create_order, methods=['POST'])
app.add_url_rule('/order', view_func=routes.list_order)
app.add_url_rule('/cashback', view_func=routes.get_all_cacheback)
