import webapp2
import empsit

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        self.response.write(empsit.get_empsit_data())


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
