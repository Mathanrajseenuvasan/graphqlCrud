# Imports
from graphql_service.models import Post, User
from ..config import db
import graphene
from graphql_service.graph_ql.schema import PostObject

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True) 
        username = graphene.String(required=True)

    post = graphene.Field(lambda: PostObject)

    def mutate(self, info, title, body, username):
        user = User.query.filter_by(username=username).first()
        post = Post(title=title, body=body)

        if user is not None:
            post.author = user
            
        db.session.add(post)
        db.session.commit()
        return CreatePost(post=post)


class DeletePost(graphene.Mutation):

    posts = graphene.Field(lambda: graphene.List(PostObject))
    success = graphene.Boolean()
    def mutate(self, info):
        try:
            posts = Post.query.all()
            for post in posts:
                db.session.delete(post)
                db.session.commit()
            return DeletePost(success=True)
        except Exception as e:
            return DeletePost(success=False)