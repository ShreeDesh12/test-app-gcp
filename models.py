from google.appengine.ext import ndb
from google.appengine.api import users

# class Greeting(ndb.Model):
#   """Models an individual Guestbook entry with an author, content, and date."""
#   author = ndb.UserProperty()
#   content = ndb.StringProperty(multiline=True)
#   date = ndb.DateTimeProperty(auto_now_add=True)

#   @classmethod
#   def query_book(cls, ancestor_key):
#     return cls.query(ancestor=ancestor_key).order(-cls.date)

class User(ndb.Model):
  id = ndb.IntegerProperty()
  name = ndb.StringProperty()
  email = ndb.StringProperty()

  @classmethod
  def get_by_email(cls, user):
      return cls.query().filter(cls.email == user.email()).get()


  # def guestbook_key(guestbook_name=None):
  #   """Constructs a datastore key for a Guestbook entity with guestbook_name."""
  #   return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')