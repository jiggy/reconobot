import webapp2
import sys, os

class MainPage(webapp2.RequestHandler):
    def get(self):
        import empsit
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        self.response.write(empsit.get_empsit_data())

"""
Import all .zip and .egg libraries from the packages directory
"""

def import_from(package_dir):
    package_dir_path = os.path.join(os.path.dirname(__file__), package_dir)

    # Allow unzipped packages to be imported
    # from packages folder
    print "########## Importing ", package_dir_path
    sys.path.insert(0, package_dir_path)

    # Append zip archives to path for zipimport
    for filename in os.listdir(package_dir_path):
        if filename.endswith((".zip", ".egg")):
            sys.path.insert(0, "%s/%s" % (package_dir_path, filename))

import_from("lib")
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
