import util

util.import_from("lib")
import praw
import empsit

def submit_link(title, url):
    r = praw.Reddit(user_agent='econobot/0.1 by /u/tootie', disable_update_check=True)
    credentials = util.get_config("creds")
    r.login(credentials["user"], credentials["password"])
    r.submit("economics", title, url=empsit.bls_url)

data = empsit.get_empsit_data()
title = empsit.generate_headline(data)

print empsit.bls_url
print title
#submit_link(title, empsit.bls_url)