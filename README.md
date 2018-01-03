# EventbriteMonitor
An extremely simple script that alerts you via sms when Eventbrite tickets are available

This script will be best used when tickets have been sold out however there may be more tickets being released without a release date. This script can monitor an Eventbrite ticket page and will alert you when the tickets are no longer sold out.

## Usage
```python EventbriteMonitor.py (url of the Eventbrite ticket page)```
This will run the tool once however if you want to continously monitor the ticket page you may want to set something else up.

To use this tool you will require a twilio account. You can get a free trial account from ![here](https://www.twilio.com).

You will then have to modify this section of the code and add in your tokens and contact numbers.
```
account_sid = "Twilio account_sid"
auth_token = "Twilio auth_token"
client = Client(account_sid, auth_token)
message = client.api.account.messages.create(
		to = "Your phone number",
		from_ ="Your twilio phone number",
```

## Implementation
There are multiple ways to implement this tool. The best way would be to run this tool on a vps or dedicated box. Even a raspberry pi with internet connectivity would work. Although a more feasable method would be to use your own computer and add the code to run on startup or use task scheduler if you are in windows.

To set this up on a linux box you could modify ```~/.bashrc``` and add ```sudo screen -dm python (/path/to/EventbriteMonitor.py) (url of evenbrite ticket page)```

This will start the script in the background when you first boot up. If you dont want to restart your pc you could then run ```sudo screen -dm python (/path/to/EventbriteMonitor.py) (url of evenbrite ticket page)``` in your terminal.

This is the method you could use when implementing this program on a vps or dedicated server/raspberry pi.

## Finally
If the program comes across an error whether this being something wrong with twilio or a networkng error it will exit the program and dump the error to ```log.txt``` which will be in the same directory as the script.

Once it sees that the tickets are available again it will send an sms to the phone number entered in the code and then exit aswell.
