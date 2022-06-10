import requests

from bs4 import BeautifulSoup

import time


def telegram_bot_sendtext(bot_message):
    bot_token = '5279714454:AAGb0K3P8gVxLJCcB1aDsOSEtO89ZPNM9Rk'
    bot_chatID = '5391166849'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    responseTelegram = requests.get(send_text)

    return responseTelegram.json()


while True:

    try:

        url = "https://www.daft.ie/sharing/dublin?sort=publishDateDesc&rentalPrice_to=800"

        response = requests.get(url)

        html = response.content

        soup = BeautifulSoup(html, "html.parser")

        soup = soup.find("ul", {"data-testid": "results"})

        link = soup.a
        link.find_next_siblings("a")
        link = link.get('href')

        response.close()

        time.sleep(5)

        url = "https://www.daft.ie/sharing/dublin?sort=publishDateDesc&rentalPrice_to=800"

        response = requests.get(url)

        html = response.content

        soup = BeautifulSoup(html, "html.parser")

        soup = soup.find("ul", {"data-testid": "results"})

        ev = soup.stripped_strings

        evinfo = []

        link2 = soup.a
        link2.find_next_siblings("a")
        link2 = link2.get('href')
        linkson = "https://www.daft.ie" + link2

        for i in ev:
            evinfo.append(i)

        if link == link2:
            print("Yeni ev yok.\n ***********")
        else:
            telegram_bot_sendtext("daft.ie Yeni ilan: \n{}\n{}, {} {}\nLink: {}".format(evinfo[1], evinfo[2], "\n", evinfo[0], linkson))
            print("Telegrama gönderildi.")

        response.close()

    except:
        hata = "daft.ie - Hata oluştu, program 2 dakika sonra yeniden çalışacak."
        print(hata)
        telegram_bot_sendtext(hata)
        time.sleep(120)
        continue
