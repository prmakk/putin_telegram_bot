from aiogram import types, Dispatcher, Bot, executor
import time
import random

TOKEN = '5768065044:AAGmR1-T6GB-2heWHQjIfqBVOvvfzCWF0-Q'

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_full_name = message.from_user.full_name
    await message.reply(f'Привіт козаче {user_full_name}. Теж чекаєш смерті путіна?')

    random_time = random.randrange(84000,87500)
    answer = 'на жаль, путін сьогодні не помер :('
    for i in range(365):
        time.sleep(random_time)
        await bot.send_message(chat_id, answer)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

