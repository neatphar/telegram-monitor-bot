<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/FxL5qM0.jpg" alt="Bot logo"></a>
</p>

<h3 align="center">Telegram Monitor Bot</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Platform](https://img.shields.io/badge/platform-telegram-blue.svg)](https://www.telegram.org/)
[![GitHub Issues](https://img.shields.io/github/issues/neatphar/telegram-monitor-bot.svg)](https://github.com/neatphar/telegram-monitor-bot/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/neatphar/telegram-monitor-bot.svg)](https://github.com/neatphar/telegram-monitor-bot/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🤖 A personal customized monitor that utilizes Telegram as a notification platform.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [How it works](#working)
- [Usage](#usage)
- [Deploying your own bot](#deployment)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your bot.

## 💭 How it works <a name = "working"></a>

The bot first extracts the word from the comment and then fetches word definitions, part of speech, example and source from the Oxford Dictionary API.

If the word does not exist in the Oxford Dictionary, the Oxford API then returns a 404 response upon which the bot then tries to fetch results form the Urban Dictionary API.

The bot uses the Pushshift API to fetch comments, PRAW module to reply to comments and Heroku as a server.

The entire bot is written in Python 3.6

## 🎈 Usage <a name = "usage"></a>

To use the bot, type:

```
!dict word
```

The first part, i.e. "!dict" **is not** case sensitive.

The bot will then give you the Oxford Dictionary (or Urban Dictionary; if the word does not exist in the Oxford Dictionary) definition of the word as a comment reply.

### Example:

> !dict what is love

**Definition:**

Baby, dont hurt me~
Dont hurt me~ no more.

**Example:**

Dude1: Bruh, what is love?
Dude2: Baby, dont hurt me, dont hurt me- no more!
Dude1: dafuq?

**Source:** https://www.urbandictionary.com/define.php?term=what%20is%20love

---

<sup>Beep boop. I am a bot. If there are any issues, contact my [Master](https://www.reddit.com/message/compose/?to=PositivePlayer1&subject=/u/Wordbook_Bot)</sup>

<sup>Want to make a similar reddit bot? Check out: [GitHub](https://github.com/kylelobo/Reddit-Bot)</sup>


## 🚀 Deploying your own bot <a name = "deployment"></a>

To see an example project on how to deploy your bot and make it available 24/7, please see check out the following tutorial:

[Building a Discord Bot with Python and Repl.it - **Codementor**](https://www.codementor.io/@garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz#setting-up-authorization-for-our-bot)

The tutorial discusses a Discord bot. However, this can still be used as a guide for a 24/7 running bot.

## ⛏️ Built Using <a name = "built_using"></a>

- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - Python Telegram API Wrapper
- [Repl.it](https://www.repl.it/) - An online IDE, Editor, Compiler, Interpreter, that can host code.

## ✍️ Authors <a name = "authors"></a>

- [@neatphar](https://github.com/neatphar) - Idea & Implementation.
