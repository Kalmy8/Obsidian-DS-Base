**Codewords:** Telegram Bot API, `aiogram`, Webhook, Polling, Environment Variables, `python-dotenv`, `dateparser`, `ngrok`.

## 1. How Telegram Bots Work

A Telegram bot is a special account that you can interact with by sending it messages, commands, and inline requests. You control your bots using HTTPS requests to the **Telegram Bot API**.

To create a bot, you need to talk to [@BotFather](https://t.me/botfather) on Telegram. It will guide you through the creation process and give you a **bot token**. This token is your bot's password—keep it secret!

### Receiving Updates: Polling vs. Webhooks

There are two ways your bot can get messages from users:
1.  **Polling:** Your application repeatedly asks Telegram, "Are there any new messages for me?". This is simple to set up for development but is inefficient. It makes many unnecessary requests.
2.  **Webhooks:** You provide Telegram with a public URL (an endpoint on your FastAPI server). Whenever there's a new message for your bot, Telegram sends an HTTP POST request with the update data to your URL. This is the preferred method for production as it's much more efficient.

### Storing Your Token Securely
You must **never** hardcode your bot token directly in your code. If you publish your code, your bot will be stolen. The standard practice is to use **environment variables**.

The `python-dotenv` library makes this easy for local development. It loads variables from a `.env` file into the environment.
```bash
pip install python-dotenv
```
Create a file named `.env` in your project root:
```
BOT_TOKEN="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
```
And in your code, you can load and access it:
```python
import os
from dotenv import load_dotenv

load_dotenv() # loads variables from .env file
BOT_TOKEN = os.getenv("BOT_TOKEN")
```

## 2. `aiogram`: The Bot Framework

`aiogram` is a modern, fully asynchronous framework for the Telegram Bot API written in Python with `asyncio` and `aiohttp`.

To get started:
```bash
pip install aiogram
```

## 3. The Project: Date-Parsing Bot

Now let's combine everything: FastAPI will be our web server to handle webhooks from Telegram, and `aiogram` will process the updates to provide the bot's logic. We will also use the `dateparser` library to find dates in text.

**Project Setup:**
1.  Install all necessary libraries:
    ```bash
    pip install fastapi "uvicorn[standard]" aiogram python-dotenv dateparser
    ```
2.  Create your bot with @BotFather and get your token.
3.  Create a `.env` file and add your `BOT_TOKEN`.
4.  Create a file named `bot_main.py`.

**The Code (`bot_main.py`):**
```python
import os
import logging
import dateparser
from dotenv import load_dotenv

from fastapi import FastAPI, Request, Response
from aiogram import Bot, Dispatcher, types

# --- Setup ---
# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
# This is the public URL for your webhook.
# For local testing, you'll need a tool like ngrok (see below).
WEBHOOK_URL = "https://your-public-domain-here.com/webhook"


# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Initialize FastAPI app
app = FastAPI()

# --- Bot Logic ---
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(
        "Hi!\nI'm DateParserBot!\n"
        "Send me a message with any dates in it, and I'll find them for you."
    )

@dp.message_handler()
async def parse_dates(message: types.Message):
    """
    This handler will be called for any text message.
    """
    # Use dateparser to find dates in the message text
    # The language order helps the parser prioritize e.g. English dates
    found_dates = dateparser.search.search_dates(
        message.text, languages=['en', 'ru']
    )

    if found_dates:
        # Format the found dates for the reply
        formatted_dates = [
            f"'{text}' -> {date.strftime('%Y-%m-%d %H:%M')}" for text, date in found_dates
        ]
        reply_text = "I found these dates:\n" + "\n".join(formatted_dates)
    else:
        reply_text = "I couldn't find any dates in your message."

    await message.reply(reply_text)


# --- Webhook Integration with FastAPI ---
@app.on_event("startup")
async def on_startup():
    """
    Actions to be performed when the application starts.
    Sets the webhook.
    """
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)
    logging.info("Webhook set to %s", WEBHOOK_URL)

@app.post("/webhook")
async def webhook(request: Request):
    """
    This endpoint will receive updates from Telegram.
    """
    # Get the update from the request body and process it with aiogram
    update = await request.json()
    await dp.process_update(types.Update(**update))
    # Return a 200 OK response to Telegram
    return Response(status_code=200)


@app.on_event("shutdown")
async def on_shutdown():
    """
    Actions to be performed when the application shuts down.
    Removes the webhook.
    """
    await bot.delete_webhook()
    logging.info("Webhook deleted.")

```
### Running the Project with `ngrok`

For Telegram to send updates to your webhook, your application must be running on a public URL. During development, you can use a tool called **`ngrok`** to create a secure public URL for your local server.

1.  [Download and install ngrok](https://ngrok.com/download).
2.  Run your FastAPI app: `uvicorn bot_main:app --host 0.0.0.0 --port 8000`
3.  In a new terminal, run ngrok to expose port 8000: `ngrok http 8000`
4.  ngrok will give you a public URL like `https://abcdef12345.ngrok.io`.
5.  **Copy this URL**, update the `WEBHOOK_URL` in your `bot_main.py` file to be `https://abcdef12345.ngrok.io/webhook`, and restart your uvicorn server.

Now your bot should be live and responding to messages!

---
#🃏/backend-basics
**Key Questions:**

1. What are the two methods for a Telegram bot to receive messages? What are the pros and cons of each?
?
- **Polling:** The bot repeatedly asks Telegram for updates.
    - **Pros:** Simple to set up for local development.
    - **Cons:** Inefficient, makes many useless requests, and has a delay.
- **Webhooks:** Telegram sends updates to a public URL you provide.
    - **Pros:** Very efficient, real-time updates, scalable for production.
    - **Cons:** Requires a public URL and a web server, making setup more complex.

2. Why should you never hardcode your bot token in your source code?
?
- The bot token is a secret password. If it's in your source code and you publish it (e.g., on GitHub), anyone can find it and take control of your bot. It should be stored securely, for example, in an environment variable.

3. What is a webhook and how does it work with FastAPI and a Telegram bot?
?
- A webhook is a mechanism where a server (Telegram) automatically sends real-time data to another application when an event occurs.
- With FastAPI, you create an endpoint (e.g., `/webhook`) that acts as the public URL. You tell Telegram this URL. When a user messages your bot, Telegram sends an HTTP POST request to your FastAPI endpoint. Your FastAPI application then processes this request, passing the data to `aiogram` to handle the bot's logic.

4. What role does a tool like `ngrok` play in bot development?
?
- Telegram webhooks require a public HTTPS URL. When developing on your local machine, your server is only accessible at `localhost`. `ngrok` creates a secure public URL that tunnels to your local server, allowing Telegram to reach your application for testing and development. 