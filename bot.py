# bot.py
import telebot
from buscador import buscar_y_procesar

# ⚠️ Coloca aquí tu token real de Telegram
TOKEN = "8421638351:AAG7zBomi8eMPtBiNwbzDBCqrg5wTcDW69M"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 ¡Hola! Usa /buscar <nombre> para encontrar una carta Pokémon EX.\n"
                          "Ejemplo: /buscar Lillie's Clefairy ex")

@bot.message_handler(commands=['buscar'])
def buscar(message):
    try:
        partes = message.text.split(maxsplit=1)
        if len(partes) < 2:
            bot.reply_to(message, "❗ Usa el comando así:\n/buscar <nombre de la carta>")
            return

        entrada = partes[1]
        resultado = buscar_y_procesar(entrada)
        bot.reply_to(message, resultado)
    except Exception as e:
        bot.reply_to(message, f"⚠️ Ocurrió un error: {e}")

# Ejecuta el bot
if __name__ == "__main__":
    print("🤖 Bot en ejecución...")
    bot.infinity_polling()
