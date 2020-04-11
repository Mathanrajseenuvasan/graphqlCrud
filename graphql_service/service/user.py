from graphql_service.graph_ql import schema
from graphql_service.models import User
import json

class _User(object):

    @classmethod
    def all_user(cls):
        query_string = '''
            query allUsers {
                allUsers{
                edges{
                node{
                    uuid
                    username
                        }
                    }
                }
            }
        '''
        result = schema.execute(
            query_string,
            operation_name='allUsers'
        )
        res = result.data
        return res

    @classmethod
    def create_user(cls, username):
        mutate_string = '''
            mutation createUser {
              createUser(username:"%s"){
                user{
                  username
                  uuid
                }
              }
            }
        ''' % (username)
        result = schema.execute(
            mutate_string,
            operation_name='createUser'
        )
        res = result.data
        return res


    @classmethod
    def delete_users(cls):
        mutate_string = '''
            mutation deleteUser {
              deleteUser{
              success
              }
            }
        '''
        result = schema.execute(
            mutate_string,
            operation_name='deleteUser'
        )
        res = result.data
        return res