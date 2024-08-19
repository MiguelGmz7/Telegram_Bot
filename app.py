from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# Obtenemos las credenciales
with open('api_key.txt','r') as file:
    api_key = file.read()

with open('username.txt','r') as file:
    username = file.read()
