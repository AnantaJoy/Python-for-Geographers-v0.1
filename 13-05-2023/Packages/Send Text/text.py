from twilio.rest import Client
from packages import account_sid, auth_token

client = Client(account_sid, auth_token)


call = client.messages.create(
    to = "+919999999999",
    from_ = "+12058585858",
    body = "Hello from Python!", 
)

call