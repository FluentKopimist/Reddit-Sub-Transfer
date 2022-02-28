import requests
import json
import os


def getLogins():
    
    #uncomment if you would like to enter your api keys in the python terminal
    
    #import pwinput
    #oldClient = pwinput.pwinput(prompt = 'client id for old account: ')
    #oldSecret = pwinput.pwinput(prompt = 'client secret for old account: ')
    #oldUsername = input('username for old account: ')
    #oldPassword = pwinput.pwinput(prompt = 'password for old account: ')
    #newClient = pwinput.pwinput(prompt = 'client id for new account: ')
    #newSecret = pwinput.pwinput(prompt = 'client secret for new account: ')
    #newUsername = input('username for new account: ')
    #newPassword = pwinput.pwinput(prompt = 'password for new account: ')
    #api_list = [oldClient, oldSecret, oldUsername, oldPassword, newClient, newSecret, newUsername, newPassword]

    #if you would like to use an env variable in the format of "oldclient/oldsecret/oldusername/oldpassword/newclient/newsecret/newusername/newpassword" (w/o quotes)
    
    api_String = os.environ["api_login"]
    api_list = api_String.split("/", -1)
    
    return(api_list)

def getSubs(api_list):

    auth = requests.auth.HTTPBasicAuth(api_list[0], api_list[1])

    data = {
        'grant_type' : 'password',
        'username' : api_list[2],
        'password' : api_list[3]
        }
    headers = {'User-Agent' : 'FluentKopimist_Sub-Transfer_API/0.0.1}'}

    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

    TOKEN = res.json()['access_token']

    headers = {**headers, **{'Authorization':f'bearer {TOKEN}'}}

    res = requests.get('https://oauth.reddit.com/subreddits/mine/subscriber', headers=headers)
    
    for post in res.json()['data']['children']:
        

    

api_list = getLogins()
getSubs(api_list)