#!/usr/bin/python

####################################
#       +++++++++++++++++++        #
#        EventbriteMonitor         #
#       +++++++++++++++++++        #
#       Author: CuPcakeN1njA       #
#       ++++++++++++++++++++       #
####################################

"""Usage ==> EventbriteMonitor.py (url of eventbrite ticket page) 

Use this tool to monitor an Eventbrite ticket page.

This script will send you a text message using the
twilio api when tickets are available again if they
have been sold out and are reselling.

In order to use this script you will have to create a twilio account
and modify the alert() function and add in your own api tokens and contact
numbers. How to do this can be found in the twilio documentation and examples
and you can set up your twilio account here: https://www.twilio.com 
"""
import requests
import time
from twilio.rest import Client
import sys
from datetime import datetime

def gethtml(url):
	resp = requests.get(url)
	html = resp.text
	return html

def check(html):
	if "Sold Out" in html:
		return False
	else:
		return True

def alert(url):
	account_sid = "Twilio account_sid"
	auth_token = "Twilio auth_token"
	client = Client(account_sid, auth_token)
	message = client.api.account.messages.create(
		to = "Your phone number",
		from_ ="Your twilio phone number",
		body = ("Your tickets are on sale\n Buy them from: \n%s" % url))

def usage():
	print("""
Usage ==> python EventbriteMonitor.py (url of eventbrite ticket page)
""")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		usage()
	else:
		try:
			url = sys.argv[1]
			while True:
				if check(gethtml(url)) == True:
					print("Tickets Available")
					break
				else:
					print("Tickets Unavailable")
				time.sleep(120)
			alert(url)
		except Exception as e:
			print("\nProgram exiting because of this error: %s" % e )
			f = open("log.txt", "a+")
			f.write("\nProgram ended at %s because of this error:\n%s" % (datetime.now(), e))
			f.close()
