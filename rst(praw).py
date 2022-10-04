import praw

debug = True #set this to False to iterate through old subs and subscribe on your new account.

# deepcode ignore MissingClose: <please specify a reason of ignoring this>, deepcode ignore MissingClose: <please specify a reason of ignoring this>, deepcode ignore MissingClose: <please specify a reason of ignoring this>, deepcode ignore MissingClose: <please specify a reason of ignoring this>, deepcode ignore MissingClose: <please specify a reason of ignoring this>
with open('keys.txt', mode='r') as f: #if you haven't already, populate the keys file with your parameters=
    keylist = f.readlines()

#these print your keys. so you can make sure everything is correct.
#print("\n" + keylist[1]+"\n"+keylist[3]+"\n"+keylist[5]+"\n"+keylist[7]+"\n")
#print("\n" + keylist[9]+"\n"+keylist[11]+"\n"+keylist[13]+"\n"+keylist[15]+"\n")

r1 = praw.Reddit(client_id = keylist[1], #praw instance for old account
                     client_secret = keylist[3],
                     user_agent ='redditsubswitcherV1',
                     username = keylist[5],
                     password = keylist[7])

r2 = praw.Reddit(client_id = keylist[9], #praw instance for new account
                     client_secret = keylist[11],
                     user_agent ='redditsubswitcherV1',
                     username = keylist[13],
                     password = keylist[15])

subreddits = list(r1.user.subreddits(limit=None)) #return all subs to a iterable list
for s in subreddits:
    if debug == False:
        r2.subreddit(str(s)).subscribe() 
    print ('subscribed to (' + str(s) + ') on acct: ' + keylist[13])
print ('done.')
