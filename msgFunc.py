import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Set environment variables for your credentials

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def sendTextMsg(name,amount,mobNumber):
  message = client.messages.create(
  body= name + " Has been fined. ₹  "+str(amount) ,
  from_="+15109399464",
  to="+91"+str(mobNumber)
  )
  print(message)
  return "Message Send Successfully"
