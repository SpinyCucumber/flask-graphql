from flask import Flask
from flask_graphql import GraphQLView
from .schema import Schema

def create_app(path='/graphql'):
    # backend = GraphQLCachedBackend(GraphQLQuiverBackend({"async_framework": "PROMISE"}))
    backend = None
    app = Flask(__name__)
    app.debug = True
    app.add_url_rule(path, view_func=GraphQLView.as_view('graphql', schema=Schema, backend=backend, graphiql=True))
    return app