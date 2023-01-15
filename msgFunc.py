
import os
from twilio.rest import Client

# Set environment variables for your credentials

account_sid = "AC576ece80995665f06bf00ccfffbc4e9e"
auth_token = "d445f62524e170bf1e0ee0f641f0bf27"
client = Client(account_sid, auth_token)

def sendTextMsg(name,amount,mobNumber):
  message = client.messages.create(
  body= name + " Has been fined. ₹  "+str(amount) ,
  from_="+15109399464",
  to="+91"+str(mobNumber)
  )
  print(message)
  return "Message Send Successfully"
