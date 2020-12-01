from telebot import TeleBot

@bot.message_
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
