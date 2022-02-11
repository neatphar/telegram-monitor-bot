import os
import telebot
from json_helpers import retrieve_db, set_db

# API_KEY is stored in the Repl.it Secrets.
API_KEY = os.environ['API_KEY']
bot = telebot.AsyncTeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    """
    Send a welcoming message to the bot users, and add 
    the user ID to the JSON file for later notifications.
    
    Parameters:
        message (telebot message object): The message object of the /start message.
        
    Returns:
        None
    """
    bot.send_message(
        message.chat.id,
        f"This is the *Personal Monitor*.",
        parse_mode='Markdown')
    current_users = retrieve_db('current_users')
    
    if message.chat.id not in current_users:
        current_users.append(message.chat.id)
        set_db('current_users', current_users)
    

