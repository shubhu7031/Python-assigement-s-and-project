# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("AC7c4790d1b7aa82962ddc36476eed4d1b", "4e99e8224e60cc7371fdd6d514fe3450")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+917046575331", 
                       from_="+19124937080", 
                       body="Hello from Python!")