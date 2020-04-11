from flask_restplus import Resource, reqparse
from graphql_service import api
from graphql_service.service.post import _Post

ns = api.namespace("posts",
           description="sample post api")

@ns.route('/get')
class PostsGet(Resource):
    def get(self):
        res = _Post.all_post()
        return res

parser = reqparse.RequestParser()
parser_copy = parser.copy()
parser.add_argument('username', required=True, help=" Name cannot be blank!")
parser.add_argument('title', required=True, help=" title cannot be blank!")
parser.add_argument('body', required=True, help=" body cannot be blank!")
@ns.expect(parser)
@ns.route('/post')
class PostsPost(Resource):
    def post(self):
        args = parser.parse_args()
        username = args.get('username')
        title = args.get('title')
        body = args.get('body')
        res = _Post.create_post(username, title, body)
        return res

@ns.route('/delete')
class PostsDelete(Resource):
    def delete(self):
        res = _Post.delete_posts()
        return res