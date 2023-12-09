import os
import logging
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import ContextTypes, Application, CommandHandler, Update


# Lo primero sería recuperar el token desde el archivo .env, esto lo hacemos usando load_dotenv y os.getenv(’nombre_que_le_hayamos_puesto’)
load_dotenv()
tl_key = os.getenv("TELEGRAM_KEY")


# El logging, que nos va a permitir ver por consola los logs de nuestro bot y su actividad. 
# Este es un estandar que se suele utilizar para bots, NO es obligatorio para el funcionamiento, pero va a ser de mucha ayuda.
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(messages)s',
    level=logging.INFO)

application = Application.builder().token(tl_key).build()

# hacer que el bot se mantenga en ejecución.
application.run_polling()

# Primer Comando
# El comando más básico, para que nos devuelva un mensaje a la hora de activarlo desde Telegram.


# Usamos update y context nos brindan distintos tipos de información que recibe el bot. 
# Usamos async para asignar las funciones asíncronas y poder ejecutarla en cualquier momento.
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   
# Gracias al contexto que recibimos atenriormente, podemos indicarle al bot que envie un mensaje usando la función send_message, 
# la cual va a requerir de un chat id, basicamente saber QUIÉN envió el mensaje y hacia donde enviarlo. Podemos acceder a él gracias a update.effective_chat.id.
# Siguiente a eso, le ponemos el texto que queremos que envie. Usamos await para ejecutar finalmente la función.
     await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola Jona! te saluda myBot")
    
# Por último, dejamos por consola asentado lo que pasó. En este caso, gracias a la update podemos conseguir cual es el primer nombre de quien ejecutó el comando.
logging.info(f'El usuario: ({Update.message.chat.first_name}) ejecutó: start_command.')

# Una vez establecido el comando, hace falta vincularlo al bot. Utilizando nuestra instancia creada previamente y la función add_handler.
# a la izquierda, el nombre con el que queremos que se ejecute, a la derecha, como le pusimos en nuestro código.

application.add_handler(CommandHandler('start', start_command))