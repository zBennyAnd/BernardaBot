import telepot
from pprint import pprint
import sys, time
bot = telepot.Bot("")
print (bot.getMe())

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    content_type = 'text'
    print(content_type, chat_type, chat_id)
    pprint(msg)
#Comandi    
    if msg['text'] == "/leavechat":
        if msg['from']['id'] == 449342191:
            bot.leaveChat(chat_id=msg['chat']['id'])
        else:
            bot.sendMessage(chat_id = chat_id, text = "Non hai i permessi!")
    elif msg['text'] == '/help' or msg['text'] == '/HELP':
        bot.sendMessage(chat_id = chat_id, text = "Ciao, eccoti una lista dei miei comandi:\n/start\n/ban\n/leavechat")
    elif msg['text'] == '/start' or msg['text'] == '/START':
         bot.sendMessage(chat_id = chat_id, text= 'Ciao ' + str(msg['from']['username']))
    elif msg['text'] == '/ban' or msg['text'] == '/BAN':
         bot.kickChatMember(chat_id, msg['reply_to_message']['from']['id'])
    elif msg['text'] == '/caramella' or msg['text'] == '/CARAMELLA':
         bot.sendPhoto(chat_id, "http://www.svapo.it/media/kunena/attachments/8216/gelo-menta-caramella.png")
    elif msg['text'] == '/pacchetto' or msg['text'] == '/PACCHETTO':
        bot.sendPhoto(chat_id, "http://www.incap.it/upload/prodotti/immagini/menta%20gelo.png")
    elif msg['text'] == '/scarta' or msg['text'] == '/SCARTA':
        bot.sendPhoto(chat_id, "http://www.datamanager.it/wp-content/uploads/2014/04/bambino-mangia-solo-caramelle-menta-800x500_c.jpg")
    elif msg['text'] == '/puzza' or msg['text'] == '/PUZZA':
        bot.sendPhoto(chat_id, "https://images-na.ssl-images-amazon.com/images/I/71G3Ef0%2BCTL._SL1500_.jpg")
    elif msg['text'] == '/flash' or msg['text'] == '/FLASH':
        bot.sendVideo(chat_id, "http://vignette2.wikia.nocookie.net/nonciclopedia/images/c/c6/Gatto_sparaflesciato.gif/revision/latest?cb=20121013150008") 
    elif msg['text'] == '/zit' or msg['text'] == '/ZIT':
        bot.sendPhoto(chat_id, "http://www.dailyexcelsior.com/wp-content/uploads/2015/10/143.jpg")
    elif msg['text'] == '/sad' or msg['text'] == '/SAD':
        bot.sendVideo(chat_id, "https://media.giphy.com/media/3ohrypGmT9bFovUzmM/giphy.gif")
    elif msg['text'] == '/ignoranza' or msg['text'] == '/IGNORANZA':
        bot.sendVideo(chat_id, "https://2.bp.blogspot.com/-F4jszpW691M/WC91ORuwsoI/AAAAAAAAB-c/rtFnTYmQRLAdv4ThqRYj8qLoWmtEcg6egCLcB/s1600/Animated-GIF-Banana.gif")
    elif msg['text'] == '/angry' or msg['text'] == '/ANGRY':
        bot.sendVideo(chat_id, "https://media.giphy.com/media/11tTNkNy1SdXGg/giphy.gif")

#Salvare gli id e gli username in un file
    with open('id.txt', 'r') as utenti:
        utenti = utenti.read()
        if str(msg['from']['id']) not in utenti:
            bot.sendMessage(chat_id = chat_id, text = "Ciao, grazie per avermi scritto, il mio creatore ti risponderà al più presto!")
            id = open('id.txt', 'a')
            id.write("\r\n" + str(msg['from']['id']) + " " + str(msg['from']['username']))
            id.close
            bot.forwardMessage(chat_id = 449342191, from_chat_id=msg['from']['id'], message_id=msg['message_id'], disable_notification=False)
            
    

        
bot.message_loop(on_chat_message)


    

while 1:
    time.sleep(1)
