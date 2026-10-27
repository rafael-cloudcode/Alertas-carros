import os
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT = os.environ["TELEGRAM_CHAT_ID"]
URL = "https://columbus.craigslist.org/search/cta?format=rss&min_price=500&max_price=6000&query=honda"


def telegram(texto):
    datos = urllib.parse.urlencode({"chat_id": CHAT, "text": texto}).encode()
    urllib.request.urlopen(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data=datos)


req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
    root = ET.fromstring(data)
except Exception as e:
    telegram(f"Craigslist falló: {e}")
    raise SystemExit

items = [e for e in root.iter() if e.tag.endswith("item")]
lineas = []
for it in items[:3]:
    titulo = next((c.text for c in it if c.tag.endswith("title")), "")
    link = next((c.text for c in it if c.tag.endswith("link")), "")
    lineas.append(f"{titulo}\n{link}")

telegram(f"Craigslist OK: {len(items)} anuncios.\n\n" + "\n\n".join(lineas))
