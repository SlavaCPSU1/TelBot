from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from Bot_command import *



app = ApplicationBuilder().token("").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum_command))
print('server start')
app.run_polling()