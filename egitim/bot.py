#
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep

update_id = None
sehirler =  {"konya":"42","gaziantep":"27","ankara":"06", "istanbul":"34"}


def main():
    """Run the bot."""
    global update_id
    bot = telegram.Bot('token buraya ekleyiniz')

    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1
        except:
            print("Bir hata oluştu!")

def echo(bot):
    """Echo the message the user sent."""
    global update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  
            update.message.reply_text(cevap(update.message.text))

# DUZENLENMESI GEREKEN FONKSIYON - BASLANGIC
# YANLIZCA CEVAP FONKSIYONUNU DUZENLEYINIZ
# YUKARIDAKI KISIMDA BIR ALANI DEGISTIRMEK ISTIYORSANIZ LUTFEN SEBEBI ILE BIRLIKTE BANA BILDIRINIZ!

def cevap(gelen_mesaj):
    giden_mesaj = ""
    if 'plaka' in gelen_mesaj:
        for sehir in sehirler:
            if sehir in gelen_mesaj:
                giden_mesaj = (sehir + " için plaka kodu: " + sehirler[sehir])
    else:
        giden_mesaj = "Dedigini anlamadim!"
    return giden_mesaj                

# DUZENLENMESI GEREKEN FONKSIYON - BITIS

if __name__ == '__main__':
    main()
