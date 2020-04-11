from flask_restplus import Resource, reqparse
from graphql_service import api
from graphql_service.service.user import _User

ns = api.namespace("user",
           description="sample user api")

@ns.route('/get')
class UserGet(Resource):
    def get(self):
        res = _User.all_user()
        return res

parser = reqparse.RequestParser()
parser_copy = parser.copy()
parser.add_argument('username', required=True, help=" Name cannot be blank!")
@ns.expect(parser)
@ns.route('/post')
class UserPost(Resource):
	def post(self):
		args = parser.parse_args()
		username = args.get('username')
		res = _User.create_user(username)
		return res
		
@ns.route('/delete')
class UserDelete(Resource):
    def delete(self):
        res = _User.delete_users()
        return res
