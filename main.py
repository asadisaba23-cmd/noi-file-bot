import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
ARCHIVE_CHANNEL_ID = os.environ["ARCHIVE_CHANNEL_ID"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("لینک فایل معتبر نیست")
        return

    try:
        message_id = int(context.args[0])
        await context.bot.copy_message(
            chat_id=update.effective_chat.id,
            from_chat_id=ARCHIVE_CHANNEL_ID,
            message_id=message_id
        )
    except Exception:
        await update.message.reply_text("فایل پیدا نشد یا لینک اشتباه است")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
