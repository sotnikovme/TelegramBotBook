import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    kb=[
    [types.KeyboardButton(text="✅Купить книгу")],
     [types.KeyboardButton(text="✅Прочитать отрывок")],
     [types.KeyboardButton(text="✅Узнать об авторе")]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(f"👋 Привет, {message.from_user.username}!\n"
                     "\n"
                     "📖 Ты попал(а) в бота книги Набережные Члены\n"
                     "\n"
                     "Я работал на этой книгой....."
                     "Книгу с написал, когда был пьян...\n"
                     "Ну блин всё\n"
                     "\n"
                     "✨ Что ты можешь сделать прямо сейчас?\n"
                     "✅ Купить книгу — погрузись в захватывающий мир [краткое описание книги].\n"
                     "✅ Прочитать отрывок — попробуй «на вкус» перед покупкой.\n"
                     "✅ Узнать об авторе — кто создал эту историю?\n"
                     "\n"
                     "💬 Если есть вопросы — смело пиши! Я всегда на связи.😊\n"
                    "\n"
                     "Чтобы открыть меню, жми /start❗❗❗\n"
                     "\n"
                     "Желаю приятного чтения!📚💫",
                         reply_markup=markup)


@dp.message(F.text.lower()=="✅купить книгу")
async def read(message: types.Message):
    await message.answer(
        "📜Жили были дед и баба\n"
        "ели кашу с молоком\n" 
        "рассердился дед на бабу\n"
        "бац по пузу кулаком\n"
        "а из пуза два арбуза \n"
        "покатились под кровать\n"
        "а из носа два матроса\n"
        "побежали танцевать\n"
        "А ЧТО ДАЛЬШЕ? 😏\n"
        "📖 Понравилось? Жми '✅Купить книгу' — узнаешь, чем всё закончилось!"
                         )


@dp.message(F.text.lower()=="✅прочитать отрывок")
async def buy(message: types.Message):
    await message.answer(
            "💎 Отличное решение перспективного человека!\n"
            "\n"
            "Ты только что сделал(а) шаг на пути к совершенству!🌟\n"
            "\n"
            "📲 Оплатить можно тут: [ссылка на оплату]\n"
            "💰 Цена: [X] руб. (или 'донат на кофе автору ☕')\n"
            "\n"
            "📬 После оплаты книга придет тебе в PDF/EPUB/TXT\n"
            "❗ Важно: Если письмо не пришло — проверь «Спам» или напиши мне!"
                         )


@dp.message(F.text.lower() == "✅узнать об авторе")
async def learn(message: types.Message):
    await message.answer(
        "❤️ Люблю Вету!!!\n"
        "❤️ Люблю Вету!!!\n"
        "❤️ Люблю Вету!!!\n"
        "❤️ Люблю Вету!!!\n"
        "❤️ Люблю Вету!!!\n"
        "❤️ Люблю Вету!!!\n"
        "❤️ Люблю Вету!!!\n"
        "❤️ Люблю Вету!!!\n"
        "❤️ Люблю Вету!!!\n"
        "❤️ Люблю Вету!!!\n"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())