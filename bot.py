from aiogram import Bot, Dispatcher, executor, types
import random 

first = ['Сегодня - идеальный день для новых начинаний','Оптимальный день чтобы расслабиться и успокоиться','Важный день сегодня для тех, кто ценит своё время','Не стоит отвлекаться на мелкие проблемы, ведь сегодняшний день принесет что-то хорошее']
second = ['Но помните, что даже в этом случае нужно не забывать про','Если поедете куда-либо отдыхать, не забудьте про','Совершая покупку вспомните про','Перед выходом на улицу не забывайте про']
second_add = ['отношения с друзьями и близкими','работу и деловые вопросы','ценность своего времени','бережность к своим финансам']
third = ['Злые языки могут говорить вам, что вы поступаете неправильно, но слушать их сегодня не нужно','Умные люди никогда не будут влезать в чужие конфликты без необходимости','Всегда можно отложить маленькие проблемы на потом, но забывать про них не стоит','Любая неожиданность принесет свои плоды, пусть и не всегда положительные']

API_TOKEN = "5899157536:AAHj0NWIjYakz7EBF5rRpsOvMKgV5LLMp5Y"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f'Я бот. Приятно познакомиться, {message.from_user.first_name}\nЧтобы получить гороскоп напишите /goroskop \nДля вызова помощи напишите /help')

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    user = message.from_user
    await message.answer(f"Ваше имя: {user.first_name} \nВаша фамилия: {user.last_name}\nНапишите /start для начала работы бота \nДля получения своего гороскопа на сегодня введите /goroskop \nА можете просто поздороваться :)")

@dp.message_handler(commands=['goroskop'])
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, text='Привет, сейчас расскажу тебе гороскоп')
    keyboard = types.InlineKeyboardMarkup()
    key_oven = types.KeyboardButton(text='Овен', callback_data='zodiac')
    keyboard.add(key_oven)
    key_telec = types.KeyboardButton(text='Телец', callback_data='zodiac')
    keyboard.add(key_telec)
    key_bliznecy = types.KeyboardButton(text='Близнецы', callback_data='zodiac')
    keyboard.add(key_bliznecy)
    key_rak = types.KeyboardButton(text='Рак', callback_data='zodiac')
    keyboard.add(key_rak)
    key_lev = types.KeyboardButton(text='Лев', callback_data='zodiac')
    keyboard.add(key_lev)
    key_deva = types.KeyboardButton(text='Дева', callback_data='zodiac')
    keyboard.add(key_deva)
    key_vesy = types.KeyboardButton(text='Весы', callback_data='zodiac')
    keyboard.add(key_vesy)
    key_scorpion = types.KeyboardButton(text='Скорпион', callback_data='zodiac')
    keyboard.add(key_scorpion)
    key_strelec = types.KeyboardButton(text='Стрелец', callback_data='zodiac')
    keyboard.add(key_strelec)
    key_kozerog = types.KeyboardButton(text='Козерог', callback_data='zodiac')
    keyboard.add(key_kozerog)
    key_vodoley = types.KeyboardButton(text='Водолей', callback_data='zodiac')
    keyboard.add(key_vodoley)
    key_ryby = types.KeyboardButton(text='Рыбы', callback_data='zodiac')
    keyboard.add(key_ryby)
    await bot.send_message(message.from_user.id, text="Выбери свой знак зодиака", reply_markup=keyboard)

@dp.callback_query_handler(run_task=lambda call: True)
async def callback_worker(call):
    if call.data == 'zodiac':
        msg = random.choice(first) + ' \n' + random.choice(second) + ' ' + random.choice(second_add) + ' \n' + random.choice(third)
        await bot.send_message(call.message.chat.id, msg + ' /start')

@dp.message_handler(content_types='text')
async def send_hello(msg : types.Message):
    if msg.text.lower() == 'привет' or msg.text.lower() == 'привет!':
        await msg.answer('Привет, если хочешь узнать свой гороскоп введи /goroskop')
    else:
        await msg.answer('Я не понял, что ты сказал, попробуй еще раз')

if __name__ == '__main__':
    executor.start_polling(dp)
