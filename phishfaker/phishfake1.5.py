#!/usr/bin/env python3
# Phishfake v1.5
# Threaded script to send fake logins to phishing sites. Aka Log overflow attack.

import requests, random, threading, json, sys

url = sys.argv[1]

thread_count = 4
post_email_param = ''
post_password_param = ''

def send_request(url, email_param, password_param):
    # Function always returns 0 unless execption occurred

    # All parameters are mandatory
    # url: url of site to send request to - string
    # email_param: the name of the HTTP POST email parameter - string
    # password_param: Name of the HTTP POST password parameter - string
    seperators = ['', '_', '-', '.']
    domains = ['yahoo.com', 'gmail.com', 'outlook.com', 'hotmail.com']
    useragent = ''

    req_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": useragent
            }
    post_data = {
            email_param: email,
            password_param: password
            }
   
    # Generate email/password
    random_num = random.randint(1,10000)
    random_name = random.choice(name_list)
    random_domain = random.choice(domains)
   
    email = f'{random_name}{seperator}{random_num}@{random_domain}'
    password = random.choice(password_list)
    useragent = random.choice(useragent_list)

    try:
        threadlock = threading.Lock()
        threadlock.acquire()
        r = requests.post(url, data=post_data, headers=req_headers)
        print(f'[*] Sent {email}:{password}... {r.status_code}')
        sent_requests += 1
        threadlock.release()
        return 0
    except Exception as error:
        print(f'Exception occurred: {error}')
        threadlock.release()
        return 1

# Load the files containing names, passwords, and user agents and convert the contents from json to python lists

with open('names.json', 'r') as namefile:
    name_list = json.load(namefile)
    namefile.close()

with open('passwords.json', 'r') as passfile:
    password_list = json.load(passfile)
    passfile.close()

with open('useragents.json', 'r') as useragentfile:
    useragent_list = json.load(useragentfile)
    useragentfile.close()


sent_requests = 0
thread_list = ()

while True:
    for i in range(thread_count):
        th = threading.Thread(send_request, args=(url, post_email_param, post_password_param))
        thread_list += (th)
        th.start()
