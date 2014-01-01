
r = praw.Reddit(user_agent='econobot', disable_update_check=True)
recon = r.get_subreddit('economics')
submissions = recon.get_hot(limit=5);

for x in submissions:
    print str(x)


#r.login("econobot", "buttered$noodles")
#r.login("tootie", "22t00tie")
#r.send_message("econobot", "hi", "yay")