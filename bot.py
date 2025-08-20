import telebot
import qrcode

token = '7272291988:AAHXqiCK4TgG8aj6PLWBz3FB2CEd5EnvTCY'

bot = telebot.TeleBot(token)

welcome_text = """🎉 *Добро пожаловать в QRCode Generator Bot!* 🎉

Я помогу тебе создать крутые QR-коды! 

📋 *Доступные команды:*
/generate [текст] - Создать обычный QR-код

💡 *Примеры:*
/generate Привет, мир!
/generate https://example.com

Создавай QR-коды для ссылок, текстов и многого другого! 🚀"""
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, (welcome_text))
        bot.send_message(message.chat.id, ("Пример:"))
        bot.send_message(message.chat.id, ("/generate Привет, как дела?"))
    if len(message.text) >= 10 and "/generate " in message.text:
        msg = message.text[10:]
        img = qrcode.make(msg)
        img.save('Qr.png')
        bot.send_photo(
            message.chat.id,
            photo=open('Qr.png', 'rb'),
            caption="Ваш QRcode успешно сгенерирован!"
        )
    elif message.text != "/start":
        bot.send_message(message.chat.id, ("Невозможно сгенерировать qrcode"))

bot.infinity_polling()