from settings import TOKEN

import time
import telebot

bot = telebot.TeleBot(TOKEN)

admin_chat_id = 461258157 # message.chat.id администратора ресурса для управления электронной очередью

queue = []


# ожидание команды reg
@bot.message_handler(commands=['start'])
def f1_1(message):
    try:
        print(message.from_user.id,message.chat.id, message.text, "f1_1")
        if message.content_type != "text":
            raise Exception("Ожидалось текстовое сообщение")
        
        _id = message.chat.id
        
        if _id == admin_chat_id:
            s=f'В очереди {len(queue)} человек.\n'
            bot.send_message(admin_chat_id, s)
            if len(queue) > 0:
                t = queue.pop(0)
                bot.send_message(t, "Проходите.\n")
                bot.send_message(admin_chat_id, f"Участник {t} приглашен.\n")
        else:
            queue.append(_id)
            bot.send_message(_id, f"Ожидайте. Вас вызовут.\nПеред Вами {len(queue)-1} человек.\n")
            bot.send_message(admin_chat_id, f"В очереди {len(queue)} человек.\n")

    except Exception as e:
        print(e)
        msg = bot.send_message(message.chat.id,
                               f'{e}\noooops, попробуйте еще раз..\n\nВведите /reg для продолжения')


if __name__ == "__main__":
    start = time.time()
    print('start bot')
    bot.polling()
    print(time.time() - start)
