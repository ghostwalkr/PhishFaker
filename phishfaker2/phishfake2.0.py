#!/usr/bin/env python3
# Phishfaker
# Send fake logins to a phishing site
import requests, argparse, threading
from time import localtime
from random import choice, randint

def showInfo(string):
    now = localtime()
    print(f"[{now.tm_hour}:{now.tm_min}:{now.tm_sec}] {string}")

def loadLists():
    # Load useragent, password, and usernames lists from files
    # Takes no parameters
    # Returns useragent, passwords, and usernames lists

    useragents = []
    passwords = []
    usernames = []

    f = open("useragents.list", "r")
    for ua in f:
        if len(ua) < 5:
            continue
        useragents.append(ua.replace("\n",""))
    f.close()
    
    f = open("passwords.list", "r")
    for p in f:
        if len(p) == 0:
            continue
        passwords.append(p.replace("\n",""))
    f.close()

    f = open("usernames.list", "r")
    for u in f:
        if len(u) == 0:
            continue
        usernames.append(u.replace("\n",""))

    return useragents, passwords, usernames

def sendRequest(url, post_params=None, http_headers=None):
    # url - URL to send request to <str>
    # post_params - POST request parameters <dict>
    # http_headers - HTTP request headers
    # Returns: 
    if http_headers == None:
        http_headers = {
                "Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"en-US,en;q=0.5",
                "User-Agent":"PhishFaker v2.0"
                }

    if post_params == None:
        post_params = {
                "password":"password",
                "username":"fuckzephishers!"
                }

    response = requests.post(url, headers=http_headers, data=post_params)

    if verbose:
        showInfo("Target responded with {}".format(response.status_code))

def requester(useragents, passwords, usernames):
    # useragents - user agents list <list>
    # passwords - passwords list <list>
    # usernames - usernames list <list>
    global logins_sent
    while True:
        useragent = choice(useragents)
        password = choice(passwords)
        username = choice(usernames)
        
        headers = {
                "Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"en-US,en;q=0.5",
                "User-Agent":useragent
                }

        post = {
                post_pass:password,
                post_user:username
                }
        
        if verbose:
            showInfo("Sending {}:{} to target".format(username, password))

        sendRequest(args.phishurl, post_params=post, http_headers=headers)

        myLock = threading.Lock()
        myLock.acquire()
        logins_sent += 1
        myLock.release()

        showInfo("Sent {} logins".format(logins_sent))

# Parse command line arguments
parser = argparse.ArgumentParser(prog="phishfaker", description="Send fake logins to phishing sites", allow_abbrev=True)
parser.add_argument("phishurl", type=str, metavar="url", help="URL of the phishing site")
parser.add_argument("-p", metavar="password", type=str, help="the name of the password POST parameter", required=True)
parser.add_argument("-u", metavar="username", type=str, help="the name of the username POST parameter", required=True)
parser.add_argument("-t", metavar="threads", type=int, help="number of threads to run at once.", required=True)
parser.add_argument("--verbose", action="store_true", help="show more information")

args = parser.parse_args()

### MAIN #####

verbose = args.verbose
post_pass = args.p
post_user = args.u
thread_count = args.t
logins_sent = 0

useragents, passwords, usernames = loadLists()

thread_list = []

for thr in range(1, thread_count + 1):
    t = threading.Thread(target=requester, args=(useragents, passwords, usernames))
    thread_list.append(t)
    t.start()
