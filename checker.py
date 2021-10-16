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
    process = subprocess.run(["ping","iot.ccnet.in","-c","2"], capture_output=True, text=True)
    standard_out = process.stdout
    standard_out = standard_out.split("\n")
    #print(type(standard_out))
    #print(standard_out)
    if len(standard_out)>3:
        webhook.send(time.ctime()+" API Online")
        print(time.ctime()+" API Online")
        time.sleep(7200)
    else:
        webhook.send(time.ctime()+" API Offline")
        print(time.ctime()+" API Offline")
        #mailer.do_mail()
        time.sleep(7200)