from google.appengine.ext import ndb
def set_key_directly(user):
    user.key = ndb.Key('User', user.email)
    return user.key