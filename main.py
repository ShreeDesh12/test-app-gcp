# import webapp2
# import os
# import json

# # class HelloWebapp2(webapp2.RequestHandler):
# #     def get(self):
# #         response = {"ENV": ""}
# #         if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
# #         # Production
# #             print("PROD")
# #             response['ENV'] = "PROD"
# #         else:
# #             print("DEV")
# #             response['ENV'] = "DEV"
# #         response = json.dumps(response)
# #         return webapp2.Response(response)

# #     def post(self):
# #         response = {"Success": True}
# #         try:
# #             request_data = self.request.body
# #             request_data = json.loads(request_data)
# #             name = request_data['name']
# #             print("Name:", name)
# #             response['name'] = name 
# #         except Exception as e:
# #             response['Success'] = False
# #             response['error'] = str(e)
# #     response = json.dumps(response)
# #     return response


# class MainPage(webapp2.RequestHandler):
#     form = """
#          <form method="post">
#               <input type="" name="day">
#               <input type="" name="month">
#               <input type="" name="year">
#               <input type="submit" name="">
#          </form>
#          """
#     def get(self):
#         self.response.out.write(self.form)

#     def post(self):
#         request_data = {}
#         request_data['day'] = self.request.get('day') 
#         print(request_data)
#         self.response.out.write("thank")


# # app = webapp2.WSGIapp([
# #     ('/', HelloWebapp2),
# # ], debug=True)


# app = webapp2.WSGIApplication([
#     ('/', MainPage),
# ], debug=True)


from google.appengine.ext.deferred.deferred import TaskHandler
from google.appengine.ext import webapp
import datetime
from routines import *
import webapp2
from um import *

# from google.appengine.ext.deferred import deferred
from google.appengine.ext.webapp.util import run_wsgi_app


def intercept_deferred(router, request):
    rv = router.default_matcher(request)
    try:
        func, args, kwargs = pickle.loads(request.body)
        logging.info ('deferred.__func__: {}'.format(func.__name__))
        logging.info (args)
        logging.info (kwargs)
    except Exception, e:
        pass

    return rv



app = webapp2.WSGIApplication([
#   ('/', MainPage),
#   ('/sign', Guestbook),
#   ('/task', WriteIntoDatastore),
  ('/createUser', createUser),
  ('/fetchUser', fetchUser)
], debug=True)

deferred_application = webapp.WSGIApplication([(".*", TaskHandler)])

def main():
    run_wsgi_app(deferred_application)
    app.RUN()


if __name__ == '__main__':
  main()

