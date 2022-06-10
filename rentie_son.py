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

        url = "https://www.rent.ie/rooms-to-rent/renting_dublin/room-type_either/rent_0-800/sort-by_date-entered_down/"

        response = requests.get(url)

        html = response.content

        soup = BeautifulSoup(html, "html.parser")

        soup = soup.find("div", {"class": "search_result"})

        ev = soup.stripped_strings

        eskiev = []

        for i in ev:
            eskiev.append(i)

        eskiev2 = eskiev[1], eskiev[4], eskiev[5]

        response.close()

        time.sleep(10)

        response = requests.get(url)

        html = response.content

        soup = BeautifulSoup(html, "html.parser")

        soup = soup.find("div", {"class": "search_result"})

        ev2 = soup.stripped_strings

        yeniev = []

        for i in ev2:
            yeniev.append(i)

        yeniev2 = yeniev[1], yeniev[4], yeniev[5]

        link = soup.a
        link.find_next_siblings("a")
        link = link.get('href')

        if yeniev2 == eskiev2:
            print("Yeni ev yok.\n ***********")
        else:
            telegram_bot_sendtext("rent.ie Yeni ilan: \n{}\n{}, {}, {}\nLink: {}".format(yeniev[1], yeniev[4], yeniev[5], yeniev[6], link))
            print("Telegrama gönderildi.")

        response.close()

    except:
        hata = "rent.ie - Hata oluştu, program 2 dakika sonra yeniden çalışacak."
        print(hata)
        telegram_bot_sendtext(hata)
        time.sleep(120)
        continue
