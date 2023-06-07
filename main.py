import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Устанавливаем уровень логов на DEBUG, чтобы видеть все сообщения об ошибках и действиях бота
logging.basicConfig(level=logging.DEBUG)

# Создаем объекты бота и диспетчера
bot = Bot(token='6137593881:AAHkxWi1aimz5x9wpr-hgxrLFKcgdqkWAaY')

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Я эхо-бот. Отправь мне сообщение, и я повторю его.")

# Кто написал книгу Тоджикон
@dp.message_handler(text='1')
async def w1(message: types.Message):
    await message.reply('''
1. Б.Ғафуров барои кадом хизматҳои шоён ба унвони олии Қаҳрамони Тоҷикистон мушарраф гардидааст?
Бо фармони Президенти Ҷумҳурии Тоҷикистон Эмомалӣ Раҳмон 8.09.1997 барои хизматҳои бузург ва фидокориҳо дар поягузории Истиқлолияти Тоҷикистон, рушди тамаддун ва худшиносии миллӣ ба фарзанди фарзонаи миллат унвони олии Қаҳрамони Тоҷикистон дода шуд.
    ''')

# Обработчик всех остальных сообщений
@dp.message_handler()
async def echo_message(message: types.Message):
    # Отправляем текст полученного сообщения в ответ
    await message.answer(f'Извините вопрос "{message.text}" не найденно.')


# Запускаем бота
if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
