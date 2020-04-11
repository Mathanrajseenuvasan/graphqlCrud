# Imports
from graphql_service.models import User
from ..config import db
import graphene
from graphql_service.graph_ql.schema import UserObject


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)

    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, username):
        user = User(username=username)

        db.session.add(user)
        db.session.commit()
        return CreateUser(user=user)


class DeleteUser(graphene.Mutation):

    users = graphene.Field(lambda: graphene.List(UserObject))
    success = graphene.Boolean()
    def mutate(self, info):
        try:
            users = User.query.all()
            for user in users:
                db.session.delete(user)
                db.session.commit()
            return DeleteUser(success=True)
        except Exception as e:
            return DeleteUser(success=False)
