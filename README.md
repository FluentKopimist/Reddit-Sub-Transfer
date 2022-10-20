# Reddit-Sub-Transfer

Very simple python script to take your old reddit subscriptions and move them to a new account.

you will to install praw by runnning:

>pip install praw

Next make an app on each of the accounts you want to communicate with.
>login to reddit

>go to https://www.reddit.com/prefs/apps

>create a new app

![create app](https://user-images.githubusercontent.com/35983980/193926949-46155510-5e94-44ab-b227-80dd0c31357c.PNG)

next you're going to open your app

>make note of your client id (underneath "personal script") and your "secret"

>do this for both accounts

![Capture](https://user-images.githubusercontent.com/35983980/193925617-3edaa4d3-7311-4c99-a8f8-8569ea5ff90c.PNG)


now populate the keys.txt

>open the keys.txt file and enter your "client ids", "secrets", usernames and passes in place of the "$$$$"

>when you run it, it will tell you what changes it will make

>if you want the changes to be permanent, change the debug flag to "False"

![debug](https://user-images.githubusercontent.com/35983980/193929649-4522c4e2-9ab0-4a84-b277-51f0d750b6ad.PNG)

>run again to batch subscribe to all the subs on your old account
