from aiogram import types
from keyboards.default.buttons import wikipediya_button
from keyboards.default.buttons import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import wikipedia
from loader import dp, bot
wikipedia.set_lang("uz")
# Wikipedia holati
class WikiState(StatesGroup):
    searching = State()

# Wikipediyaga kirish
@dp.message_handler(lambda message: message.text.lower() == "wikipediyaga kirish", state=None)
async def enter_wiki_mode(message: types.Message):
    await message.answer(
        "Wikipedia rejimiga kirdingiz. Qidirayotgan so'zingizni kiriting.\nChiqish uchun 'chiqish' tugmasini bosing.",reply_markup=wikipediya_button
    )
    await WikiState.searching.set()

# Wikipedia qidiruv / chiqish
@dp.message_handler(state=WikiState.searching)
async def wiki_search(message: types.Message, state: FSMContext):
    if message.text.lower() == "chiqish":
        current_state = await state.get_state()
        if current_state is not None:
            try:
                await state.finish()
            except KeyError:
                pass
        await message.answer("Asosiy ekranga qaytdingiz.",reply_markup=start_button)
        return

    try:
        javob = wikipedia.summary(message.text)
        await message.answer(javob)
    except wikipedia.exceptions.DisambiguationError as e:
        await message.answer(
            f"Bir nechta natijalar topildi: {e.options[:5]}... Iltimos, aniqroq so'z kiriting."
        )
    except wikipedia.exceptions.PageError:
        await message.answer("Bunday ma'lumot topilmadi.")
    except Exception:
        await message.answer("Xatolik yuz berdi. Iltimos, boshqa so'z kiriting.")
