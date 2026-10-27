import os
import urllib.parse
import urllib.request

token = os.environ["TELEGRAM_TOKEN"]
chat = os.environ["TELEGRAM_CHAT_ID"]
texto = "Bot de carros funcionando ✅"
datos = urllib.parse.urlencode({"chat_id": chat, "text": texto}).encode()
urllib.request.urlopen(f"https://api.telegram.org/bot{token}/sendMessage", data=datos)
print("ok")
