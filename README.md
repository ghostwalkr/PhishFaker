# PhishFaker
A script to make lots of fake logins to phishing pages

## Description
PhishFaker uses a log overflow attack on phishing sites. It automatically sends logins using fake generated credentials. The idea is that the phishing site owner won't be able to tell the difference between the fake logins from PhishFaker and the logins from real victims.

## Todo
This script isn't user friendly at the moment. You have to manually find out where the phishing page sends the login POST request to and then edit the script accordingly.
- Function to find the specific request and POST data for each phishing site.
- Command line arguments.

## Usage 
`python3 phishfaker.py <url>`
