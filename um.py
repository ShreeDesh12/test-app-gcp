
import webapp2
from models import User
import cgi
import urllib
import wsgiref.handlers
from utils import *

# class MainPage(webapp2.RequestHandler):
#   def get(self):
#     self.response.out.write('<html><body>')
#     guestbook_name=self.request.get('guestbook_name')   

#     # Ancestor Queries, as shown here, are strongly consistent with the High
#     # Replication datastore. Queries that span entity groups are eventually
#     # consistent. If we omitted the ancestor from this query there would be a
#     # slight chance that Greeting that had just been written would not show up
#     # in a query.
#     greetings = db.GqlQuery("SELECT * "
#                             "FROM Greeting "
#                             "WHERE ANCESTOR IS :1 "
#                             "ORDER BY date DESC LIMIT 10",
#                             guestbook_key(guestbook_name))

#     for greeting in greetings:
#       if greeting.author:
#         self.response.out.write(
#             '<b>%s</b> wrote:' % greeting.author.nickname())
#       else:
#         self.response.out.write('An anonymous person wrote:')
#       self.response.out.write('<blockquote>%s</blockquote>' %
#                               cgi.escape(greeting.content))

#     self.response.out.write("""
#           <form action="/sign?%s" method="post">
#             <div><textarea name="content" rows="3" cols="60"></textarea></div>
#             <div><input type="submit" value="Sign Guestbook"></div>
#           </form>
#           <hr>
#           <form>Guestbook name: <input value="%s" name="guestbook_name">
#           <input type="submit" value="switch"></form>
#         </body>
#       </html>""" % (urllib.urlencode({'guestbook_name': guestbook_name}),
#                           cgi.escape(guestbook_name)))


# class Guestbook(webapp2.RequestHandler):
#   def post(self):
#     # We set the same parent key on the 'Greeting' to ensure each greeting is in
#     # the same entity group. Queries across the single entity group will be
#     # consistent. However, the write rate to a single entity group should
#     # be limited to ~1/second.
#     guestbook_name = self.request.get('guestbook_name')
#     greeting = Greeting(parent=guestbook_key(guestbook_name))

#     if users.get_current_user():
#       greeting.author = users.get_current_user()

#     greeting.content = self.request.get('content')
#     greeting.put()
#     self.redirect('/?' + urllib.urlencode({'guestbook_name': guestbook_name}))

# class WriteIntoDatastore(webapp2.RequestHandler):
#   def get(self):
#     try:
#       g = Greeting.get(key="agxkZXZ-Zmxhc2thcHByJwsSCUd1ZXN0Ym9vayIDQUJDDAsSCEdyZWV0aW5nGICAgICAgKAIDA")
#       self.response.out.write(str(g))
#     except Exception as e:
#       error = "Error: "+ str(e)
#       self.response.out.write(error)
import json
from google.appengine.ext import ndb
from google.appengine.ext.deferred import deferred

from routines import *

class createUser(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("Working")
  def post(self):
    request_data = self.request.body 
    request_data = json.loads(request_data)
    print(request_data)
    u = User(
      name = request_data['name'],
      id = request_data.get('ID'),
      email = request_data.get('email')
    )
    u_key = u.put()
    print("Insertion successful")
    print(set_key_directly(u))
    print("Set email as key")
    print(u_key.get())
    out = "Details inserted: " + str(u_key.get())
    return self.response.out.write(out)

class fetchUser(webapp2.RequestHandler):
  def post(self):
    request_data = self.request.body
    request_data = json.loads(request_data)
    print("Request : ", request_data)
    output = ""
    if request_data.get('email'):
      print(request_data['email'])
      records = ndb.gql('SELECT * from User where email = :1', request_data['email']).fetch()
    else:
      records = ndb.gql('SELECT * from User').fetch()
    print(records)
    for record in records:
      u_key = record.key
      print(u_key)
      user = u_key.get()
      print("Old details: ", user.name, user.email)
      new_name = request_data['new_name']
      if new_name:
        deferred.defer(user_name_change, u_key, new_name)
        print("New Details: ", user.name, user.email)
      u = "Name: " + str(user.name) + ", Email: " + str(user.email)
      output+=u+"\n"
    # query = User.query().fetch()
    # print(query)
    return self.response.out.write(output)
