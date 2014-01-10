import webapp2
import util

class MainPage(webapp2.RequestHandler):
    def get(self):
        import empsit
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        self.response.write(empsit.get_empsit_data())

import_from("lib")
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
