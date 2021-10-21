from twilio.rest import Client

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) # use your personal TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN as the values for the env variables.

# my_message takes in from the terminal the message that is to be sent.   
print('enter a text message')
my_message = input()

msg_receipients = ('+1-123-123-1234', '+1-123-123-1235', '+1-123-123-1236') # an array containing the phone numbers that will be sent my_message.  

# refresh_num_msgs takes in from the terminal the number of times the message will be sent. 
print('enter the number of times to send the text message')
refresh_num_msgs = input()
refresh_num_msgs = int(refresh_num_msgs) 

def create_text_message():
    """ sends a message from the terminal to the phone numbers in msg_receipients.  
    num_msgs is the number of times the message will be sent.  
    Use your TWILIO_PHONE_NUMBER as an env variable."""
    for receipient in msg_receipients:
        num_msgs = refresh_num_msgs
        while num_msgs > 0:
            msg = client.messages.create(
                to=receipient,
                from_=TWILIO_PHONE_NUMBER,
                body=f"{my_message}"
            )
            num_msgs -= 1

 