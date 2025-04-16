from kavenegar import KavenegarAPI, APIException, HTTPException
from django.conf import settings




class SMSClient:
    def __init__(self):
        self.api_key = settings.KAVENEGAR_API_KEY
        self.sender = settings.KAVENEGAR_SENDER


    def send_otp(self, phone, code):
        try:
            api = KavenegarAPI(self.api_key)    
            params = {
                "sender":self.sender,
                "receptor":phone,
                "message":f"your validated code is {code}",
            }
            return api.sms_send(params)
        except (APIException, HTTPException) as e:
            print(f"[SMS ERROR]:{e}")
            return None
        