import requests
from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.from_url("https://discord.com/api/webhooks/898861270005071883/p5YDlpjsh1q-mRz641BKtTOnTd6WMlB10yp13Nok2kKlKqv1XOfasuuMIICPMedDF7lD", adapter=RequestsWebhookAdapter())
webhook.send("Hello World")