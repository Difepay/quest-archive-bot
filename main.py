import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8941329862:AAFvgoS4qco0p5NM1WD1ROFSzM1UhrJmhYE"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Система архива готова к работе.\nВведите команду, номер дела или ключ."
    )


@dp.message()
async def process_message(message: types.Message):
    text = message.text.strip().lower()
    words = text.split()

    if not words:
        return

    first_word = words[0]

    # --- СЕКЦИЯ: ДЕЛО ---
    if first_word == "дело":
        if len(words) < 2:
            await message.answer(
                "Укажите номер дела"
            )
            return

        case_num = words[1]

        # Проверка номера дела
        if case_num not in ["4", "12"]:
            await message.answer("Дело не найдено")
            return

        # Проверка наличия 3-го аргумента (кодового названия)
        if len(words) < 3:
            await message.answer(
                f"Для получения данных из архива по делу номер {case_num} нужно ввести его кодовое название после номера."
            )
            return

        # Собираем всё, что идет после номера дела (чтобы учесть фразы из двух слов)
        code_name = " ".join(words[2:])

        # Проверка кодового названия
        if case_num == "4":
            valid_codes = [
                "carpediem",
                "carpe diem",
                "ловимомент",
                "лови момент",
            ]
            if code_name in valid_codes:
                await message.answer(
                    "Доступ к Делу №4 разрешен. [Данные по делу №4]"
                )
            else:
                await message.answer("Кодовое название не подходит")

        elif case_num == "12":
            valid_codes = ["аладдин", "aladdin"]
            if code_name in valid_codes:
                await message.answer(
                    "Доступ к Делу №12 разрешен. [Данные по делу №12]"
                )
            else:
                await message.answer("Кодовое название не подходит")

    # --- СЕКЦИЯ: КЛЮЧ ---
    elif first_word == "ключ":
        if len(words) < 2:
            await message.answer("Укажите значение ключа.")
            return

        key_val = words[1]

        if key_val == "7721":
            await message.answer(
                "Пароль для расшифровки второго раздела Дела 19 - 678922"
            )
        elif key_val == "x":  # Подставь сюда нужный ключ позже
            await message.answer(
                "Пароль для расшифровки третьего раздела Дела 19 - 562371"
            )
        else:
            await message.answer("Неверный ключ.")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
