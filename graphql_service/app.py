# Imports
import os
from graphql_service.graph_ql import schema
from flask_graphql import GraphQLView
from graphql_service import app, api
from flask import Blueprint
from graphql_service.apis.user import ns as user
from graphql_service.apis.post import ns as post

app.debug = True

# Routes
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

api.add_namespace(user)
api.add_namespace(post)


if __name__ == '__main__':
    app.run()
