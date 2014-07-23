import praw
import re
import sys
import json


USERNAME = "xxxx"
PASSWORD = "xxxx"
SUBREDDIT = "books"

user_agent = ("usernotes 1.0 by /u/boib")
r=praw.Reddit(user_agent=user_agent)

Trying = True
while Trying:
	try:
		r.login(USERNAME, PASSWORD)
		print('Successfully logged in\n')
		Trying = False
	except praw.errors.InvalidUserPass:
		print('Wrong Username or Password')
		quit()
	except Exception as e:
		print("%s" % e)
		time.sleep(5)


x = r.get_subreddit(SUBREDDIT)
d = x.get_wiki_page("usernotes")
data = json.loads(d.content_md)

for j in data["users"]:
    print ("-------------------------------")
    print (j)
    for k in data["users"][j]["ns"]:
        print (k['n'])


#for j in data["constants"]["users"]:
#    print (j)
#


print ("\n-------------------------------\nChecking for deleted users\n-------------------------------")


gone = []
for i in data["users"]:
    try:
        print ("Getting user %s" % i)
        v = r.get_redditor(i)

    except:
        #print "Unexpected error:", sys.exc_info()[0]
        print ("========= user %s appears to be gone" % i)
        gone.append(i)
        pass

print ("\n-------------------------------\nList of gone!\n-------------------------------")
for i in gone:
    print (i)


