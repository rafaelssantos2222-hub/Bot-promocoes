import requests
import time
import random

# 🔑 coloque seu token aqui (BotFather)
TOKEN = "8491561897:AAG2K1jTho6YIg3waHsqpi3VNMXkGI0Va6Q"

# 📢 coloque seu canal aqui
CANAL = "@promocoesrelampag1"

promocoes = [
    "🔌 Carregador turbo baratinho hoje! https://meli.la/1rJL3ee",
    "🎧 Fone Bluetooth em oferta! https://meli.la/2NWAaXM",
    "📱 Celular com desconto! https://meli.la/1Kv6msC"
]

while True:
    msg = random.choice(promocoes)

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CANAL, "text": msg}
    )

    time.sleep(60 * 30)
