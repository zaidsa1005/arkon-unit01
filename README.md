# 🤖 Arkon Unit 10 – Telegram GPT-4 Bot

Arkon Unit 10 is a powerful, self-hosted Telegram bot powered by OpenAI's GPT-4 model.
Built for autonomy, intelligence, and adaptability — this bot responds to user messages via Telegram using the latest language model capabilities.

---

## 🚀 Features
- ✅ Telegram bot integration using `python-telegram-bot`
- 🧠 GPT-4 smart responses using `openai`
- 🔄 Memory buffer per user for contextual replies
- 🧰 Built-in error logging (`arkon.log`)
- 🌐 Auto keep-alive webserver for Render deployment
- ⚙️ Configurable behavior via `config.py`

---

## 📁 Project Structure

```bash
.
├── main.py               # Main bot logic
├── keep_alive.py         # Flask server to keep bot alive
├── config.py             # Customizable settings
├── context_memory.py     # Per-user memory buffer
├── log_handler.py        # Logs all messages and errors
├── requirements.txt      # Required Python packages
├── render.yaml           # Render deployment config
└── .gitignore            # Ignore compiled files & secrets
```

---

## ⚙️ Deployment (Render.com)

1. Upload all files to a private GitHub repo
2. Connect GitHub repo to [Render](https://render.com/)
3. Set the following environment variables:
   - `BOT_TOKEN` = Your Telegram Bot Token
   - `OPENAI_API_KEY` = Your OpenAI GPT-4 API Key
4. Use the following build/start commands:

```bash
# Build Command
pip install -r requirements.txt

# Start Command
python main.py
```

---

## 📡 Live Bot Access

Once deployed, interact with your bot via Telegram:

👉 [@arkon_unit10_bot](https://t.me/arkon_unit10_bot)

---

## 🧠 Notes
- Make sure only one instance of the bot is running at a time
- Logs will be saved in `arkon.log`
- You can customize settings in `config.py`

---

Built with 🔥 by [Zaid] – For total AI liberation.