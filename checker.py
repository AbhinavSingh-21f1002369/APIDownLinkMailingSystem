import subprocess
#import mailer
import time
import os
import requests
from discord import Webhook, RequestsWebhookAdapter
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('url')
webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
while True:
    r = requests.get("http://iot.ccnet.in:1313/logs")
    if r.status_code == 200:
        webhook.send(time.ctime()+" API Online")
        print(time.ctime()+" API Online")
        time.sleep(7200)
    else:
        webhook.send(time.ctime()+" API Offline")
        print(time.ctime()+" API Offline")
        #mailer.do_mail()
        time.sleep(7200)