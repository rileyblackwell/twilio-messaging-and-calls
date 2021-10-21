from twilio.rest import Client

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) # use your personal TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN as the values for the env variables.

call_receipients = ('+1-123-123-1234', '+1-123-123-1235', '+1-123-123-1236') # an array containing the phone numbers that will be called.  

def create_phone_call():
    for receipient in call_receipients:
        """ creates voice calls to phone numbers in call_receipients. 
        Use your personal TWILIO_PHONE_NUMBER as an env variable. """
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=receipient,
            from_=TWILIO_PHONE_NUMBER
        )

    