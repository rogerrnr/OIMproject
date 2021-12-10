from twilio.rest import Client, TwilioClient
from configTWL import accountSID
from configTWL import authToken
import emoji
import time


twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+17162815007'
myCellPhone = '+18454180950'
myCellPhone2 = '+12068180891'




def txtself(message):
    """
    This is a function that sends a message to our phone numbers
    """
    twilioCli.messages.create(body= f'{message}', from_= myTwilioNumber, to= myCellPhone)
    twilioCli.messages.create(body= f'{message}', from_= myTwilioNumber, to= myCellPhone2)
    
# txtself("Hey, was good homie")



# thumbsup = emoji.emojize(":thumbs_up:")
#Sends a Message to my phone
# Message = twilioCli.messages.create(body= f'Hey Michael was good homie{thumbsup}!', from_= myTwilioNumber, to= myCellPhone)


# Sends a message to my phone every 10 seconds
#def sendmessage():
    #twilioCli.messages.create(body= "Michael - Come here - I want to see you.", from_= myTwilioNumber, to= myCellPhone)
    #time.sleep(10)
#for i in range(5):
    #sendmessage()

