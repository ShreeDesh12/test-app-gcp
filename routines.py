
from google.appengine.ext import db
from google.appengine.api import users
from models import User

# class user_routines():
def user_name_change(key, new_name):
  # print("Entered inside the queue successfully")
  # user = key.get()
  print(new_name)
  # user.name = new_name
  # u = user.put()
  # return u 

  # @classmethod
  # def run_cls(cls, product_key):
  #     cls().user_name_change(product_key)
  