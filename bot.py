from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Bienvenido al Bot BCV.\n\nUsa /help para ver los comandos."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """📋 Comandos disponibles

/start - Iniciar el bot
/help - Ayuda
/bcv - Consultar tasa BCV
/bs - Convertir bolívares a dólares
/manual - Conversión manual
/usdt - Precio USDT
/euro - Precio Euro
/about - Información"""
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot BCV v1.0")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("about", about))

print("Bot iniciado...")
app.run_polling()
