# PhishFaker
A script to make lots of fake logins to phishing pages

## Description
PhishFaker uses a log overflow attack on phishing sites. It automatically sends logins using fake generated credentials. The idea is that the phishing site owner won't be able to tell the difference between the fake logins from PhishFaker and the logins from real victims.

## Usage
python3 phishfake2.0.py -t <threads> -u <usernameparam> -p <passparam> --verbose url
  -t the number of request threads to have going at once. 
  -u POST request username parameter name
  -p POST request password parameter
  --verbose enable verbose mode
  url - url to the phishing site
  
  ex: `$ python3 phishfake2.0.py -t 4 -u email -p pass https://phishing.site/login.php`
  
 ## Usage Guide
 This is a little guide on how to use the tool. It is easy once you know how, but it's not super obvious from the beginning.
 1. Find a site
 I like to look on https://phishtank.com. I use the search function to find verified phishes that are online: https://phishtank.com/phish_search.php?valid=y&active=y&Search=Search. In general I look for ones that look like social media or banking phishes. Ones that have bank, facebook, amazon, etc in the domain. I also tend to go for ones that have login.php or something similar. These ar e usually promising.
 
 2. Extract the needed info
 Now we need a few things. This is the part of the process I need to automate, but one project at a time. You need a) the URL that the login post request goes to. b) the name of the username post parameter and c) the name of the post password parameter. You can get all three using your browser's development tools. In firefox it goes like this: menu > web developer > network. Or you can press ctrl + shift + e. Now make a fake log in to the phishing site. It'll make a bunch of stuff scroll across the network screen. Look near the top for something like "login.php." It should be a POST request. Once you see it, click on it. Then click on the "parameters" tab on the right side of the web dev window. It should have something like email:"email you put in" password: "password you entered". We're going to need to copy the URL the post request went to and the post request username/password parameter. Open up a terminal and enter: `python3 phishfake2.0.py -u <post username param> -p <post pass param> -t <thread count> <URL POST request went to>`
 Phishfaker should start right up. Have fun!
 
 ## Todo
 - Add way to pass custom POST parameters to phishfaker.
 - Detect a "normal" response and inform user if an abnormal response is receieved.
