from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# Obtenemos las credenciales
with open('api_key.txt','r') as file:
    api_key = file.read()

with open('username.txt','r') as file:
    username = file.read()

# Commands
async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bienvenido, cuenta tu problema')

async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Aqui estamos para ayudarte')

# Responses
def handle_response(text:str) -> str:

    p_response: str = text.lower()

    if "hello" in p_response:
        return "Helloworld"
    
    if "Como te llamas?" in p_response:
        return "NO TENGO NOMBRE NI APELLIDO"
    
    return "No te entendi"

# using the api to control the bot
async def handle_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type # group o private
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: {text}') # user id que manda el mensaje || User(miguel) in (group): Helloworld

    if message_type == 'group':
        if username in text:
            new_text: str = text.replace(username,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    # debbuging
    print('Bot', response)
    await update.message.reply_text(response) # manejamos la api para contestar


# api error
async def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# app

if __name__ == '__main__':

    print("Iniciando el bot...")

    # usamos el token 
    app = Application.builder().token(api_key).build()

    # iniciamos los comandos que vamos a usar 
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))


    # Mensajes que puede responder
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #Errors
    app.add_error_handler(error)

    # Revisa cada cuanto tiempo llegan nuevos mensajes
    print("polling....")
    app.run_polling(poll_interval=3)