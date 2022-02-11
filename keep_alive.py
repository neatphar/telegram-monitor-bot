"""
This makes use of Repl.it's (waking up to HTTP requests) feature.
TODO: Set up a uptimerobot.com to frequently wake up the repl.
"""

from flask import Flask
from threading import Thread

from flask import cli
cli.show_server_banner = lambda *_: None

app = Flask('')

@app.route('/')
def main():
    return "This bot is alive!"

def run():
    app.run(host="0.0.0.0")

def keep_alive():
    server = Thread(target=run)
    server.start()