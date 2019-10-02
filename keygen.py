import hmac
import hashlib
import base64
secret = bytes('oh nah nah whats my name', 'utf-8')
message = bytes('potatoey','utf-8')
signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
# base64.b64encode(dig)
print(signature)