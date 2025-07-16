import requests
import time
from telegram import Bot

# 🔁 Reemplaza estos valores con los tuyos
TELEGRAM_TOKEN = '8189856365:AAFIhGxu9q6N8MYMkYlGRj8lkbwwPQeUNCw'
CHAT_ID = 5265836164  # sin comillas si es un número

bot = Bot(token=TELEGRAM_TOKEN)

# URL de la página oficial de citas
URL_CITA = 'https://icp.administracionelectronica.gob.es/icpplus/citar?p=21&locale=es'

def check_citas():
    try:
        response = requests.get(URL_CITA)
        if response.status_code == 200:
            html = response.text.lower()
            if "no hay citas disponibles" not in html:
                return True
        return False
    except Exception as e:
        print("Error:", e)
        return False

def main():
    while True:
        if check_citas():
            bot.send_message(chat_id=CHAT_ID, text="🚨 ¡Hay citas disponibles para renovar NIE en Huelva!")
            time.sleep(30)  # Espera 30 segundos si hay cita
        else:
            print("No hay citas todavía.")
            time.sleep(30)  # Revisa cada 30 segundos

if __name__ == "__main__":
    main()
