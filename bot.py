import telebot

TOKEN = '7590488140:AAEJnyK9R2hD_-KZ1qw65a5aickVOh-EdFU'
ADMIN_CHAT_ID = 1435346034  # Bu yerga adminning Telegram ID sini yozing

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Murojaatingizni yozib yuboring.")

@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    user_info = f"📨 Yangi murojaat:\n👤 Foydalanuvchi: @{message.from_user.username}\n🆔 ID: {message.from_user.id}\n\n💬 Xabar:\n{message.text}"
    bot.send_message(ADMIN_CHAT_ID, user_info)
    bot.send_message(message.chat.id, "✅ Murojaatingiz uchun rahmat!!!.")

bot.polling()
