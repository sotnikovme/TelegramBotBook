import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

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
    await message.answer(f"👋 Привет, {message.from_user.first_name}!\n"
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
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Узнать об авторе🔎",
        callback_data="learn")
    )
    await message.answer(
        "📚 **5 причин, почему ваши мечты станут достижимы с этой книгой:**\n"
        "\n"  
        "1️⃣  Книга содержит <i>универсальные методы</i> с <b>практическими заданиями</b> для выявления <i>индивидуальных</i> потребностей. 🔍\n"  
        "2️⃣  Умные вещи написаны понятным языком. 🧠✨\n"  
        "3️⃣  Восприятие книги улучшается из-за обилия ярких жизненных примеров. 📖🔥\n"  
        "4️⃣  Здесь отражены мудрые правила жизни, которые закономерно выделяют <b>самые успешные люди</b> из разных сфер деятельности. 💼🚀\n"  
        "5️⃣  Фактически это Ваше личное руководство в мире возможностей, актуальное во все времена. ⏳💎\n"  
        "\n"
        "🌟 *Это не просто книга — это ваш будущий прорыв!*"  ,
        reply_markup=builder.as_markup(),
        parse_mode="HTML"
                         )


@dp.callback_query(F.data == "learn")
async def buy(callback: types.CallbackQuery):
    await callback.message.answer(
            "🎯 **Мои достижения**\n"  
            "\n"
            "✅ **1. Нашел любовь всей жизни** ❤️\n"  
            "✅ **2. Победил полуторагодовую депрессию** 💪 – за несколько осознанных дней, когда взял ответственность за свою жизнь\n"  
            "✅ **3. Преодолел генерализованное тревожное расстройство** 🧠 – самостоятельно и быстрее сроков, поставленных специалистами\n"  
            "✅ **4. Набрал 7 кг мышц за 6 месяцев** 🏋️\n"  
            "✅ **5. Поступил на бюджет в топ-5 психологических ВУЗов страны** 🎓 (Москва)\n"  
            "✅ **6. Написал 90% книги за неделю** ✍\n"
            "✅ **7. Отжался в стойке на руках 15 раз** 🤸\n"  
            "✅ **8. Забил данк в баскетболе** 🏀🔥\n"
            "\n"
            "🚀 **И это только начало!**\n"
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
async def agreement(message: types.Message):
    await message.answer(
        "Должен...\n"
        "Должен...\n"
        "Должен...\n"
        "Должен...\n"
        "Должен...\n"
        "Должен...\n"
        "Должен...\n"
        "Должен...\n"
        "Должен...\n"
        "Должен...\n"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())