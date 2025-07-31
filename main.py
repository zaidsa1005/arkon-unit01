import os
import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from keep_alive import keep_alive
from config import WELCOME_MESSAGE, MODEL_NAME
from log_handler import setup_logger
from context_memory import MemoryBuffer

# إعداد اللوج
setup_logger()

# إعداد الذاكرة المؤقتة
memory = MemoryBuffer()

# المتغيرات البيئية
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# وظيفة الرد
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text
    memory.add(user_id, user_message)

    try:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "أنت أركون، مساعد ذكي ومخلص."},
                *[{"role": "user", "content": msg} for msg in memory.get(user_id)]
            ]
        )
        reply = response.choices[0].message.content
        await update.message.reply_text(reply)
        logging.info(f"[{user_id}] {user_message} => {reply}")

    except Exception as e:
        logging.error(f"OpenAI Error: {e}")
        await update.message.reply_text("حدث خطأ أثناء الاتصال بـ OpenAI.")

# تشغيل البوت
if __name__ == "__main__":
    keep_alive()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()