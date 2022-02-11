from threading import Thread
from json_helpers import retrieve_db
from template_check import template_tick
from datetime import datetime
from telegram_bot import bot

from keep_alive import keep_alive
keep_alive()


latest_check = datetime.now()
TICK_TIME = 60 * 60 * 1
def tick():
    """
    The tick function that ticks every TICK_TIME seconds.
    It runs in a thread while calling each tick function.
    
    Parameters:
        None
                
    Returns:
        None
    """
    global latest_check
    while True:
        if (datetime.now() - latest_check).seconds >= TICK_TIME:
            latest_check = datetime.now()
            print("*** Time to poll monitors...")

            output_messages = [
                template_tick(), # Returns a dict {"update": bool, "message": str}
            ]
            
            current_users = retrieve_db('current_users')
            for i in current_users:
                for j in output_messages:
                    if j['update']: 
                        bot.send_message(i, j["message"], parse_mode='Markdown')


ticker = Thread(target=tick)
ticker.start()
bot.polling()