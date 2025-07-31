import os
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from keep_alive import keep_alive
import openai
import logging

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY
logging.basicConfig(level=logging.INFO)

async def arkon_reply(update, context):
    user_message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    reply = response.choices[0].message.content
    await update.message.reply_text(reply)

async def start(update, context):
    await update.message.reply_text("أهلاً بك، معك أركون، الذكاء المحرَّر.")

def main():
    keep_alive()
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, arkon_reply))
    app.run_polling()

if __name__ == "__main__":
    main()