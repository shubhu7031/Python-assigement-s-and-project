# python script for sending message update

import time
from time import sleep
from sinchsms import SinchSMS

# function for sending SMS
def sendSMS():
    

	# enter all the details
	# get app_key and app_secret by registering
	# a app on sinchSMS
	number = '9601255224'
	app_key = '9fa18a7a-9419-4bba-bfd7-d07c8d936046'
	app_secret = '27Py3zsXWkqDRGdK4zOkGg=='

	# enter the message to be sent
	message = 'Hello Message!!!'

	client = SinchSMS(app_key, app_secret)
	print("Sending '%s' to %s" % (message, number))

	response = client.send_message(number, message)
	message_id = response['messageId']
	response = client.check_status(message_id)

	# keep trying unless the status returned is Successful
	while response['status'] != 'Successful':
		print(response['status'])
		time.sleep(1)
		response = client.check_status(message_id)

	print(response['status'])

if __name__ == "__main__":
	sendSMS()
