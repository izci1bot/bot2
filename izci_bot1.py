from telebot import TeleBot
from bs4 import BeautifulSoup
import requests


bot = TeleBot("1229478827:AAHKwARIFOP-G5iMf_rDUXyPNzTK-o69lTo")

@bot.message_handler(commands=["doviz"])
def start_mesaj(m):
    print("saddasads")
    r = requests.get("https://altin.in/fiyat/gram-altin")

    soup = BeautifulSoup(r.content, "html.parser")

    dolar = soup.find("h2", attrs={"id":"dfiy"})

    euro = soup.find("h2", attrs={"id":"efiy"})

    sterlin = soup.find("h2", attrs={"id":"sfiy"})

    altin_alis = soup.find("li", attrs={"title":"Gram Altın - Alış"})

    altin_satis = soup.find("li", attrs={"title":"Gram Altın - Satış"})

    bilgi = f"Dolar: {dolar.text}\nEuro: {euro.text}\nSterlin: {sterlin.text}\nAltın: \nAlış = {altin_alis.text}\nSatış = {altin_satis.text}"

    bot.reply_to(m, bilgi)

bot.polling()