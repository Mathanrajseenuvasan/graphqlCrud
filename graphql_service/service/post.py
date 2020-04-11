from graphql_service.graph_ql import schema
from graphql_service.models import Post
import json

class _Post(object):

    @classmethod
    def all_post(cls):
        query_string = '''
            query allPosts{
                allPosts{
                edges{
                node{
                    body
                    title
                    author{
                        uuid
                        username
                    }
                    }
                }
                }
                }
        '''
        result = schema.execute(
            query_string,
            operation_name='allPosts'
        )
        res = result.data
        return res

    @classmethod
    def create_post(cls, username, title, body):
        mutate_string = '''
            mutation createPost {
              createPost(username:"%s", title:"%s", body:"%s"){
                post{
                  title
                  body
                  author{
                    username
                  }
                }
              }
            }
        ''' % (username, title, body)
        result = schema.execute(
            mutate_string,
            operation_name='createPost'
        )
        res = result.data
        return res

    @classmethod
    def delete_posts(cls):
        mutate_string = '''
            mutation deletePost {
                deletePost{
                success
              }
            }
        '''
        result = schema.execute(
            mutate_string,
            operation_name='deletePost'
        )
        res = result.data
        return res