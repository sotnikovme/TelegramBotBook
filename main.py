import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    kb=[
     [types.KeyboardButton(text="Стоит ли прочесть?🧐")],
    [types.KeyboardButton(text="Купить книгу🤑")],
     [types.KeyboardButton(text="Пользовательское соглашение🧑‍💻")]
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


@dp.message(F.text.lower()=="стоит ли прочесть?🧐")
async def read(message: types.Message):
    await message.answer(
        "5 причин, из-за чего Ваши мечты станут достижимы с этой книгой:\n"
        "1️⃣ Книга содержит универсальные методы с практическими заданиями для выявления индивидуальных потребностей.\n"
        "2️⃣ Умные вещи написаны понятным языком.\n"
        "3️⃣ Восприятие книги улучшается из-за обилия ярких жизненных примеров.\n"
        "4️⃣ Здесь отражены мудрые правила жизни, которые закономерно выделяют самые успешные люди из разных сфер деятельности.\n"
        "5️⃣ Фактически это Ваше личное руководство в мире возможностей, актуальное во все времена.\n"
                         )


@dp.message(F.text.lower()=="купить книгу🤑")
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


@dp.message(F.text.lower() == "пользовательское соглашение🧑‍💻")
async def learn(message: types.Message):
    await message.answer(
        "Должен..."
        "Должен..."
        "Должен..."
        "Должен..."
        "Должен..."
        "Должен..."
        "Должен..."
        "Должен..."
        "Должен..."
        "Должен..."
    )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())