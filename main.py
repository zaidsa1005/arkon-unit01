import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# إعداد مفاتيح OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG_ID")

# وظيفة الرد على الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # أو "gpt-4" إذا كان متاح
            messages=[
                {"role": "system", "content": "أنت مساعد ذكي."},
                {"role": "user", "content": user_message}
            ]
        )

        reply_text = response.choices[0].message.content
        await update.message.reply_text(reply_text)

    except Exception as e:
        await update.message.reply_text(f"حدث خطأ: {str(e)}")

# تشغيل البوت
if __name__ == "__main__":
    telegram_token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(telegram_token).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
