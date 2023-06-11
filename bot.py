import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO, filename="bot_log.log", filemode="w")

bot = Bot(token = os.environ.get("TOKEN"))
dp = Dispatcher(bot, storage=MemoryStorage())

def breaks_delete(text):
    return(text.replace('\n', ' '))

@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello! I'm a bot to help you remove line breaks. I can come in handy when directly copying text from articles in pdf format.")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, breaks_delete(msg.text))

async def main():
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
