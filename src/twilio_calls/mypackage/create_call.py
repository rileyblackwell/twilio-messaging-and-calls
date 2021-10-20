from twilio.rest import Client

client = Client(ACCOUNT_SID, AUTH_TOKEN) # use your personal twilio ACCOUNT_SID and AUTH_TOKEN as the values for the env variables

call_receipients = ('+1-123-123-1234', '+1-123-123-1235', '+1-123-123-1236') # an array containing the phone numbers that will be called  

def create_phone_call():
    for receipient in call_receipients:
        """ create a call to phone numbers in call_receipients  """
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=receipient,
            from_='+18507808382'
        )

    