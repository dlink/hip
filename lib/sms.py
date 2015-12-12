import os

from twilio.rest import TwilioRestClient 

class Sms(object):
        
    def send(self, phonenumber, msg):

        account_sid = os.getenv('SMS_ACCOUNT_SID')
        auth_token  = os.getenv('SMS_AUTH_TOKEN')
        our_phone_number = os.getenv('SMS_OUR_PHONE_NUMBER')
        
        client = TwilioRestClient(account_sid, auth_token) 
        client.messages.create(
            to=phonenumber, 
            from_=our_phone_number,
            body=msg,  
            )

if __name__ == '__main__':
    my_phone_number = os.getenv('SMS_MY_PHONE_NUMBER')
    Sms().send(my_phone_number, 'Peace')
