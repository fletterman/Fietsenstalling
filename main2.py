import telebot
import time
bot_token = "878137494:AAFq1YmAoh4bMGXeUBPM90hTJUMNdivlqw4"
bot = telebot.Telebot(token=bot_token)
@bot.message_handler(commands=['start'])
def send_welcome(mesage):
    bot.reply