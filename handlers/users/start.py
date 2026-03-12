
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from utils.db import Database
from data.config import ADMINS
from filters import IsPrivate
from keyboards.default.buttons import *
from loader import dp, user_ids, bot
from keyboards.default.buttons import  start_button
from aiogram.dispatcher import FSMContext
db = Database("main_database.db")



class BroadcastState(StatesGroup):
    waiting_for_content = State()
async def get_all_user_ids():
    return list(user_ids.copy())


@dp.message_handler(IsPrivate(), commands="start")
async def start_handler(message: types.Message):
    text = (
        f"👋 <b>Salom, {message.from_user.first_name}!</b>\n\n"
        f"Sizni <b>Online Kutubxona</b> botida ko'rib turganimizdan mamnunmiz. ✨\n\n"
        f"🔍 <i>Kerakli kitobni qidirish yoki bo'limlarni tanlash uchun quyidagi tugmalardan foydalaning.</i>"
    )
    if message.from_user.id in ADMINS:
        await message.answer(text, parse_mode="HTML", reply_markup=admin_button)
    else:
        await message.answer(text, parse_mode="HTML", reply_markup=start_button)




@dp.message_handler(IsPrivate(), text="Chiqish", state="*")
async def chiqish(message: types.Message, state: FSMContext):
    cur_state = await state.get_state()

    if cur_state is not None:
        try:
            await state.finish()
        except KeyError:
            pass

    keyboard = admin_button if message.from_user.id in ADMINS else start_button
    await message.answer("Asosiy ekranga qaytdingiz.", reply_markup=keyboard)







@dp.message_handler(IsPrivate(), text="🧑‍💻 Dasturchi")
async def bot_start(message: types.Message):
    text="<b>Dasturchi:</b>\nAbdumalikov Otabek\n<b>Username:</b>\n@abdumalikovotabek2006\n<b>E-mail:</b>\nabdumalikovotabek2006@gmail.com\n<b>Telefon raqam:</b>\n+998(91)9055419\n+998(93)9055419"""
    await message.answer_photo(photo="AgACAgIAAxkBAAIhEGknShIKoRcXlRbYH2yo-0kIvOIBAALaC2sbx65ASUpFZlZM4RkNAQADAgADeQADNgQ",caption=text,parse_mode="HTML")
@dp.message_handler(IsPrivate(), text="🤖 Botni guruhga qo'shish")
async def botni(message: types.Message):
    text = """Botni guruhga qo'shish:

Botni guruhga qo'shish uchun quyidagi link ustiga bosing va botni qo'shmoqchi bo'lgan guruhingizni tanlang. Guruhga qo'shganingizdan so'ng bot ishlashi uchun admin qiling.

LINK: https://t.me/E_KitobXazinasi_Bot?startgroup=ru """
    await message.answer(text)


@dp.message_handler(IsPrivate(), text="📚 Grammatika")
async def grammatik(message: types.Message):
    text = "https://telegra.ph/Grammar-Books-11-04"
    await message.answer(text)


@dp.message_handler(IsPrivate(), text="📚 IELTS")
async def ielts(message: types.Message):
    text = "https://telegra.ph/IELTS-Books-11-04"
    await message.answer(text)


@dp.message_handler(IsPrivate(), text="📚 Vocabulary")
async def vocabulary(message: types.Message):
    text = "https://telegra.ph/Vocabulary-Books-11-04"
    await message.answer(text)


@dp.message_handler(IsPrivate(), text="📚 Testlar")
async def testlar(message: types.Message):
    text = "https://telegra.ph/Test-Books-11-04"
    await message.answer(text)


@dp.message_handler(IsPrivate(), text="📚 Fiction Books")
async def fiction(message: types.Message):
    text = "https://telegra.ph/Fiction-Books-12-24"
    await message.answer(text)


@dp.message_handler(IsPrivate(), text='🇬🇧 Ingliz tilidan foydali kanallar')
async def foydali(message: types.Message):
    text = """@English_books_new - Ushbu kanaldan ko'proq ingliz tili kitoblarini yuklab olishingiz mumkin. ✅

@shaxzodtorayev - IELTS 7.0, Reading 8.5 sohibining blogi! 🔥"""
    await message.answer(text)


@dp.message_handler(IsPrivate(), text="📚 O'zbek adabiyoti")
async def ozbek(message: types.Message):
    text = "Sizga qaysi yozuvchining asarlari kerak? Tanlang! 👇"
    await message.answer(text, reply_markup=uzb_lit)


@dp.message_handler(IsPrivate(), text="Go Back")
async def go_back(message: types.Message):
    text = "Asosiy menyu"

    keyboard = admin_button if message.from_user.id in ADMINS else start_button

    await message.answer(text, reply_markup=keyboard)



@dp.message_handler(IsPrivate(), text="📚 Jahon adabiyoti")
async def start(message: types.Message):
    text = "Yozuvchini tanlang"
    await message.answer(text, reply_markup=jahon_adabiyoti)


@dp.message_handler(IsPrivate(), text="📚 Bolalar adabiyoti")
async def bolalar(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=bolalar_adabiyoti)


@dp.message_handler(IsPrivate(), text="📚 Mumtoz adabiyot")
async def mumtoz(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=mumtoz_adabiyot)


@dp.message_handler(IsPrivate(), text="🎧 Audio kitoblar")
async def audio(message: types.Message):
    text = "Sizga o'zbek adabiyotidan audio kitoblar kerakmi yoki jahon adabiyotidanmi? Tanlang! 👇"
    await message.answer(text, reply_markup=audio_kitob)


@dp.message_handler(IsPrivate(), text="🇺🇿 O'zbek adabiyoti")
async def ozbek(message: types.Message):
    text = "Sizga qaysi janrdagi audio kitoblar kerak? Tanlang! 👇"
    await message.answer(text, reply_markup=uzb_audio)


@dp.message_handler(IsPrivate(), text="Romanlar")
async def romanlarr(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=uzb_romanlar)


@dp.message_handler(IsPrivate(), text="Qissalar")
async def romanlarr(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=uzb_qissa_audio)


@dp.message_handler(IsPrivate(), text="🌐 Jahon adabiyoti")
async def jahon(message: types.Message):
    text = "Sizga qaysi janrdagi audio kitoblar kerak? Tanlang! 👇"
    await message.answer(text, reply_markup=jahon_adabiyoti_rus)


@dp.message_handler(IsPrivate(), text="🌐 Romanlar")
async def romanaudio(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=jahon_roman_audio)


@dp.message_handler(IsPrivate(), text="🌐 Qissalar")
async def romanaudio(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=jahon_qissa_audio)


@dp.message_handler(IsPrivate(), text="📚 Maktab darsliklari")
async def romanaudio(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=maktab_darsliklari)


@dp.message_handler(IsPrivate(), text="🇺🇿 O'zbekcha")
async def romanaudio(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=uzb_maktab_darsliklari)


@dp.message_handler(IsPrivate(), text="🔢 Sinflar bo'yicha")
async def sinflar(message: types.Message):
    text = "Sizga qaysi sinf darsliklari kerak? Tanlang! 👇"
    await message.answer(text, reply_markup=uzb_maktab_darsliklari_sinflar_buyicha)


@dp.message_handler(IsPrivate(), text="📔 Fanlar bo'yicha")
async def sinflar(message: types.Message):
    text = "Sizga qaysi sinf darsliklari kerak? Tanlang! 👇"
    await message.answer(text, reply_markup=uzb_maktab_darsliklari_fanlar_buyicha)


@dp.message_handler(IsPrivate(), text="🇷🇺 Ruscha")
async def romanaudio(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=ru_maktab_darsliklari)


@dp.message_handler(IsPrivate(), text="🔢 Sinflar bo'yicha 🇷🇺")
async def sinflar(message: types.Message):
    text = "Sizga qaysi sinf darsliklari kerak? Tanlang! 👇"
    await message.answer(text, reply_markup=ru_maktab_darsliklari_sinflar_buyicha)


@dp.message_handler(IsPrivate(),text="📚 Islomiy kitoblar")
async def sinflar(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=islomiy_kitoblar)


@dp.message_handler(IsPrivate(),text="🔍 Lug'atlar")
async def sinflar(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=lugatlar)


@dp.message_handler(IsPrivate(),text="📝 She'riyat")
async def sinflar(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=sheriyat)


@dp.message_handler(IsPrivate(),text="📥 Kitob o'qish uchun dasturlar")
async def sinflar(message: types.Message):
    text = "Tanlang! 👇"
    await message.answer(text, reply_markup=kitob_uqish_uchun_dasturlar)


@dp.message_handler(IsPrivate(),text="↗️ Botni do'stlarga ulashish")
async def sinflar(message: types.Message):
    text = """Botni do'stlarga ulashish:

Botni ulashish uchun quyidagi link ustiga bosing va ulashmoqchi bo'lgan odamingizni tanlang:

LINK: https://telegram.me/share/url?url=https://telegram.me/E_KitobXazinasi_Bot"""
    await message.answer(text)










@dp.message_handler(IsPrivate(), text=["Bekor qilish", "Done"])
async def cancel_or_done(message: types.Message):

    text = "Bekor qilindi" if message.text == "Bekor qilish" else "Tayyor!"

    keyboard = admin_button if message.from_user.id in ADMINS else start_button

    await message.answer(text, reply_markup=keyboard)



@dp.message_handler(IsPrivate(),text="⭐ Botni baholash")
async def rating(message: types.Message):
    await message.answer('Botga quyidagi tugmalar orqali baho bering 👇🏻',reply_markup=rating_buttons)

@dp.message_handler(
    IsPrivate(),
    text=["⭐️⭐️⭐️⭐️⭐️ | A'lo", "⭐️⭐️⭐️⭐️ | Yaxshi", "⭐️⭐️⭐️ | O'rtacha", "⭐️⭐️ | Qoniqarli", "⭐️ | Qoniqarsiz"]
)
async def rating(message: types.Message):

    if message.from_user.id in ADMINS:
        await message.answer("Tayyor!", reply_markup=admin_button)
    else:
        await message.answer("Tayyor!", reply_markup=start_button)

    user = message.from_user
    stars = message.text.split('|')[0].strip()

    # 🔥 username bor-yo‘qligini tekshiramiz
    if user.username:
        user_link = f"<a href='https://t.me/{user.username}'>{user.full_name}</a>"
    else:
        user_link = f"<a href='tg://user?id={user.id}'>{user.full_name}</a>"

    admin_text = f"""
⭐️ <b>Yangi baho!</b>

👤 Foydalanuvchi: {user_link}
📊 Baho: {stars}
"""

    for admin in ADMINS:
        try:
            await bot.send_message(admin, admin_text, parse_mode="HTML")
        except Exception as e:
            print(f"Admin {admin} ga xabar ketmadi: {e}")


@dp.message_handler(IsPrivate(),text="O'zbek adabiyotiga qaytish")
async def qilish(message: types.Message):
    await message.answer("🔙Orqaga", reply_markup=uzb_audio)


@dp.message_handler(IsPrivate(),text="Jahon adabiyotiga qaytish")
async def qaytish(message: types.Message):
    await message.answer("🔙Orqaga", reply_markup=jahon_adabiyoti_rus)


@dp.message_handler(IsPrivate(),text="Maktab darsliklariga qaytish")
async def qaytish(message: types.Message):
    await message.answer("🔙Orqaga", reply_markup=maktab_darsliklari)


@dp.message_handler(IsPrivate(),text="Orqaga")
async def orqaga(message: types.Message):
    await message.answer("Orqaga", reply_markup=uzb_maktab_darsliklari)


@dp.message_handler(IsPrivate(),text="Rus darsliklariga qaytish")
async def qaytish(message: types.Message):
    await message.answer("Orqaga ", reply_markup=ru_maktab_darsliklari)


@dp.message_handler(IsPrivate(),text="👤 Abdulla Qodiriy")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIHyWkgrFCBSwZcDNbGfOKho7Njsj7fAAKkAAPrH4YNDmnAahWTTTQ2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIHymkgrFAPcQFTNr_QCBy0TuOBn4XrAAJ3AAN-UnFQV5AGMjQszO02BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIHy2kgrFArD8c-lcbdvwv3YXLzeZUNAAJ2AAN-UnFQKG8cDQ4qK5Q2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIHzGkgrFCttOugJuSWxpUo5wypeUljAAJMCQAC70RYUBoeCumXR8iWNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIHzWkgrFAiTgK5tsqBFCRi-KXvfakVAAJ4AAN-UnFQTxIYPkEQGPg2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIHzmkgrFCGK_AuVAkAAcnSjbkuKRDOQwAChwADuFZlBUnsOL6OrwN-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIHz2kgrFApFN98EpeI2nE-DbCDaTsuAAKcCwACmxSQSxqHoOTrVu4sNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Cho'lpon")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIKPWkguYHopFZpyWjxY_TEewMFFCtJAAIJAANfYwQQwibHG0PaX8c2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIKPmkguYE3Iy87RHVsSDsmY7bCEHWWAAKtAAPLzywNpadcqdd1XaE2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIKP2kguYHnAv9KNr1xH3eERu-z-EC3AAKIBgACpctZSkIjml28knx5NgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIKQGkguYFjx-g04ALtyQwiJ7yLdanrAAJOCQAC70RYUEDF5L4lid2YNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Oybek")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAIK7Wkgv_N5QjZ_Xg6FSqZECuXxcpRYAAL9AQACflJxUPDAuRgtvbwAATYE", "type": "document"},
        {"id": "BQACAgQAAxkBAAIK7mkgv_MXLd3IsPs2o2akl1UZCX-UAAL8AQACflJxUNopC3a-8TJRNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIK72kgv_M94lpiaXJTlOU_3DxFvZAVAAIIAgACflJxUIXh7JpyLU82NgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIK8Gkgv_PSkJSdG1O3rvkzNubVzBqFAAJPCQAC70RYUIz5p-bcak2pNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIK8Wkgv_MM1jYbfuG_phep0Rdn60MrAAJRCQAC70RYUBDpCkBPRFBUNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIK8mkgv_Oq2WO8k01vFY8n2-nxgY2CAAI9CAACwv-IUL1qDZUBAwGhNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 G'afur G'ulom")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAIK-WkgwHYHHo9kbA2kY9uV15kZix4jAAJUCQAC70RYUBY3iTm05YerNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIK-mkgwHZ5RsGDJH1YRHDKKZIY9icQAAJVCQAC70RYUOzaY33v3WZWNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIK-2kgwHbUKgcOnMMFPCO0rSaXie-lAAJsAAMQGJBQq-yNmY9vQK82BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIK_GkgwHb82oPZKS_BFBWoaWdwdZiQAAJxAgACroTYSCBzoCqu74IFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIK_WkgwHYXox191Uo_uP6ZDGIfqrfnAAIsAwAC4WEQSupAUSa5cvVFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIK_mkgwHadSBu2pvFaMmnPhDkdjUAEAALiAwACAtaRSrDf4z3XUmVYNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIK_2kgwHYyyvgfhumOebUqhJ02ZT-zAAKJAANf_yFLJx4SlT3kqng2BA", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Abdulla Qahhor")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAILh2kgxYbFgOlRZYceetKNOVqDuvJqAAJwAAN-UnFQOvnxTb6b3wk2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAILiGkgxYa5NgqxcqSRce1is4Gk17gKAAJ0AAN-UnFQ9J2hVim3eq42BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAILiWkgxYYuwAYGTwYSTm_4dUzI7SaMAAJxAAN-UnFQWeudmZw--o82BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAILimkgxYZlCXKvs1s35h0uM3xa_bsgAAJHAQACQHv5SguyQ8D2tPsnNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILi2kgxYa6K3zbD69vbWZu63fV4h2tAALuBQACeuxpSTxMi9VCF2EsNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILjGkgxYYISpl-UKFOGNS_9qQ3qoY_AAK1AwACBv4xSkdbsZQV9YYDNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAILjWkgxYa6HiVTPPJW2A2Ipcole_uWAAJ1AAN-UnFQF9wul0kweGQ2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAILjmkgxYZy1Qr6wbhXf8RvNWbwGiqvAAIZAQACLbY4SYTj3jL3KMeDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILj2kgxYZLtvM0wbHZDBxeD49JnfOYAAJ_CwACmxSQS5-l7hdU4iqhNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILkGkgxYZJ5RQPR6WskOQd16SlQoZPAAKDCwACmxSQS3R4iYwdjEliNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILkWkgxYZ_cUhmH52H8px-61yBfHD2AAKCCwACmxSQS_BH-fKv0xENNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILkmkgxYaSxMIFKZpojkowLgzgXM0VAAKECwACmxSQS5YvATV7BUZFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILk2kgxYZUTqHHj9kD6rjWaoXWtSc8AAKJCwACmxSQS6wfN9aAbiY5NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILlGkgxYY_rs_uFnaI4d9DtBOUJXHWAAKKCwACmxSQS9xizJ40mKwCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILlWkgxYYiJuAVoKZ4PS94zGzrc4qWAAKLCwACmxSQS7vRzwVX_BfrNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILlmkgxYY582qHS3WYRGbAPd3c_v6ZAAKMCwACmxSQS40JlZ4DMGBhNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILl2kgxYafhYuixQ5S0TuyZMQV-lU4AAKNCwACmxSQS9YxR1U1u-IAATYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAILmGkgxYYV_xeqaLZYFtuh0Skip7CSAAKOCwACmxSQS3noP_H6pWOmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILmWkgxYYjvUlSe_vXylAF1brOW6WYAAKPCwACmxSQS_XjjUgLFY5bNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILmmkgxYZDoQ2KcSZJySJPA0tF0fZNAAKTCwACmxSQS_7eJBp53Si9NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILm2kgxYYc6SUZeGtv83W3v3a4VBBJAAKbCwACmxSQSyliP_xLr_HeNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILnGkgxYZbCfkFnd_bYCycMRvM4p_cAAKUCwACmxSQSwNZG9VUAR90NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILnWkgxYZ551vBqmcKhLJb18bcNrkCAAKaCwACmxSQS_68HUJgNoJfNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILnmkgxYYYUHG2Db4hoBX1TN2S8h52AAKYCwACmxSQSz44fhNfG4YXNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILn2kgxYZkGRQSE-I5_vFbhQmngSjyAAKRCwACmxSQS94Ho9BfBsbUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILoGkgxYZk6L531LseEqEYhbzAuhN9AALPCAACQk1wSEHJTQRSfvSPNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAILoWkgxYYAAR6h9aJBVhNS3kK-5U-4KwACVwkAAu9EWFBGXe0U1XGaXjYE", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Said Ahmad")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAILo2kgxdW-iZBpQ1oVD77C77mhcEMDAAILAAPsxYhJtYs6Lmw1DgE2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAILpGkgxdXtT3Vc58dKVLvlKrTgWBIdAAIzAgACflJxUPICai_kPnbSNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAILpWkgxdUiK5qUOzkD3jWArs3mItIIAAI2AgACflJxUKf1OXuroJXvNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAILpmkgxdUNx_A1WUwEFqglOcPBrN7CAAIuAgACflJxUOfvhzZfpRKFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILp2kgxdUUFp1G2tRikK5h9wruXzviAAIBAANhGelJcRjUo_JYO1s2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAILqGkgxdVzBaL8aWj52CveeujE1EMzAAK5AAPLzywN2rn8p84WWM82BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAILqWkgxdVIVuKfmRJ9zhCd7wmu35NSAAIxAgACflJxUMm6LvN4ZIY7NgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAILqmkgxdWQnz_FST9HQgGb3BpISumVAALTAQACflJ5UO2q-QFkF-mTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILq2kgxdWx1Vv-nL5DCmsAAWWGTAlgtgACugUAAv3LGUmGP-vm2I04tjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAILrGkgxdU31X67iOyp6vDyLGG39hltAAKDBQACqW0wSRP7par7HDNLNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAILrWkgxdW2KuAqIHkLNNhvouxVwuQBAAKaAAMQGJBQ-YZWuPlkAQs2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAILrmkgxdXAXB9aTV4tRj2PBSe1CI9gAAIvBwACuyYAAUtDMpkraysrxDYE", "type": "document"},
        {"id": "BQACAgQAAxkBAAILr2kgxdVX-NAe64VYSd3fm2INhbl3AAI1AgACflJxUBn_u4n9JQABRjYE", "type": "document"},
        {"id": "BQACAgQAAxkBAAILsGkgxdVIXO6yh1ucIHCr-Azbf3gSAAI0AgACflJxUM7nfSi0_tSJNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAILsWkgxdW1n3PoV__1x9jxW1a1D7ZdAAIyAgACflJxULbCuKlg_fSqNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAILsmkgxdWCedUvfpLgvVpw2pN84Y0YAAI4AgACflJxUFeILaZiZIR6NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILs2kgxdV-n8DmcPyl1aX7OrQtnGRzAAJcAgACQ1HISstA18Jzc_McNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 O'tkir Hoshimov")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAILxmkgxldkHp6YsqTzEtwsmZJBlqkeAAL5AQACflJxULTxy2rOInOTNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAILx2kgxlfrP4B5l3jcMZ_J0woyCCX_AAL7AQACflJxUGzY4FSMFvIONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILyGkgxlcPzx3GBRsuCAzzQyGayeufAAIXAAP5H1sHlPRAj943RZ82BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAILyWkgxlcXI4SC4HdWMgE43OfVdX--AAIRAgACzNKQS7HE-tP3KpTnNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILymkgxlc1X047WVbecs4O9tUWsbH8AAJKAwACAXbwSR3nAwTLZ9vgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAILzGkgxlc1Y5ImnJbmq9ZQdYFs2sm8AAIDAANfYwQQ32qkJPVQ9542BA", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Pirimqul Qodirov")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAIMMGkgx7QgcbZuj0gJPh84cRTHAAH3mwACCwIAAn5ScVAHRiNCNegVFDYE", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMMWkgx7QIEaYhOHT50fiPCO08yO39AAIKAgACflJxUBKaSVFIDYaTNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMMmkgx7SS3VNGX_ZFnDmRJpPStBbWAAIMAgACflJxUO3wSHoEB41iNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMM2kgx7Q-XU0QRz_QNETY6VNh2wYeAAINAgACflJxUAISpuH0QvjZNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMNGkgx7QbVfmrRr6FIF6N1s6La9QuAAIOAgACflJxUNYBa1I2buBmNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Asqad Muxtor")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIMNmkgx_Ii8X_aPaqEMyWTg0KAGDKsAAKeAANfLahJ3rC0Qz7anFI2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMN2kgx_LWZNAB0QFBmPiiGEL_tkj2AAK1AAN-UnFQIIz5QZ_rXS02BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMOGkgx_I-JdXXaXL-hs-6hi4bp52lAAKxAAN-UnFQieJQvOTaFEA2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMOWkgx_L5XzvzyvU8jN2VgEkcczXoAAKPAgACebUpSh4yhJOzAUpiNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMOmkgx_L5QyxkGVykJg0b6_AMtXogAAJcDAACmxSQS8nlGNHPMJNGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMO2kgx_LIxkGiOoMYXXIVEqC8o-OUAAJdDAACmxSQSxTYo1DKL7FNNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Odil Yoqubov")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgEAAxkBAAIMWGkgyNbPl8KDAQ7DbUXU-rilQE85AAIeAQACEPExRIZjUTKI-_OxNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMWWkgyNbLRYhKS9tF7NLbaAABXXlzpQAC1wEAAn5ScVDPg3Coyv1gFDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMWmkgyNYvf_InlZGwsi8MLdsrYWVJAAJYAgACwUQ4SrgLpoWa7v8YNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMW2kgyNY-DbdGiMzPRjbMFd0Ua_TnAAJZAgACwUQ4Sn45T6xs2FtmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMXGkgyNZ0hC4nqmnqTMBQmo-Ke2DDAAJaAgACwUQ4SvZzVhZdj4MhNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMXWkgyNb684suK4asL7yLk0oD-8IFAALQAQACflJxUI9V2xys9ip4NgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Tog'ay Murod")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIMZmkgyS5dHpO9bjANUzSVgdR5ZT8uAAKeBwACUh4BSrYCkRF4AWGDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMZ2kgyS6uhmQVXa6rFKqup832LedSAAI8BAAC5Z4YSnMM7w_7FGFtNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMaGkgyS46ZR79MsSvgupFJtjAyYuTAAJqAgACflJxULnpiw1rgBAPNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMaWkgyS7JV5N-wA-xwDFXOQPB7H7cAAJWAwACk4vZShsOIougKY1eNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMamkgyS6XRMLjfs_xn6Ja4rytlgLsAAJXAwACk4vZSgiOlvfu220aNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMa2kgyS5X1QRExRE5QwABTXQc13zZBAACWAMAApOL2UrfytYPUVN72zYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMbGkgyS50Md58nhO5PEp6KFDlnnyZAAJcAwACk4vZSjq2uoLSYAABLTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMbWkgyS43KtLWq5qrBFgv5n7rvcC6AAJeAwACk4vZSolxArBPIR15NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMbmkgyS6wnkJXg65wUfKxM9ORSeyEAAJQAwACfjLYSiGSQWqyd1kYNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMb2kgyS7pi_YoAAH41jWJB6zNmZLX3wACWQMAApOL2Upz5bAQbdAg9TYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMcGkgyS4UMEFHNy8Uuz_WGrIZ3Sv0AAJdAwACk4vZSg2oAU4psLm3NgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Tohir Malik")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIMcmkgyfVmvnDKWBcRarrR8vz6PDzRAALXAwACDwoxSM0CxibtI87aNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMc2kgyfXBFfD6ktVx-crrgGeL6YNCAAIjAAPZFSFJZp_LD75toek2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMdGkgyfVh2N0e3j_BxmLxuq6RRpC-AAJzAAPsGRlJKeicGugZpVU2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMdWkgyfWqecm-E1Gj86cguLxvvpXuAAI9AQAC-R9bB3o4MOgQxL6vNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMdmkgyfVId7rFjzLyU2f0_lxG2m_9AAISAAMbcalJUNK5PhdY8PU2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMd2kgyfX0H8t_pIV0Ytp70T4h9anHAALNAgAC1kgoSFfVSgZZZ135NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMeGkgyfV73KmmJmFPUWPHjRfe1I4pAAIkAAPZFSFJk-2HNwK_YVM2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMeWkgyfXQGcfqZQXmD1TDbBhAzEMfAAKyAQACt_MgShcpb73FRTJQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMemkgyfXKVqGdhYZWjpOUf6orR0EuAAKzAQACt_MgSmmLHVGiT6_GNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMe2kgyfX29JJJ0cKvbB987YP49pH3AAK0AQACt_MgSsxkdGJ6e7MFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMfGkgyfWJBFHtWYdGJtwGoVI37MGbAAK1AQACt_MgSkcuq5L0TtjbNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMfWkgyfXSqa7ZVi-Cm-_Gfa7ESHg2AAJ-AQACzq3ISEdfIma5sLasNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 O'lmas Umarbekov")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIMpmkgy1okieVB-X-fshxE-8a4NCEOAAJkAQAC-R9bB0qwVLPkWOSjNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMp2kgy1rlZp33t2p8y4Wk5usMbZAKAAJuBQAC-2aZS1zfnx1bZAEWNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMqGkgy1pbAAEHEX_jufSA0lDZ6ppdXAACOQMAAlIVmEnH9g63QQd_ozYE", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMqWkgy1q_-CxE1FrDpmyFM6AyPlY8AAKUAAMQGJBQC2qPej9T9do2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMqmkgy1rN2d0NRq6t1a6_rTZ-dIK-AALnAQACflJxUBfU16wSxra-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMq2kgy1riMEBqGeszc6RxE3_2b3HmAAIWBgAC50R4StyyTd6xQOfuNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMrGkgy1ox0O8a-3VEiOxG-t7SWEGYAALlAQACflJxUMMa9J-WmrdkNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMrWkgy1qHztg5TGIy4xHclXQzJQABsgAC4wEAAn5ScVBSISyYRAhs5DYE", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMrmkgy1pr_vvRuclkvbNkK9FIPeJ-AALgAQACflJxUIvpGQVimoYlNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMr2kgy1q1FCXd3-A1T-qRZ2Dsqp1ZAALkAQACflJxUMnr63QUWgzqNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIMsGkgy1rmdZwxpquLGk4NgMw-_ws6AALhAQACflJxUN7LcKnLWE3pNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIMsmkgy1oRZtFeffW4rpSX-3vZOYBfAALdAQAC6SagSQX-LmPJqx2hNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Lev Tolstoy")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAINsmki-OXrpV9IJJdTeZKkMJbI5Ze1AAL3AwACT24BSerLjJSme7HvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINs2ki-OU_aVRqd036smjfurryl-3BAALTAAMyqzBJnto2bhkWtBY2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAINtGki-OVY9IBj4_eNp49iokU0HyupAALUAAMyqzBJrk__u_JBQWg2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAINtWki-OWx4qCSCni50UMzBXfVgWt0AAKYAAMttjBJjQgGM8WkO942BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAINtmki-OWZjLM3cHv2eje9WOEfUztBAAKZAAMttjBJ8YqNFBYY9t02BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAINt2ki-OUlZOP5vucdL7LYDJWfK7dGAAKaAAMttjBJGtDJut-9ZnA2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAINuGki-OUWTrgRaAYxfOZD8JNFdWVMAAIUAANfYwQQa67LaQABM-BoNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINuWki-OWmfQ0hyZzB3Fn8P-gzHX5QAAIVAANfYwQQKZTrzhelwbg2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAINumki-OXs_kSTM6sQFhEsxpHiFKSrAAIXAANfYwQQGqmCKM0RXnE2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAINu2ki-OWFl9a3a4W78WZxBlmy4WarAAIWAANfYwQQZGOYvbWHSjc2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAINvGki-OUiYA2UCTLg3mSrh7b0mg6dAALhAgACizAwSgABkRBMApXL6jYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAINvWki-OUa3bmO9k1GOP-xi7yy2uqqAALUAAPLzywNjRWsGpUskTI2BA", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Aleksandr Pushkin")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAINv2ki-SEMDqIhBUgd_gF52b8rAuTtAALDAwACBv4xSvbiuv9aVSqiNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINwGki-SHUQSM2O1u_JZXFiAdcy8BUAALlAANfM6oOA1wroubyMMo2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAINwWki-SHrYpUiJSMMj9jec7ByQDpuAAL2CwACmxSQS6uY5HlvQ_WTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINwmki-SEeISY3L8ghBN7qFD286iQFAAL3CwACmxSQS4kNqIgs9hNdNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINw2ki-SFWsS5_-URliOAU74JMWoplAAL4CwACmxSQS2CeVuZQd5HWNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINxGki-SE3pYsrNARG-8ExrOdJwfMsAAL1CwACmxSQS6aM__uKVUBsNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINxWki-SGFwde564IX-nNA0qebtFLrAAL5CwACmxSQS4RpP-i8gQwRNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAINxmki-SFWqlEoF3SoF09aFY5fwXLAAAJ5AAN0FpBQX_4mJNB3Dz82BA", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Fyodor Dostoyevskiy")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAINyGki-Vi65vc9q8plMA9tUKi2zNjBAAK1CgACG3CZS0LNEoDwV21wNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINyWki-Vh_i4GFcJpQ5IFRm_yn0Yv6AALAAQACcHcYSj-nHN2Xe25BNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINymki-Vj_bRKXDC14uxSULLD_28NsAALBAQACcHcYSkLCHOhIiThGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINy2ki-Vhh8_CLaffg3Waw0HIxf7iMAAIcAQACXzOqDgKZNgJvyRHnNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINzGki-VhAyn3wy-9yYZtbkfktY7xqAAJ6GgACU7H3AwTgVkATk-s4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAINzWki-VhUwmXsEmsn0ZSRAdFUTVs2AAIDAAMIUrBJZJU712k2vC82BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAINzmki-VhuiV4rzA3vhxowaNzL1ZIOAAIdAQACXzOqDn39j-tGQ9T0NgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Mixail Bulgakov")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIN0Gki-X-QSmRI2yzt7jCFVPPYs8MrAAJ7BAACMMdhSMNsWod9_TaQNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Chingiz Aytmatov")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIN0mki-acJh8zT9Kyg8ggqd9z7ll2ZAAI8AwACdqQAAUusisdMKlhSIDYE", "type": "document"},
        {"id": "BQACAgQAAxkBAAIN02ki-afbNV2E6-q3yje-UWzu-vO3AAJiAAN0FohQzOE0lwhmXZk2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN1Gki-acT-jg09vPnTzexPqqMI5aaAAKoAAMYDDFLOAAB3nVimdCkNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN1Wki-afdAAHj2tDdJYsZnmF0rDTiBwACSgIAAhaToUnnm6VVIj8jBTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN1mki-afdZl0iU1DcZq9YQtQYUIQ2AAI3AwACUhWYSYdmHIWVPPgFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN12ki-ad-0cEZS0t10wEXy2kftnomAAKHAQACpJ-oSbXFaOyZopMPNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN2Gki-acb7andXt1RE8lMslduF4LGAAJoAwACdEL5Sf27Rj6hPAbDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN2Wki-af_HW4RjTlAvp0ZaBbbxFsXAALIBQACafdASwMF8AxSe-cDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN2mki-adYt_uGyN4bAl-rkcHd-nD7AAKsBwACwCAYSVr5YI4-E-OtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN22ki-adaAAG4tJsE2-uP09sEVTQMHAACKgYAAmO4GUkp36b5CTTJrDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN3Gki-adtwZcfdy58egW5jztsVluEAAITAAOjlYMLhOwAATVVwUIMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN3Wki-ad3bSGnpx4YKEbJ6r6V85rKAAKHAgACooq4StGNH0lfPB6hNgQ", "type": "document"},
        {"id": "BQACAgEAAxkBAAIN3mki-ac45oqWnZFlebtQBsyJRUD1AAKWAQAC_4yYRsofWRftgUbbNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN32ki-ac_8HINW-sEF3gNU31Lz9QIAAK3BQACN-IBSWPt-nE9zTFmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN4Gki-aectNr9AAGqjdbklNRaKn9rOwAC3QQAApc7oUmZKQb71dRXfzYE", "type": "document"},
        {"id": "BQACAgQAAxkBAAIN4Wki-aerhE4B4tLz_cC0aNXvlvHwAAJhAAN0FohQYDKb2UyDjWY2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN4mki-adx0_zVuVxp3sPkJpv_3U7ZAAKcBwAC0DGQSxBCqNyMPTiVNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIN42ki-acZ535ES2JmYvi6Rc4W3J52AAJkAAN0FohQBcL4gPmGpEo2BA", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Nodar Dumbadze")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIN5Wki-diiS9u6PQNVUimZz1cYvgmAAAJYCgACy7pJSPwaN2bl0LWdNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN5mki-dgC924KyXH0j_M35wIYKyppAAJSAANmvIhKRomWfDJsDws2BA", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Jek London")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIN6Gki-f2J4whHR7QNDaMxIlGPrRrUAAK9AgACwbFRSkOygaD2ZPt-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN6Wki-f3Znvc9Zbi4Qmao2nUDeNt6AALZAAMvbjlJNPerTZjazTQ2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN6mki-f3SiCJ3R30geVgiFSBOpbzLAAIsBgACCaQpSUT7u9fgGKhFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN62ki-f3mMh5d6K5FodG8R3OYAiLPAALpAAPLzywNnNhAi0kcT7Q2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN7Gki-f0iDArWHxqu-RP0A5Fy_nVvAAIRAwAC7w4hSnXJjbgbWUVONgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Gabriel Garsia Markes")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIN7mki-h2_Q9txuBxcsG1zIiRvfHjrAALXAgACUsfISl9rqQGiDk6DNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN72ki-h1S4Q49D6NzjwgV6c89zTFiAAIfAQACXzOqDqcqvkWwbLcONgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIN8Gki-h2sxokiYfxTnyDaM-K2-FQfAAJjCQAC1qZoUObBI3wwgIKCNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Alber Kamyu")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIN8mki-kJSqyY5uNu1hXNRrd4QBN11AALuAgACebUpSqwttyJh22_YNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN82ki-kKAVZgLJu0HIuTCUUo47VaXAALvCwACmxSQS-6RR-fvLWu-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN9Gki-kLR_riBTu-3-T-Kp-XRd5bmAALxCwACmxSQSw875K6xoskMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN9Wki-kLE4uCB05ULCmdU8VHxzVp9AALwCwACmxSQS0dUsklwrno3NgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Kobo Abe")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIN92ki-mYTMVqWoA31KnY-HETJF7B4AAKOAgACGl7oSj2sZKO1gnFBNgQ", "type": "document"},
        {"id": "BQACAgEAAxkBAAIN-Gki-mbPKue1eaA3wH-JO-PGATDWAAJUAAMxPKlEOryd_Tl3emg2BA", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Lao She")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgEAAxkBAAIN-mki-odrnZyoh0xSCBIym3zMzTV9AAJgAQACDg_gRDUci1jeysEyNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])





@dp.message_handler(IsPrivate(),text="👤 Artur Konan Doyl")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIN_Gki-vFC4JBkn-hoPGFb9bDN52uRAALDAwACRl3AS5FzzStXpiN3NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN_Wki-vHe9XwO6Z73CuZMvcaGPn1hAAIRAAPwT0BLfDJaNpR4Jfw2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN_mki-vEqcMt-ScuBa_6mcaD06KcdAAJWDAACmxSQS7TCMcbATKXfNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIN_2ki-vE8JTmYni3Md0qGcWrYrIuPAAIDAAPW5OlKq3tO6oBKfPo2BA", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])


@dp.message_handler(IsPrivate(),text="👤 Agata Kristi")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOAWki-2pLUGpTkarlB4aD-8zlBPyhAAJBAgAC1jthStANZaEDjjWENgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOAmki-2qrXbnmBOqZ1XP-1xw1XrJLAAI9BQAC_AWASJkvimy7yHTKNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOA2ki-2rotFNdO5t5AhvFHK7ojkeIAAL4AgACXUJpSk3ARBe6LjT4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOBGki-2qlaKhhrqCijA9HxZVIZBREAAJzAgACooq4Sl1F3oY6MfM6NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOBWki-2or93BA9G2DEeWHXscrF9V_AALIAwACs-NgStwb8JID0roJNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOBmki-2qJJDqJ23VodZmGyirVP8JaAAJhAwACQYcRSKd9GslsRqxQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOB2ki-2osDnZCLAieEQXJn8huKX9gAAJ3BQAC96PYS_uFeNr84PFWNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOCGki-2qlduVnSaq-sxwWTts0OHVZAALrAgACebUpSgABa0O8XKqrxjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOCWki-2p5-va0zzrTSUSriV5_lZs4AALKAQACh8BpScicC-8odD-QNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Gi De Mopassan")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOC2ki-5nHGEsWdy2eCDZcTLcnFZYHAAJ6AAOrJzFIKHpJ4ppZ5Ug2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIODGki-5nSjzfDTllY5cuKSsMjDEjHAAL-AAOVP7FJ5DRYOaBlRHM2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIODWki-5k7b3eDnj279_o7mEpQ-BHoAAKKAAOo1rFJugWgOmWS1kE2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIODmki-5khBEaCF2DzoLQAAQ4rrPdNQQACOAEAAuMeqEo4nDiNg_ZsWDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOD2ki-5m-Ufu_IMHcFzpUzQOICqEeAALLAwACwmNpSzfwSDr7f4b7NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOEGki-5ltEWiYMjSpCBnmRWQ3WTPKAALvAgACeyjJSkBck5ZOXHTjNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Onor De Balzak")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgEAAxkBAAIOEmki-71p33kZbJLpJxIake8Vy_lNAAJaAAN2sHBHhy6ohhdmB4I2BA", "type": "document"},
        {"id": "BQACAgEAAxkBAAIOE2ki-70am4nPKWLnSZciWqBhdn7IAAJ4AwACc_NoRDmtjB3FN6ciNgQ", "type": "document"},
        {"id": "BQACAgEAAxkBAAIOFGki-72RJRDA6olBj0JDU5RaU-caAALRAQACYMSRRDyA8PDn2HfUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOFWki-70HA4rqdyswxA-TX_ZhVSuXAALGAgACxXNRSAvoUuimZJbmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOFmki-70qFJKk8Wb7EyVonunas02KAAJtAQACXzOqDtKXlYgRgk5zNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Ernest Xeminguey")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOGGki-_SQj7zMF890I4qNd34ddAzsAAJEAgAC8n4xSRmlgvNT6izXNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOGWki-_Ql2Aos6fuT0klD8brLvPBYAAJqBAAC1JEwSJag1FTyIOk7NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOGmki-_QboQY1TjvZ8t0WhpV31QU8AALcAgACMjf4SAvt1jSWDhYLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOG2ki-_RutQ-CayaJqFRI6axeCsjXAAJnAgACTu34SNVW5E47dLZKNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOHGki-_Sddhe7a_fzBRrvITVpQZVLAAJtAgACTu34SCWluOUIOPHpNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOHWki-_QPO2qZc6GllG7HND7mHU3aAAKNAwACJ-EJSrp0Rz-rogUcNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Jeyms Joys")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOH2ki_BrvE2LKnWZcm8VWofy59iXXAAKNAwACGfyhSluEGKKobgaINgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOIGki_BqBZixl6F4iJqZJpRwD2n0jAAIeBAACfX6uBXZ2aCI-Rz9jNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Jonatan Svift")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOImki_DaEG1RRJ1ipwbeagSlpYbB7AAIeAQACUoTgSaQhsPZGjGhrNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Jyul Vern")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOJGki_FaYgevrgr69CmrbgFrvnO31AAKdAwACobsAAUr7aMgKqhE77zYE", "type": "document"},
        {"id": "BQACAgQAAxkBAAIOJWki_FZhnt1dMhE0Sb5Yn0bE88BmAAL3BgACYDw5UIm_UOK8qa0uNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOJmki_FYqGmq31Vwx0NvrJb2V-59MAALlAAP2y7FKNW19e2NfPJw2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOJ2ki_FbFQz7ZU4Cpjv49Dwv9UfOFAAJPAgACQD04SCJvtJnTnijTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOKGki_Fbc9Gluoht-5WOb4NrPNzplAALSCAACQk1wSOLbnmPH5fOaNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Somerset Moem")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOKmki_G8iudMZ1xiY4wWIgCjYz_jwAALOBAACfX6uBeHMi8d4HSNINgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Robindranat Tagor")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOLGki_IIla1dzQ0n1QxXM8-UVbeQFAAJ2BQACh_LxSY2uKLunAAFkSjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOLWki_II32jDZXKiH_T6DvL3_0m3_AAKQBgACVMrhS8BsVNjUp1HjNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📚 Ertaklar")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAIOMWki_LxcNOFc5l5v0vlgGs2L_L0eAAKbCQAC1qZoUJRpUZyFchTnNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIOMmki_LzS3iPrsIxBJ0AICDh1Tf9GAAKdCQAC1qZoUHI_gxPd0UHzNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIOM2ki_LwhMG2-EPxrV5CGbW4sn8q4AAKfCQAC1qZoUAEr_zZ_PcU4NgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIONGki_LxM1Tr-qlp0cCU2qP5_-rdHAAKhCQAC1qZoUBBu0w3JsDTkNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🤓 Qiziqarli kitoblar | Bolalar ensiklopediyasi")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAIONmki_NxKShn1y_yeieuKtONiP_-cAAKjCQAC1qZoULEroOxKynrdNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAION2ki_NxFRg-nnZpL3owlNQJKb5WUAAKlCQAC1qZoUDBgTSHaruadNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIOOGki_NzeeNa3142h5KGRZESHSkINAAKnCQAC1qZoUElvW7nWJ964NgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIOOWki_NxnvgKdqkelfJFqNOOpJ97yAAKoCQAC1qZoUPKuQvcYC9flNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIOOmki_NwWzOOoXk2XBO6vC2flftKUAAKpCQAC1qZoUI73mbomIY_aNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📓 Boburnoma")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOPmki_QzoO2XKIyjG-yiMaoRg8QqaAALsAQACk0vwSDWqNpuiznvfNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOP2ki_QxT4aaMyWW5o27TErmYIBrcAAIKBQACBZZISjZybh9XkBkMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOQGki_Qzbok9EskFI3-In33567lsNAALrAQACVXmRSCPQ_RSaSuSvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOQWki_QzS_xieIy8AAT7kAQad4-g0ugADBgACbFIISFRTKbfc89Y4NgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📓 Shohnoma")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOQ2ki_S8M_ZK_lPRWVVKIXd-N9VsHAAISAwACAt25SsapquDrDRlKNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📓 Zarbulmasal")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAIORWki_UlV5Vd3irsLdyES1ZNZejvFAAJHAAN-UnlQolx02ZJgGWA2BA", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📓 To'rt ulus tarixi")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOR2ki_WmqgDfXPnrVXePzg8SbljloAAKcBAACp61ASSYE_tzeH1lXNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOSGki_WmdnOkgbQTLhCJcr9-hzIsoAAKOAwAC9QYZS0R5WMuHNwuuNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOSWki_WnVdX1JttQmAfHMBN339BzxAAI8AQACfOehSnwFRcMugFc5NgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📓 Devoni lug'otut turk")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOS2ki_YqoPIUXW4hi_VZB3i0_qH2FAAKkAQAC-FDxSbs9ftre3512NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOTGki_YpSFKBrgjoE1BgGU_whlRjxAAI3AQACXzOqDvOrF2xurHVMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOTWki_Yqc6IL4C078vdd2Dnfoi-_FAAI4AQACXzOqDmMB41t99tOHNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📓 Qutadg'u bilig")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIOT2ki_aRTzL1WnqWj_7hRUrH4rXfMAAL1AQACcy4YSpu5ppnXOkMrNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOUGki_aTneimhSM-yZla-00BtFfI1AAJHAwACRu0pSrRbktdWfLBuNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIOUWki_aTbHMvhhZ9LDlDAMkl1FyzgAAL_BAACZPUpSjxSyMnkLNiHNgQ", "type": "document"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='Abdulla Qodiriy - "O\'tkan kunlar"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIIDWkgshBV03EZ8nzfY_n6kSvNv-5eAAKyAwACXx8QSslVbIKMoILBNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIDmkgshCh9ZzyDtzYT1Oj5H-5fvgZAALhAwACXx8YSmfmr14k1hXNNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIID2kgshAmc6icjFW2eq59tx_m-CyDAAKuAwACjRZBSth-nfB5XH0vNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIEGkgshBp8JpbsZIS6S9ARSq0rdvOAAIbAwACjRZJSqAK3BOSaVecNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIEWkgshD3pm_rHoyJtUdxuSoq46xOAAIcAwACjRZJSsrHcz1gm1-ENgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIEmkgshDh37papT0rMy_s2aPWhwa2AAIdAwACjRZJSoM5gYF13QX2NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIE2kgshCCK-FIjhmltiRIaVuS01ugAAIeAwACjRZJSh4caVRYtBGxNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIFGkgshDs4qE23XVjdc3EkcI5Ro3UAAL-AgAC-ghJSrhqWShBWAXqNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIFWkgshDo0btXJ2kUCGigwBXzCAE5AAIfAwACjRZJSlF93e7SeUxZNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIAmkgr-DdPy36_-vYihisXcFFj9bMAAJCAwACrohJSunwbG2vR7PZNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIIWkgshBn-VxXC_lKJx73E9_cK-0TAAIgAwACjRZJSjwlmPcuMn9jNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIImkgshCAlIguIJRkG1qnm3hwRJBnAAIfAwACqSVYSgUhGKTPmiefNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIII2kgshBCLyriMz4nQ6ewjarQAhR-AAIgAwACqSVYSt0NQBHV0OsaNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIJGkgshCev5hbcnSkbWAFT4xFWIDRAAIWAwACDkpYSspXO-gKBEizNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIJWkgshClU7iNHvLofnSgJgZBpJBeAAIjAwACqSVYSuKHbZkI6TD7NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIJmkgshAvAUXajWZOMM2u1A6E7CCuAAIYAwACDkpYSiEUywWUext3NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIJ2kgshDBM-zJyOsaAeMYtUi4B2WxAAIlAwACqSVYSmXv7cwGNNKmNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIKGkgshCWrjbLmwxAzJefdDs96Gb0AAIaAwACDkpYStNBwrC1O_fBNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIKWkgshB4dD9JvMPuyB2iHPP61TkPAAIbAwACDkpYSjoIniWPvv9KNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIKmkgshCecebAFrAE5jZ8Iw5nQh8PAAIeAwACDkpYSijDwZ-CircLNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIK2kgshCKSldvdG3ax88YPCWRaBheAAKKBAACwCFhSs5DDjNhnk4mNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIILGkgshCaV2yNdlR9-cPMmIzBQL7KAAKLBAACwCFhSl-BTFyM7uvnNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIILWkgshCdlqQRYgF2kHLMO0nYOdCGAAKMBAACwCFhSnN_3SgxioC9NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIILmkgshDXIy-Sq4ytoqVxrCd7gmInAAKNBAACwCFhSqPT9aqhkV-LNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIL2kgshBgz_muc8MiHr_DS6WKEXarAAKSAwACDkpYSlioBFXr0OpVNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIMGkgshCjVoZT4otR-qt6tUH82qr1AAKTAwACDkpYSiyEfqbJIduINgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIMWkgshBtYBzpRPy7flqznB4URtDbAAKUAwACDkpYSiMzeUcD9klINgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIMmkgshD7Q-RIC1ayPYqK6jf1yV4DAAKOBAACwCFhSj1--S89jIQhNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIIM2kgshDLez5kOpcjFsI0qvXUJPfdAAKWAwACDkpYSnFu2rrJuOuRNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIINGkgshDcPbUUNrq1FNJqKcUWJ7NLAAKXAwACDkpYSvLGau9G549cNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIINWkgshDrto5vXVKjREHiblG0yY3sAAKYAwACDkpYSuYYe9bLMVZMNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIINmkgshACAAHiEcmpWFi_jVyB-hclBAACmQMAAg5KWEqslVW59fS5EzYE", "type": "audio"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='Abdulla Qodiriy - "Mehrobdan chayon"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIOdGki_itAux3qISsp_H5A8UV7V1ABAAIkBAAC5Hp4SHHFIs2B8Aq3NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOdWki_isLuBjNWfRsqZylBVMIHAWqAAIlBAAC5Hp4SL74lPlisfxzNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOdmki_iv-SarsE5WZrDw96s6iGWpbAAImBAAC5Hp4SMpMtwqgHCiONgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOd2ki_ish07fKq5YLLTDs9_QsOl9eAAIoBAAC5Hp4SHXvT4nODh5YNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOeGki_isZ4pj7PFZ9CFZU4UZ5SD8yAAIwBQAC0F55SO3jI0y7VYWVNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOeWki_ito4e9TfucUXI32DPZ6skzYAAIrBAAC5Hp4SE29654e0BTINgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOemki_it_Wr0k1zEV8DZXIbHPqTU-AAIxBQAC0F55SETM2FmmSGzsNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOe2ki_itIoNCOVXUdqe5b5ktKnyeyAAIsBAAC5Hp4SDHxhUTBfnm0NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOfGki_iu4Xedhy61rnErVThdVMrAqAAItBAAC5Hp4SI5EQTQIbkUhNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOfWki_ivTaI1ObCijmnittxUcyD1cAAIuBAAC5Hp4SCgbrAdiL8UqNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOfmki_isPb3JLxPSng6hdMoT0IIYXAAIyBQAC0F55SAjPMAMJWmT4NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOf2ki_ivyGQ1Y0dm1FvktXf9wGAABXQAC8AUAAhGJeEiZvTbniCXHezYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOgGki_ispjGxXsVWsf6s1LICEm3HRAALxBQACEYl4SCCEVUy9Jm9mNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOgWki_itqwMc1DTmyNg43PW6nV5GxAAI0BQAC0F55SMb2obY-azofNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOgmki_iuJcg6zjuQXrj1u56AhiUqTAAIvBAAC5Hp4SE00GPoez0EhNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOg2ki_iseDTytJnk2WZvvGk_OH5RhAAL0BQACEYl4SDAC2imge7ZqNgQ", "type": "audio"}
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='Oybek - "Navoiy"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIOhWki_sBKuwj1iIv1sUqGpmvIKzo5AAI_BAAChSrwSmA21rATfhumNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOhmki_sAklA64GOOA1ZfcxqXO_y3SAALLAgACmZnwSnfiXnHCv5xGNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOh2ki_sBgAj-jV_LZj-jAHstkdVD7AAJABAAChSrwSvpWoVoHWkmfNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOiGki_sDM16EFUYYR8elIgbTNuHKUAAJDBAAChSrwSizC7uzBbdfANgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOiWki_sAdeERCBKZRPqA1WzXDR0aKAAJEBAAChSrwSi5M-OVFuB53NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOimki_sAoeI_ZyfPkFf7Hk35adLsYAALeAQACPuH5SptsWJkQ0nbmNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOi2ki_sD20midPoIvpv9KIF8yY_mfAAJFBAAChSrwSi2QnAQzMStwNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOjGki_sADnG8x901A3OdhDCCAQAvmAALfAQACPuH5SggWpcuM3KzGNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOjWki_sDBmvOwJmJAgPC4JfIfEOmJAALSAgACmZnwSrWqw2jh7bbXNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOjmki_sAEQ3sVsq8EjQ1ODDgKKOW4AAJPBAAChSrwSqNuqAXCz4EFNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOj2ki_sC44ngrXuYIkCG4jwUKiDayAAL7AQACPuH5SkoJcB_7VoJkNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOkGki_sAZ1PHqJyfnBXPrGe8gTLCkAAJRBAAChSrwSjMHiWjF27gxNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOkWki_sBnqXYolrToqB52mUG_WDOOAAJSBAAChSrwSqfWSzW5qFjCNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOkmki_sCuK3PGKrQhaPEJVRyrakVZAAL8AQACPuH5SllQ3TXGiS_dNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOk2ki_sBqKCR7bk8w6aj8OvHYConbAAJTBAAChSrwSvjzpX_UCzWNNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOlGki_sCfi8wTYmfVJdp21kaeY7ZiAAJUBAAChSrwSkiqcBer1bqWNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOlWki_sBnEmWrpfGwpFHQtttPDat9AAMCAAI-4flK-lNCgXsgfF82BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOlmki_sCnk5zsz42oBVbddbmqlqE2AAJVBAAChSrwSk4jiCGlr4ZTNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOl2ki_sB3EH6TW1bBp0i5VeB-GQd4AAIBAgACPuH5SmDc1srbdA60NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOmGki_sCVKHuFgkIH57LVXLcVOV3JAAJWBAAChSrwSp93NIMUVJdkNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOmWki_sCOYZoa0Uo99Q7nXp0QJd2YAAJXBAAChSrwSm3zzYHryAXCNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOmmki_sDN6K1o9oa0UHi9o2DP3VKOAAJlBAAChSrwSuNSSrFEY8dzNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOm2ki_sBX0QNjVQUCkZ_6cYoWMQQYAAJmBAAChSrwSlDdAZhbA3omNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOnGki_sD5pD_kkTXYrPfKl9wMm8iOAAIQAgACPuH5Sns7gOFSXVOWNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOnWki_sB7lxGvRlWB8Ro-0iVFAAG3VwACEQIAAj7h-UodZLO5CD9A8DYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOnmki_sANnsYawi29eengFRdbb89yAAL8AgACmZnwSmjWhEaPIBscNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOn2ki_sDh83BUvwuXZe9PcYYdYdQRAAJpBAAChSrwSlmPIp2GxrSUNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOoGki_sBbH5u-aX3vJ2628pQB0IbqAAJmBAAChSr4SjtfUvJ8FSJoNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOoWki_sDkjgRt_z2PuZSUNA9g3uUkAAJnBAAChSr4SvBg08G2v0-wNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOomki_sAL6gQRpJ-v2CPFtsGpGFrLAAJoBAAChSr4StwMFa0HTgx6NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOo2ki_sBpII_c1WX7zyxfoxTsswlWAAJqBAAChSr4SgU2fdrJL--CNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOpGki_sBFw9cSkXIZt7oc-SniuoaLAAJrBAAChSr4SqYJr-8K7NwPNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOpWki_sD01RjS2bzFBLhu0b5g2a9cAAIcAgACPuH5SpHOXM9U31_7NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOpmki_sBf0DN8yxybMqUE7d8T7YHfAAJsBAAChSr4So8Dqc4cJFMtNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOp2ki_sDx5d4m_6_7rYKB2AnqTB7GAAJtBAAChSr4Svzaeu1dvNLjNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOqGki_sDOb9mtMPWOskgN2sUHhr5vAAI6AgACmZn4Sv69A_ZXYKE-NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOqWki_sDwZWALGBY4NUcPoe7ZGbGsAAIVAgACT7z4SobuvsxGX-h0NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOqmki_sAjk5xAp1HEHFk0Jplgnd6XAAJuBAAChSr4SumHP9kkxB0hNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOq2ki_sCpwlfbTTE5F7xPSj1xz8XVAAJvBAAChSr4SrOU9pfZyt9vNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOrGki_sBLfnioyFLPKryfxBm5rfvSAAJRAgACmZn4SnQXOLIGL4RGNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOrWki_sAsUUfA6jgfvyB0bzYg_wcWAAJ7BAAChSr4Sh_82ceM0NICNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOrmki_sA_2BNDAAHjHuBuKe4WuggTqQACfAQAAoUq-Eru1jeFrc7EyTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOr2ki_sA7rfH2-YEIPPdXZ_GfCXlDAAIjAgACT7z4SqQ9qDHvNqhmNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOsGki_sB28vppfCci8Q56s00bGksVAAKABAAChSr4SmvqdONRYXLnNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOsWki_sDpxIqgIe86ZgOimOvHJ8n7AAJXAgACmZn4SqKrc1I1gbwiNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIOsmki_sCRAQlghKPinuMib2Qub37LAAKBBAAChSr4SjCMLoEsfqwjNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])

@dp.message_handler(IsPrivate(),text='Pirimqul Qodirov - "Yulduzli tunlar"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIPO2ki_8bceUT7Zy2kgfatSdj057B_AAIQAgAC_2BJSxsXkxdlnBvONgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPPGki_8aNAoNsoA1usxJPyXNX4dNjAAKJAgACoQVAS1oy7UU17jtqNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPPWki_8b-fUbhWJuZBUyOXTgdgB47AAIdAgACoQVIS2maIcYtElqJNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPPmki_8ap8Jil0oab_-bNf_7IGb1kAAJeAgACoQVISxZLqP9e57CxNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPP2ki_8YIPDiuK4nlJ4gzB5TAiNTXAAJfAgACoQVISyLOVjX35a6JNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPQGki_8ZQPH3HgtLSBfzTvG7xQ2AnAAJgAgACoQVIS2ZLMilzrxBeNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPQWki_8bEmBTLUdZ7tHgTiHfiSI7hAAJhAgACoQVIS48xt0aLiVL3NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPQmki_8b0ntFnNwuB0CK2U9wHIzP4AAJlAgACoQVIS5vqT4OkUtXJNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPQ2ki_8aEPEFZNu0tLc1vIQuQkolgAAJmAgACoQVIS3SpKKceE2HDNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPRGki_8bZCwy0gfVflcJQtjm6c0HUAAIkAwAC9SRIS42rClYi4K18NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPRWki_8Yc76eB4Y_xTXz_ZNBensM5AAJXAgAC_2BJS8cQNwk4W105NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPRmki_8aM2ouZsIDQibSluvzG8iCSAAJYAgAC_2BJS4VYIMnRAUmqNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPR2ki_8ayBOokt_ML2pNCjVoalZuJAAJZAgAC_2BJS6p29JYuTrIINgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPSGki_8a_QGT8xZPwdRPiNaD8jQoYAAJaAgAC_2BJS2iNjJyFDewCNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPSWki_8ai21_S-gdFx8O6pgRIuQ-qAAIlAwAC9SRISwq9s9KFo5YINgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPSmki_8YWMUvXkXfnDR8jGOp0QGbJAAJ-AwAC9SRIS34NdnRbHJIKNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPS2ki_8Zsf5A3uz85LvIsUkctLSfjAAKAAwAC9SRIS8Im8ITsSlvhNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPTGki_8Z1vY4Pjw8DLRvR5A3p31jWAAKuAwAC_2BRS0snx8kTKh0AATYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPTWki_8Y0eDNxo9dPHelX4USH-IMqAAKvAwAC_2BRSyluY_qLNlStNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPTmki_8ZLeUWurWvdg482-ArOuhXfAAKBAwAC9SRIS-8tmP9wUyDaNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPT2ki_8YrS10aBUybAAGZVcRkWfrx7QACggMAAvUkSEs-U-nub0nRjTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPUGki_8bqjZGkKa9uwgU1ZGWKEqr7AAJZAwAC9SRQS6IFi1NLrfjhNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPUWki_8aoEZCnaygq-Gt4IM1eDL_7AAKiAgAC_ONIS4INza-muORdNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPUmki_8Zj6j0i75Xd5ymm6dijOZk8AAKlAgAC_ONIS2CxrjrMUlHhNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPU2ki_8aNzQSehGLF7tIOv3yIEkxsAAKnAgAC_ONIS2Xk4cY9pwYJNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPVGki_8aGYBdbx8wKijfXT79TINNeAAKoAgAC_ONIS3GF_Khtb7ZgNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPVWki_8ZW9vJOIHje39oaoNIvLXfNAAJxAwAC9SRQSw1sVQABl62jeTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPVmki_8Y_epGePffM50aQJCvlZM99AAKpAgAC_ONIS0uJA46FMISXNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPV2ki_8YTo7cTn4BgDCZZQNh9Z0SPAAJyAwAC9SRQS57WteL833OQNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPWGki_8bf7yFUVztii3lJHjXaGXgmAAJzAwAC9SRQS56_cDIWRJvMNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPWWki_8Z5ygTt639SPOtcSUsfLzWeAAJ0AwAC9SRQS_Qz9Im55YIjNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPWmki_8azX2DC4yfYUqiDBhOzWzgDAAJ1AwAC9SRQS6s-t695iRIrNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPW2ki_8aqzv6VmialJSKuJLfTDqgeAAJ2AwAC9SRQS2WnWgHCCASuNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPXGki_8YYRCFPcIED8k4zL7SaTh7BAAJ3AwAC9SRQS_ZquCczITMZNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPXWki_8Z99IFnT2SoUAtbGrUXkhlvAAJ4AwAC9SRQS1XAbf3kK_w4NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPXmki_8bTPmo4OW-UTFjbK_1otFHIAAJ5AwAC9SRQS-g8iSZw8wy6NgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='Said Ahmad - "Ufq"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIPYGkjAAEJCZcDICsuaKQkIT-s3D0OegACHAQAAgF-oUsrXTkrYxQ1GzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPYWkjAAEJmYoajMybYgbRv3_f3A2JIQACJQMAAnktmUuVdLeJLlJy7jYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPYmkjAAEJAhzYYauQo-Lz5eGRgqxQDAACIgQAAgF-oUsNHiG3eridoTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPY2kjAAEJm2fOc6QmOJ1NTE0iuz1bNQACIwQAAgF-oUv-9AtX5-Ki7jYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPZGkjAAEJ9nrVdP9Ve0n_DqNDgTeU1QACJAQAAgF-oUsOHuRbKjKHcDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPZWkjAAEJ7UJMOuwKl3Hmee8JcmZTYAACJwMAAnktmUuNhJlym-EPUDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPZmkjAAEJ6VfKVIupaM_qUIkcpxTKtQACJQQAAgF-oUsQBlQU_YsZ9TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPZ2kjAAEJ9J2ZSLeqSc2k7gXC4voGowACKQMAAnktmUtNW2B3GSUtJTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPaGkjAAEJZ7MyMERO0styvyzj6GHicgACMgMAAnktmUsd3GsSq2_fXDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPaWkjAAEJc4GQDk2cmIiLL6qT_BlCQQACKgQAAgF-oUtI8nR37mBp6TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPamkjAAEJxgekX5_8MQQJ1HYGAd4vfgACKwQAAgF-oUuGpcPiI5qlBTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPa2kjAAEJy9d4b7mFMGBWZIZNX4KiFAACLAQAAgF-oUtIJ8LF8JvjdzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPbGkjAAEJ3IbJxy_x5AQGuJUPn1q7NAACtQMAArmgqUvZuq7R2Ypm8DYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPbWkjAAEJdmMMhPGnHkcR5j-DfFWG2QACkgMAAgF-qUuRzhZXwju-nDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPbmkjAAEJH4uLoaHsZ-BWJi2QVAu4CQACuAMAArmgqUvxyCUMJ-7KgzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPb2kjAAEJhLSYS57R9zcdQomFkMk9VgACZgMAAixBqUtcVAiBuBzpbzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPcGkjAAEJ3nyV6JcmpDVKujSdl0hxNQAClAMAAgF-qUvPgetE3N3J8TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPcWkjAAEJXKynefxgRElhgTLG68JmPgACagMAAixBqUv2QE1MobxhQjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPcmkjAAEJeu1fgZZQ3uxxX-QlWbp2tQACbQMAAixBqUs6OL7PGMbpPzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPc2kjAAEJLuLaHOw710VtUuaIG8DimQACdQMAAixBqUuBB5jH9s5wLTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPdGkjAAEJ5AHoXsDFTwUw30UfEEWe5gACeAMAAixBqUtevc30ddNLjzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPdWkjAAEJzpkXG625J9-rIaGmmfsQiwACpAMAAgF-qUvVKKIJd1tqbTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPdmkjAAEJBCpnU1azG5c2hpsjPRQnMQAChAMAAixBqUvFfded2EDMSjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPd2kjAAEJPflm3zAbbBRwNQhelFtqswAChwMAAixBqUsPWkcbv-gyOjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPeGkjAAEJhVxJL2lxYykeLgABenMynGYAAmYEAALhprhLHfmttTcc4n42BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPeWkjAAEJccR1Bggmqea_sQHpM5iVeAACuwMAAgw4uUvC9uqWnbCx3zYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPemkjAAEJwVj8_2WrBSn0gNRMhBW9TwACHQQAAoAMuUuQWJRrjb3HjjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPe2kjAAEJKxe1Q9UkD0kXCMbeR8ALDgACaAQAAuGmuEtr3hMMDAmt2TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPfGkjAAEJPPtce55I1wlyZv2Db0KXxQACaQQAAuGmuEupQYJaqCpD6zYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPfWkjAAEJJIzvy3zUUgABh13LRNnRw_0AAh4EAAKADLlL12piylhmHbw2BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPf2kjAAEoZBrQY6sCj0CbBpBFDhJ47wACvgMAAgw4uUt1fLeFZ6WWXzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPgGkjAAEolNyhjgQxn00Jl-O3D0vmfQACIQQAAoAMuUuzh5XIxLWwyjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPgWkjAAEopMsB4ufmuPs8QzJyw-TY9QACIgQAAoAMuUuRxgIzLsMGIjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPgmkjAAEo7Zt38_WEw4wQRZcCUc5ssAACawQAAuGmuEuUu2s81Rf9EzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPg2kjAAEo6n_2gwSKhWeML4c7UsGtkAACbAQAAuGmuEtfw49a5g8f_TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPhGkjAAEoI0mm6I4owGiJEYE__5G-8gACJAQAAoAMuUtVezE039Y6FjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPhWkjAAEotu1mSOsMTPHBB2A7rc_MFwAC3wMAAgmAyEs18BtBDUXykDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPhmkjAAEo5g7evSenolgd5spfaomOnQACswMAAuGmwEt5FC-6e53RhDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPh2kjAAEo1ygb5laZWvJYCFiC9isQJAACYgUAAtI5wEtqkrrmCfAN-TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPiGkjAAEoAi6oTp-FrHy60o9yYVVxmgACYwUAAtI5wEvWlf8wxlbxwTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPiWkjAAEoe2IwrUHfULsvzhRsEk9KhQACuAMAAuGmwEuGLMQYemNRQTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPimkjAAEoUJRp07Je9KuZ9LRQVOAYMQACugMAAuGmwEuEjRDMzKj3PzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPi2kjAAEo4q6ztFAskyAXaVuv23nt_gACuwMAAuGmwEtlwjHJxEvmQjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPjGkjAAEorImiGr7EeXVDDIjsj0a8_gACvAMAAuGmwEtwVPlPZhwWRzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPjWkjAAEovm5VzFtTGQFJzqdY1VTwjgACvQMAAuGmwEvj2s7CxQzHNDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPjmkjAAEoaLCYE0en-MMUaDvbK5zaRgACZQUAAtI5wEu7nwZkrm8NTjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPj2kjAAEo_lQ2zN1zi74S6YM86Kxk2QAC4gMAAgmAyEtiOClZE6GF_DYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPkGkjAAEov3pXbMJV8JiQa9DrU4BHQgAC4QMAAgmAyEugaj9N1WmgqjYE", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='Tohir Malik - "Shaytanat"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIPkmkjAAFVfH5sP6uNFi1hOOYt3EgkSwACmgUAAsPmqUuATEnJrP2D7zYE", "type": "document"},
        {"id": "CQACAgIAAxkBAAIPk2kjAAFVO0s8f6HEOfbS7bn4Fr3ZiAAC9QYAAnO2yEsJinntQGPyLjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPlGkjAAFVH67MZIL34TrlPt6djVBPkgACKQYAAmQeyUsc8Lsr5dTOaDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPlWkjAAFVTWzHf_UYfba3qge8IAVx8QAC9gYAAnO2yEt9vCy7u6nmkzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPlmkjAAFV48qSRqsjWMznxTTHf_NmgwAC9wYAAnO2yEtyVpCfBz8bJTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPl2kjAAFVH6dxYP4iv58nF85ZYfZyrwACKwYAAmQeyUsqXW-aGWJTxzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPmGkjAAFVrdvORwhCndYoK0aJGcLcWAAC-AYAAnO2yEtbMY7gtIzIPDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPmWkjAAFVqBYe2473DSpwqOTjsUZJCgAC-QYAAnO2yEsOWKcOS3P9GDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPmmkjAAFVkTw3f_b2Hq0jWofbJT4FeAAC-gYAAnO2yEva97kH9plZ5DYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPm2kjAAFV78FeIG6Cg7dpcj8AAWslmBcAAiwGAAJkHslLMOBtPtvmWWM2BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPnGkjAAFVi3KwYdY2GW9vg7l7ifPRNQACLgYAAmQeyUu9Hj7nX7VqKjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPnWkjAAFVGlH5AzKMY1JmSXZ_KhSF0AACMAYAAmQeyUvtZP428q-9UjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPnmkjAAFVbqvOW7geUBn536ITFMIjigACMgYAAmQeyUs1Aw3XukRCgDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPn2kjAAFV3OWO3sEvLqwW3UX0lF5gKQACNAYAAmQeyUtbVEFf98jHfjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPoGkjAAFVcBDtODZn3p7FxzkNSv4RXAACNgYAAmQeyUtdnxifTsJAaDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPoWkjAAFVWN5181ElxiqR5Rho9n7-mQAC_gYAAnO2yEtUQ6_nBffuezYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPomkjAAFV9TlIw9ED_eTGwtEliSW2_wACOAYAAmQeyUu1u22HiRfMSTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPo2kjAAFVcmFlAAEcgz4W4fQ23ZnHXoMAAjkGAAJkHslLDPrQD4tOxTc2BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPpGkjAAFVZWtiraOyXk11h1K0lTeAyQACOgYAAmQeyUsIGUOoyG_UtzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPpWkjAAFVUPJ-INorMJAE5cOttmvqmwACOwYAAmQeyUtpEuXf1062EDYE", "type": "audio"},
        {"id": "BQACAgIAAxkBAAIPp2kjAAGDKhd0-S_6p_osBUQf739jGQACnAYAAsBosEu6-SsRd68uMzYE", "type": "document"},
        {"id": "CQACAgIAAxkBAAIPqGkjAAGD1imw5MYJkun1hl_PqwbL3wACqQYAAmQeyUvStkxt5ZsCszYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPqWkjAAGD5OxD9CUvhS-2SVe9PObbEgACqgYAAmQeyUsXA0JscI1gaTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPqmkjAAGDlhyvwHdE_bQWVIp-qNfdqgACqQcAAnO2yEtssPKV0jTooDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPq2kjAAGD8ibAHsD2Q2giFWVsWp4zVwACrAYAAmQeyUvSFHyK_5s_CTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPrGkjAAGDRA90X2Is8Zuoy62VDVuUdQACrQYAAmQeyUse_ecZfeBCTjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPrWkjAAGDmHFOCvh2nj8T9Z9u24JrdgACqgcAAnO2yEt_F3sDt6YaOzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPrmkjAAGD82VRAnx2FeZw-hnDIwABoLsAAq4GAAJkHslLT96KxbNJeJE2BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPr2kjAAGDYzSRS7-ALintEk_Lj5D5qwACqwcAAnO2yEsfKfk7tZq4qzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPsGkjAAGDh9nn778IILS3ja715yLZvgACrAcAAnO2yEvclhv2oRQnqzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPsWkjAAGDa6dbtGwV1JVYtpjooMTSlgACrQcAAnO2yEuIY3w500YU0TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPsmkjAAGDIDAFkg-vxbrxfDmUmSRzOQACrgcAAnO2yEvlu5vs9L9xNTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPs2kjAAGDyH0j_nDmF6i9W6uZmdG8zgACMQUAAuGhyEtpmqCc9xZ3cTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPtGkjAAGD8KTt0rxKwnp39sigx-KPGwACtwcAAnO2yEvShDJmg1dgrjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPtWkjAAGDNVA5yqcpxxwucvVpz0DTMwACrwYAAmQeyUuQ5zPxaEHtszYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPtmkjAAGDEGCmB73OK5KA8j9EiHk_nAACvAcAAnO2yEtUqyY8jIYyeDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPt2kjAAGDgaZqxTGRZtRF_qsmweshywACsAYAAmQeyUvmgn4CqS-oaDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPuGkjAAGDv-n3lGd9SsNxTrCC4r1CKQACsQYAAmQeyUuXBR56hbXtljYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPuWkjAAGDll3kczHNhT_So7wSYUPM6wACsgYAAmQeyUtGH0movInijjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPumkjAAGDM4fMbI5K0RKciDSEz0RmqAACwQcAAnO2yEvMA_37ZicIkzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPvGkjAAGp5diST_5b3cnDJ4u9GdIh0QACcgUAAmQe0Ust93rOEYA3QDYE", "type": "audio"},
        {"id": "BQACAgIAAxkBAAIPvWkjAAGpLyZ2z_Zkmpj2jwttuNAtgwACVgYAAsPmsUux3nVOVRCfNjYE", "type": "document"},
        {"id": "CQACAgIAAxkBAAIPvmkjAAGp_fCQUL2_5--r5CBe-S5_yAAC2AUAAhpO0EsqxyCAAwM28TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPv2kjAAGpVo5ATxcCubI20yjLuBIXkgAC2gUAAhpO0EuALEdz-UOcGTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPwGkjAAGpkfgBHBpgH2yG_NkB5lUN-gAC3QUAAhpO0Es8OwEe6QEWSjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPwWkjAAGpstrEtOOVaGbguhvwp9mKVwAC3gUAAhpO0Es2GTGGr0DCATYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPwmkjAAGpW7n7Xgp1eLJp5qcw5pu-NwAC3wUAAhpO0EvgIHQ-bOY1xTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPw2kjAAGpNSTAsrNd67EK12tCSo0FBAAC4QUAAhpO0EuOSjZkakeaDTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPxGkjAAGp8MF04hoErkM5xFHznfB_HwAChwUAAmqo2Es810kT06hs1zYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPxWkjAAGpTmkvThm_kfLjcUPLmq5WkgAC4wUAAhpO0EuVju6LK8-RyjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPxmkjAAGpI35IvqW7EcHshu1jPFidBwACiAUAAmqo2EvFLH7y4L_itjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPx2kjAAGpy_1NcQqGhThGhtetswiTsAAC0AcAAhrg2EsCkElCvMsaSjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPyGkjAAGpWYsAAe7reD_GFMqXGl-OAAGiAALlBQACGk7QS-LnE0-NPEUzNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPyWkjAAGp8p7gDvuCbvkYGyktbGXErQAC0gcAAhrg2EvYf6P7XwM9GTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPymkjAAGpQOFsGFvIAldytvs97fp-UgAC5gUAAhpO0Ev2CQVQIG6CCzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPy2kjAAGpgA3VTSx0RTAHaZ6D76QGBgAC0wcAAhrg2Eua7vtliEhbPjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPzGkjAAGpBEImr0sqLYpIi9nMjyLXyAAC5wUAAhpO0Etf1602fj8qcDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPzWkjAAGpyQqYZEJrWd3Ad6Ep3jmdrwACigUAAmqo2Es59--yrUwxjTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIPzmkjAAGpWF112t0b3v8gaqisCmtmlgAC6AUAAhpO0EuRGy9iTa8rTDYE", "type": "audio"},
        {"id": "BQACAgIAAxkBAAIPz2kjAAGp0VrH8J029E80ebNTFqrK1QACwAYAAsBosEsfKjcOCmdudDYE", "type": "document"},
        {"id": "CQACAgIAAxkBAAIP0WkjAAHRDpJx5vFKN0U-1SK3Ilee-AACBQcAAp0G6Eu9ti9_winxbDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP0mkjAAHRK8O6PMrH6Fxqj0lDbskJkAACBgcAAp0G6EtPrJrJyDOTcDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP02kjAAHRx3MkDRFSpEH6vZ2XIB99YAACBwcAAp0G6EtHFJMcp-twazYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP1GkjAAHRlMR9EEKfq9lJDJdY3XYbPAACCgcAAp0G6Eu9h9SLpzKLETYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP1WkjAAHR-p2xgqxKpRjHEf2UjNT5ogACCwcAAp0G6EuGj8cHAxzXSTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP1mkjAAHRIJQF-ve2SVut6Us05LUocQACDAcAAp0G6EtFWKfKWmLk9TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP12kjAAHRpZSXED3SggniI5GqBS6zxAACDQcAAp0G6EuEhChwgr3cazYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP2GkjAAHR5AthZUGUL1DP7tsMTOevAAMOBwACnQboS_KchQQ0HzbaNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP2WkjAAHRrmwrRAZ0T2rFi9AakXRDWwACDwcAAp0G6EtN4hyIrDCCtTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP2mkjAAHR135cf_6bwXqZa5MB2A0dMAACEAcAAp0G6EuD5EXq98NAEDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP22kjAAHR0_tn_-uy4F6Ny3oLPKxV1gACEQcAAp0G6EusVNL4oLxPTDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP3GkjAAHRgkPr3CB_dqbdIcY91MH8OwAC4gUAAhpO0Ev4JPmj1bQkpzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP3WkjAAHRWIslSnA582zs7BQ0Rb1xuAACEwcAAp0G6EtFoK3EF1Hi6jYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP3mkjAAHR_1JKISe8aw-gT2p1pxkb0QACFAcAAp0G6EvkOcUBZAxm0TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP32kjAAHRTDeCkVllwux-01uPugn-ggACFgcAAp0G6EtDOFqN1MIHnDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP4GkjAAHRbDZjRNlh_scJnDXuAAEtMbcAAhcHAAKdBuhLb4yzrsLENmc2BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP4WkjAAHRvme0BZ1A4tl7eXFJSxO7lwACGAcAAp0G6EsIhynFutkrdjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP4mkjAAHRoZunRJmgsgdv3WLWw_SErAACGgcAAp0G6Ess28y7PVKx_TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP42kjAAHR_0VR3r2v3MbfK9jx9mS96gACGwcAAp0G6Ev4rT6OBjqBuDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP5GkjAAHRseR5jrjAMPhuIF9XCjG1BQACHAcAAp0G6EtJbTgcFDCTtDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP5WkjAAHRBL0uNwWXMYogSrUmjl7oFQACHQcAAp0G6EvT3S5DmAVtDTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP5mkjAAHR4YN0cnsXLVBbZpweP4WxrQACHgcAAp0G6EsmbKB8j88qhzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP52kjAAHR5bE3Bgz_bpKcsiLpgXXOygACIAcAAp0G6EuAsFeAHad45TYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP6GkjAAHRMtZ24eHODC2f8lnEFcPbSwACIQcAAp0G6Eu-mwr_jkvqfTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP6WkjAAHRTvO-ZpWkO1t9LIosK9BxSgACIgcAAp0G6EuteXQ15rcUJzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP6mkjAAHREVO8e_j_z6U66AQJrnLZ0wACJAcAAp0G6Esy6U_Ywi_wsjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP62kjAAHRkNuMZPrplRvoArgZ4XRuTQACJQcAAp0G6Et6lDPb22xfTDYE", "type": "audio"},
        {"id": "BQACAgIAAxkBAAIP7GkjAAHRhZdv3Gi-nneTaYUKz8fSoAACwQYAAsBosEvk7UsM8fH8wTYE", "type": "document"},
        {"id": "CQACAgIAAxkBAAIP7WkjAAHRyf2qgCOatXo9dBJyP2J90AACogUAAnUO-UuKZDccvoAwZDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP7mkjAAHRNcvBGCXU8SDJKRdcvAxIaAACpAUAAnUO-UvEKKFFIbJdeTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP8GkjAAH3v9vKK_ltYStPhqArOWlx4gACpwUAAnUO-UuVVCJHju1GfDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP8WkjAAH34z-4lXzAGzQLZoopCA5XHAACpQUAAnUO-UvMq3E0iVPWFTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP8mkjAAH333FsxhQ943FhanDHn6H69gACqAUAAnUO-UuQrz7HxJ2-QjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP82kjAAH3BgSSrc4qMkyzH3WwE5LHXAACqQUAAnUO-UtGCo94EXTwLjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP9GkjAAH3OKflzomRlDH_zrQZJW1ZXgACqgUAAnUO-UsavslUbNPgDDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP9WkjAAH3zaaQFgWgHSr8MDFbi9BUKAACqwUAAnUO-UvROjS5cseGdjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP9mkjAAH38ScK4ErYGL-1ctANiATrqgACrAUAAnUO-Us-vEcVEnO4yzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP92kjAAH3Ik8VodJh1Urj5Q1ktqkfuAACrQUAAnUO-Uv36kQzQb4X_DYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP-GkjAAH3ow-j3glI6wABOJSk2ZJaIa8AAq4FAAJ1DvlLiMwG2DdGCkQ2BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP-WkjAAH33KRXryhAF7YdCefdD5zU8AAC5AUAAhpO0EsUwPEMpL5szzYE", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='Cho\'lpon - "Kecha va kunduz"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIP-2kjASDCC6zaGdcoOQABJC9WiivKSwADAwACGsJRS7XtLN5nTerwNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP_GkjASBg-0tZROOGt7k4PfF4NB31AAIhBAACM_1QSy8IgjgOIn2-NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP_WkjASD8p2h8vDKCfBaZBUaeCxhfAAJhAwACuvVQS3syqrjLhNfvNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP_mkjASCu4Lg5D1x7hQnUNIHrHqPgAAIMAwACGsJRS8bT6gWrd5trNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIP_2kjASDgk6buD_LrzzsIanCS0zAdAAJjAwACuvVQS44WDlyX-gsiNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQAAFpIwEgtTTp9MH0WtUsCrtK7XfugAACZAMAArr1UEsxJSpPdKfJCDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQAWkjASDdWvGMSHHDhTeYXd6DH2RgAAIlBAACM_1QS3nx55jqT8DcNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQAmkjASAKdrG4bOp-TsWbeuKjyoKVAAImBAACM_1QS51O_NO428JGNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQA2kjASDz34_AcIx7UCo9O6_aIDqMAAInBAACM_1QS0x36FwEi2xaNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQBGkjASB8-OeN9KIJYjYT4CdTvqCIAAJlAwACuvVQS07hGQI6IWDdNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQBWkjASDbt9jfRq6ds-1dTJG7WhVbAAIpBAACM_1QSzxymE-DKaDRNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQBmkjASCya6lJCJp8-LBMnV5MI45hAAJmAwACuvVQSxWjjMaqKK_5NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQB2kjASAe45NXHb6ZeDnp7mHY4IM9AAIqBAACM_1QSx7c31pNZcTXNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='G\'afur G\'ulom - "Shum bola"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIHpmkgqYuhEzK35yp1SegfcEaRQrguAAKMBwAC_kmxSDrDnfuuQ3hkNgQ", "type": "document"},
        {"id": "CQACAgIAAxkBAAIHp2kgqYufQqsrYCZrkZv20t6T7SjjAAJ6BQACrPG5SO7WF2Ji2VnxNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIHqGkgqYsAAToKf3gkz8XTHLCrzbfOVgACfgUAAqzxuUisv-NMcpY4sjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIHqWkgqYveDUcxqwREZ_fu4BqBjak0AAKDBQACrPG5SAsNGwarXre7NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIHqmkgqYtck9pxWVgVG2SgToOAZxW7AAKFBQACrPG5SKo585AqMgJiNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='Tog\'ay Murod - "Yulduzlar mangu yonadi"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIQD2kjAWaVvV5fY2h5kQtesmvp2jvUAAKRAgAC-SzYStgce9hTGJclNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQEGkjAWavQ51xa9tZ5SzxQqcJdE6vAAKTAgAC-SzYSufDfszivVd7NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQEWkjAWbJeApL1BHflok-JEUWi_eFAAKUAgAC-SzYSo7jPTQfXl5GNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQEmkjAWZRP6IIA3V_R5I-2eSH52wSAAKXAgAC-SzYSniGrveTWd5NNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQE2kjAWa4m7pUXLYoEhoa_26tT1oUAAKYAgAC-SzYSjyOGB9wCygDNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQFGkjAWY82V5YG8USuSswo9aVSkf_AAKZAgAC-SzYSiD3ELNXRG2QNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQFWkjAWZTpsyuQQT7MVG9WdMdWnEBAAKaAgAC-SzYSi8VhGgFK1QTNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQFmkjAWYdWmJWhCHh-Qc8l83c4_l0AAKbAgAC-SzYStWUIzPk62CVNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='Tohir Malik - "Alvido bolalik"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIQGGkjAYiV0z2JLFBovuOyhtq7irnuAAKgBQAC5X55SKQy5Eb9TMnJNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQGWkjAYjMTUP3xcJkr9fA6_iV7kXVAAKMAwACDnR5SK9zWtpQDAYENgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQGmkjAYirSuxt_Iod055mnP7vy6YmAAKkBQAC5X55SMZD_5IV5kGxNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQG2kjAYjwct_0VZO7RR8jef2gqlYmAAKlBQAC5X55SKbf6wkOMla3NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQHGkjAYioUcd9lHiGfE0aDqsq2vdDAAKRAwACDnR5SIbok1SHjOOhNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQHWkjAYgd6lw-0y-WP3NhhT4rGayCAAKnBQAC5X55SFXT5WPux-8TNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQHmkjAYgh_5m9yhhfVS3lW6q0yCfrAAKpBQAC5X55SA2zIzmZ9f2mNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQH2kjAYgL6b071SvKixUv538xPVraAAKXAwACDnR5SNB1hh-Y4VHnNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQIGkjAYjqVe99suK0amw_eayY3DirAAJvAwACDnSBSL-y-w9ZNtwoNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQIWkjAYgMjBdQ58hlA0JZ9-NK_GhGAAKzBQAC5X55SI6Iad18zZJaNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='O\'tkir Hoshimov - "Dunyoning ishlari"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIQI2kjAedG7zrEke0mp2s6VkkS3vDCAALaBAAC0iB5StLnAwSGQ3olNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQJGkjAeeqyFqj6VNqASJtGSla35q3AALYAwACmYZwSkgBnCFHd_QKNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQJWkjAeeeP8X7C0ketOmd8FJfr8xxAALZBAACH115SqYtG2n55Q9NNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQJmkjAeejnaIikuSpuvhkmt6wN1TZAALZAwACmYZwShLJsIRUGpWdNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQJ2kjAeeSzoQI9ZSX1AABkVLcJlAqrgAC2wMAApmGcEoBHwbmvSHFPjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQKGkjAedRO5HcasiXQfn1Lb2-z1LFAALcAwACmYZwSi-YF0Th0E0aNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQKWkjAefmLUH24nweR-Qjq7rMxGekAALbBAACH115Su0AAdUhpLvVIzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQKmkjAedNbhjsH30WFBn5atEu0-6NAALcBAACH115SphnZNhTTHS-NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQK2kjAef0ip1eBwVupC0xCkm48ZkeAALeBAACH115Svo4j78QL2AtNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQLGkjAecCmYugiTwIYzZ4vy0bkKw4AALdAwACmYZwSqqtAQJqbWj0NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQLWkjAedcEqHqCc4I1K93ET32NxsfAALeAwACmYZwSn_9S1F0iyCtNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQLmkjAed0kJfqNei8VCTd42n-hgewAAMFAALuqolKmFogsDVuh8E2BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQL2kjAefE_eBgFeO2w9D8JRKw5ixnAAKOAwACXa6ISgjZQzBkBi-oNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQMGkjAeehuNsPkO0EspxxyTg1lSXFAAKUAwACXa6ISiy1110fk4-7NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQMWkjAefD7DHr1fs4RxrjDZqeEKsAAwcFAALuqolKbh4Cfxu3IWg2BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQMmkjAee_MO_s5jXjSlOjNtcBgjYvAAKvAgACJFyJSmhs_V8t0LqXNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQM2kjAeevdy7xrK2MjksnIDXbaPOEAAK2AgACJFyJSnOOdcSmO2xcNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQNGkjAedJosEkcR_QJRgQpLcv_h95AAKVAwACXa6ISh0JKMSUXAmKNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQNWkjAedxJBuNEg8WBo3aTtxqNPG2AAINBQAC7qqJStwXoN2jUH2KNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQNmkjAeeW0g5Kg3rDd3b4gNy1dMmDAAIOBQAC7qqJSuq-XH8iElHDNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQN2kjAee8vj5RmQMKLvi1giS2YmvUAALDAgACJFyJSnpBkZbXAAGuHDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQOGkjAeerAa0XqtxbGOtgnGvIcA-tAALEAgACJFyJSgRtIZ0h76fONgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQOWkjAedhstToTr2NYzle36etHWm8AAIxBAACnNeZSmjJXiliILSiNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQOmkjAefT_MnZ5uOI7z4lbv1y6Z4FAALGBAACXa6QSglT423I-3uMNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQO2kjAecG37Pd7v7G1eI40dsbfIHsAAIyBAACnNeZSobBZxFW5dkQNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQPGkjAeeRzDdOKNfGVeOfUkk2rH-vAAI0BAACnNeZSvacfFLKfE3xNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQPWkjAefdhYRnzfMBXDPnzkrdrFD3AALJBAACXa6QSvw-LBkyATVRNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQPmkjAedYIWfAA5GhpWErcAP92xYRAAI3BAACnNeZSlZpgX-pUd9xNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQP2kjAeew5QiyUVtH8rj8ahNjN-hqAALQBAACXa6QSv-eUEwrTWOzNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQQGkjAecdgCJl35JWW0YzJzLENzjOAAI4BAACnNeZSrr5EW8nXzzVNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQQWkjAee7FCgK7MolwexQfiz3UidwAAI5BAACnNeZSiKHJKqZSLtSNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQQmkjAedFbCSIFTISyeFuvLCwjQ6CAAI6BAACnNeZSmzqrLeKqE2VNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQQ2kjAed_lyyoPqgsAy7Ey5Yr0fodAAI7BAACnNeZSs3HFYyr7hOzNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Hikoyalar")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIQRWkjAiCLZw7iP9d7Ll-YrQlgN6lyAALAAgACovKISRvaKKs2n-IAATYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQRmkjAiAaOeixwgTOIbAD-Tmh0jB_AAKkAwACtGBYSDxw-iURcW8WNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQR2kjAiDVohr7cbhZXGTu1ClEj6ujAAI6AQACqpFpSxHA4zRtDIqZNgQ", "type": "audio"},
        {"id": "CQACAgQAAxkBAAIQSWkjAiBp0Z0hw_YS7ypXx-H2G845AALIMQACPR5kB7ge1QsfRxZQNgQ", "type": "audio"},
        {"id": "CQACAgQAAxkBAAIQSmkjAiA_WVSvqrC1HWohh_KtR1QAA54xAAJKGmQHO7Ods5U0yeM2BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQS2kjAiDIFoTYa4pq6bDljHs_lSzBAAJ8AwACw_hISubSaI04lb8LNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQTGkjAiB64Y9AqSa3zBAvEwJjPoqtAAIPAgACbPpxS4tPWSpEvwNDNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQTWkjAiD_6GsOdA4ynYigMzo-E8ZbAALFAQACnUn4S4BCGWipewrRNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQTmkjAiA92_oVr13t1lNP-upRVWNAAAKEAgAC9ihJSEIYRG7njJTaNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQT2kjAiBnM8iRd6BOghERIR0iNU2sAAKdAQACDEXAScJC0Ui2OBLGNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQUGkjAiDqemcMYfCMoFYNJDb2jHr_AAKrAgACSrDISedmi1mWBIddNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQUWkjAiAXnuWfgftmCOv9bamx4-hLAAIiAgACKBZwSUkt5xk2eT_KNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQUmkjAiBoJU_6vhCH_Zcqm10TUAYAA08BAAKLKPBIpYIfN04Kj4A2BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQU2kjAiBnnTgh-l9mLsnzcuoVpJW0AAK0AgACSfM4SH1vgYXG3aWpNgQ", "type": "audio"},
        {"id": "CQACAgQAAxkBAAIQVGkjAiAKJNXsxdi7u1LUny1h99VxAALCMQAC9hxkB6l1_Z7YsGsFNgQ", "type": "audio"},
        {"id": "CQACAgUAAxkBAAIQVWkjAiC4JO38C-BWs5NeSRDl5IlYAAIzAAMWq0hXqxcoUkd8FI02BA", "type": "audio"},
        {"id": "CQACAgUAAxkBAAIQVmkjAiAMZPHQfT4iER6Q39pRih8QAAI1AAMWq0hXmnFMTpYR9kg2BA", "type": "audio"},
        {"id": "CQACAgUAAxkBAAIQV2kjAiARLqyprGx5QyDvbZfKGbIPAAI6AAMWq0hXw0DMjk607lE2BA", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQWGkjAiAle94B6YW5nrIQgy3yp3IVAALXAgACthaJSsAkcsg6_pxpNgQ", "type": "audio"},
        {"id": "CQACAgQAAxkBAAIQWWkjAiDtKMMiQnPSv5Xk4d8Wq_uCAAKbMQAC0hdkB9j_QZ2pP9XaNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🌐 Hikoyalar")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIQW2kjAoIJwFXVoETLY8N1nNB8S6dOAAIRAgACLXoYSNTMFP7UI20XNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQXGkjAoL61OjFvF6WgTGocxhG5PiaAAKeAgAChMgAAUlvtl5nHbmt_zYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQXWkjAoKj50lEOg11eyWoiBYlPvaSAAK1AgACSfMoSF55yueOxNj7NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQXmkjAoJHqaJU45vthkTD2zqFmd7HAAIlAwACvyMQSPDJlNgKgeYkNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQX2kjAoIstHrXjs4OjUINubJ2edlpAAKTAgAC7FxoSFkAAbV0wzwNqjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQYGkjAoIvjvzDikCBtblKYetguluCAAIYAwACLogRSoRs92LAVgbjNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQYWkjAoI_oy5BsuAtFS4mv5xk3BZQAAKOAgAC6o2wShkHcGXvZd3yNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQYmkjAoKJ4ePNHp0dCmXrV8STB122AAJAAQACBTNISzevAAEmOJKUFDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQY2kjAoLv-NqpBLZIXfl-SKzeF7cTAALrAwACLN8YSgm-F4wmYQ6GNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQZGkjAoIUxT8oLtNGqfdQPs8UOw1LAAJLAgACjldQSP4bwQYK1FchNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQZWkjAoLLVlso5H1PEGhQSRCrz2uiAAJNAgACJfgZSrXJLb2fgg_oNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="O'nta negir bolasi")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIQdGkjAsq_roZdW67-JK6JaA_vrjP9AAJyBQACtzzASH5U0wHtPE3-NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQdWkjAsoXQqESCUHGWM4sjC31efEiAAJzBQACtzzASKsxz5dkWm-fNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQdmkjAsqvFIIhEI64QQNqyXAOwK-7AAJLBAACT23ASIV3T3ucGVdENgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQd2kjAsoYIl4Ry80tKskqqAGNLudqAAJ0BQACtzzASKJgn-nPA4V-NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQeGkjAspEIykdzqjtXiAccVDeTCPyAAJ3BQACtzzASICcCugUQj5pNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQeWkjAsq1HmILx27NlHOpTnaNDzNVAAJ4BQACtzzASJmME9G5LFQpNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQemkjAsq8OYhT5vJoBjkWVgwSoOreAAKgAwACGJnBSCYbY4FyYueENgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQe2kjAsovL2hZ5M8DdD10YNE8yL8HAAJ5BQACtzzASF9SYVOeDtTvNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQfGkjAsohb3DPyTnx7IW0jB9-lwZnAAJ6BQACtzzASJOlNcnUxhdvNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQfWkjAsowGLxxLaqYYmBsi5fWGJDuAAJNBAACT23ASB0YaP0VU0iLNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQZ2kjArCBIXzyXPmhf3D2CaF77vcfAAJ8BQACtzzASMBQZL5q6qOcNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQaGkjArCeMgL0P7TEIxoKdN8HqZ7eAAIhBAAC8kLISMYevFg19L87NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQaWkjArC3StQr8WOha80tSbGOoC7QAAIfBAAC8kLISPcjpr1Wr3XzNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQamkjArABxzCjGG4EhXR9TMjomLwaAAL6BAACT23ISEKLtpjjT0onNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQa2kjArC5-NZAQS3ogekJd2uVBTrMAAIiBAAC8kLISP4t-dTj4xtgNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQbGkjArCh2hOPvMgqudQfRUL-f5mtAAIkBAAC8kLISOsIQ4zsUWXlNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQbWkjArDF6tRl2Merlf4J4stiW7m0AAL9BAACT23ISODnyBd-YGL2NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQbmkjArDZCfT-KyYvHIrRdn_m-PDYAAIgBAAC8kLISPAk5e_pndRtNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQb2kjArCWAAEI6cdmMTTXsB9Joh2vhQAC_gQAAk9tyEhoCZA5scYffzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQcGkjArB4fTvYXaEbo27I0obYMGjcAAIlBAAC8kLISIImFZX9lQQWNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQcWkjArBHdqCsLgR8fYsZhbkFdUWHAAL_BAACT23ISNGKn6sYm75TNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQcmkjArA66XwkIHIDNqFtOHNcDYm5AAL5BAACT23ISAyX4sqAvnPjNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Dengiz sarguzashtlari")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIQgWkjAwtgKNWqhjW2VVFjP_PBDNuTAAIIBgACuALASwVD1ypXcQeQNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQgmkjAwtngXHrHLekBIpFbqLNXoScAAIJBgACuALAS_IWXMhA7eOXNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQg2kjAwt5c_XysjJXYIwkXneT4JQ6AAIKBgACuALAS_Trt3ZKWJODNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQhGkjAwu_YHaqwBICiHpveYeE2klyAAILBgACuALAS4EaapgXwe6jNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQhWkjAwuWDSdcaWNZ7JkHty9z54h9AAIMBgACuALAS5at3gsXhaj-NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQhmkjAwvZ__d_kwqo60qrU2-20tEfAAINBgACuALAS4978AbodQPlNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQh2kjAwuGB-nP4622N3t_fseDicqiAAIOBgACuALASxUNi46H96_kNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQiGkjAwsyMVI24cXR076gAelgawY-AAIPBgACuALAS_WZohrt6GXtNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQiWkjAwvAOAnBrvxIVHHOQUcY1c7AAAIQBgACuALAS6Rqa1GfKC9KNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Graf Monte Kristo")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIQi2kjA6s9fcq8T7HKXsYO0qx1H94BAAK_BAACFwgYS1bJnAy3ok1XNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQjGkjA6sSRDzhncH86m43UEYPdSvVAALABAACFwgYS4X-NQE7BPtuNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQjWkjA6t5qKp_JtyIQVDjGBV8JQN3AALlBAACGUsgSx9JKfYTqd_WNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQjmkjA6vMNty_bTJ0P1lUmH-EvhEvAALmBAACGUsgS9PlAbstlRy5NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQj2kjA6vzGmwk8jqNLYrrL6fSrx7-AALnBAACGUsgSxnmw4ZWnOC1NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQkGkjA6uDIKB9iNo-hJmwI8NZ8OgLAALBBAACFwgYS0QPdEtTqMW4NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQkWkjA6uxlzc1e1gJEAjF1AYmB9w5AALCBAACFwgYS_yWUY_0zVboNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQkmkjA6sXOW0pbaKlYNAcekcdZIxUAALDBAACFwgYSwuMGEW8TuOZNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQk2kjA6vzpxWgOmKRJ6NZnHQ9Lao6AALEBAACFwgYS4Hq6hkrquw8NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQlGkjA6utQc11HBs7SlY3s3IDPMlJAALFBAACFwgYSx0ssD2VnMDlNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQlWkjA6tZJuxKk3sAAYIC-HcXC1nALQACJgUAAhcIKEvZ1HOlsRGkLzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQlmkjA6sEt9iZTu_ii80AAcYR_p8ZEwACJwUAAhcIKEvsuZrToXvVHzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQl2kjA6vzxqxkCYkMMMLIi9oYiTQ8AALDBAACGUsoS-JrKkV_AAEejTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQmGkjA6uowidvdTkQLKNGy7pmY9fQAAL6AwACGmcoS_2MgZUCdyJsNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQmWkjA6vJJTQXA-qa7Gc3AAGakQdV_QACxAQAAhlLKEuj86qjTd2vBDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQmmkjA6u5ITPy4KUpIO7IIzgloFVUAAL8AwACGmcoS5LyEQ7yzk5_NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQm2kjA6tuxxWRkwsR54wp2Tgd_m9iAAL9AwACGmcoS9O4Trbq7sOoNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQnGkjA6vMGLUEL1xR4yCbdQULudDYAALFBAACGUsoS26KrFfTYo0NNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQnWkjA6tokoIawD28TGvFe3LOKd6CAAIZBAACGmcoSypCif61e0xdNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQnmkjA6vhUjLyTa3bCQ256UMI5BZhAALUBAACGUsoS-1avdIj5EjDNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQn2kjA6uejr_2xk2zS_Lm4dXqVG9EAAIUBQACGmcwS6Sf-x4FnivVNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQoGkjA6vtOfXcSmTw2kvSNURlHLMiAAJ4BQAC1fgwSz1z7OH0d3_BNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQoWkjA6vmymVHYrWSHURx0CmADMzKAAIVBQACGmcwS61KisqN-1JsNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQomkjA6vL1jFy7AwatopM2ks9zfMRAAIWBQACGmcwS8XWSe1yJt2xNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQo2kjA6s-RXFJTNpReV7r2trJ25-rAAIXBQACGmcwS5QAAbekmCMNtzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQpGkjA6uTaLj5ob3g7ALw5Y226sk9AAJ5BQAC1fgwS_5InTQ7uvChNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQpWkjA6uUMBcib9hAPhz7-o0kPSOdAAIYBQACGmcwS9TPpNiPqzjyNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQpmkjA6sY-bNyV8JqXwJh4HNvUnF_AAIZBQACGmcwS48hcd8U2TuJNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQp2kjA6vwAmxu92j39F5a2cP6ZwXBAAIbBQACGmcwSyefKVi20ZFxNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQqGkjA6vT09f_ZxigmKKDOD1AupydAAJ6BQAC1fgwS8J2bOdnSeydNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQqmkjA8wdIBR5WFMYKQRFBpHhAePJAALUBAACK_tAS5T9t6GsPeypNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQq2kjA8yn-yA-jCshbmGGsXxgJuxKAALVBAACK_tAS9AUgeTiCc8ONgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQrGkjA8wI5tDSqHCLRwMfKFgr-e_XAALQBQAC1fg4S0iiof3zQBT8NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQrWkjA8xaOBwylriWGwJl1AcMImVrAALRBQAC1fg4S7Pgtq_Y19FqNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQrmkjA8wDevz0jL114UyZY3ZoruVmAALWBAACK_tAS81IFMlKoad1NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQr2kjA8yayFFAW0FAvFPgQrXeQKFcAALXBAACK_tAS2uUN5-P-dpJNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQsGkjA8xiGeP1QXco3fNRnUgDuWXyAALYBAACK_tAS5gIQTZbgAnUNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQsWkjA8yE8xs67-VXGsnfGTkubwnXAALZBAACK_tAS9EtkVakISAQNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQsmkjA8xyXjaXmlUaCyud0DKfNExnAALaBAACK_tAS6EkqchSAYC7NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQs2kjA8wXbt7GeOBgVo1Y6YvjE-nbAALbBAACK_tAS-UJ0tuF1zO9NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQtGkjA8yB7lRPq06z6HjuaiF3fHg7AAJbBAACUjFASxjlJdnJODv0NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQtWkjA8zAvocAAWTJtYBBIK2P7u6SlgACXAQAAlIxQEsdjMj4gqYyhzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQtmkjA8wmEjgwQwYECcdX_GgthXu4AAKhBAACK_tIS_f7UEVhkzMaNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQt2kjA8y2dNDIHEKVvjCSzcRhnG0lAAJdBAACUjFAS6QG6QvlJc10NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQuGkjA8y74RgJQhdIpkeeckJv8v5AAAJeBAACUjFASzlUpnkV9yawNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQuWkjA8yzviCUk7tU9TpeHqcf2OzPAAKiBAACK_tIS1HybNt74aG3NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQumkjA8wKyLHPnX5LMdo7tYLjZo1HAAKjBAACK_tIS_fwEUmuQqBsNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQu2kjA8xHAAGT6BqQTJHUb6kQdM8w1gACXwQAAlIxQEvm9oMGVhpqAzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQvGkjA8zD0RWY-LnWSssHMaA2Uu1gAAJgBAACUjFAS03IwkUIzusGNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQvWkjA8wOwsmGPfM1j5TfQly8_1N4AAL1AwACS4FRS1lZmA_mnYhdNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQvmkjA8x10LkFKHpDzlD7bDKIc_oFAAL4AwACsBRQS3Huj8OW1FimNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQv2kjA8zH8oBTJdJ4gNpMjphyWzftAAL5AwACsBRQS3CNv9oxCFysNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQwGkjA8xvCG8FAAFCUQ7Nu3oEJvEbcwAC9gMAAkuBUUtB21dm7QKTpzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQwWkjA8xUJqnlWvWH-QFOgSLNphWYAAL3AwACS4FRS3Ryv9gUwae4NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQwmkjA8ydndvucMpbRCkfE2mmepXCAAL4AwACS4FRS4rZfHHPxHRzNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQw2kjA8ywtvmLUjQtttcrbTEAAbzL-wAC-gMAArAUUEvOiW0dSprEPTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQxGkjA8zFVfiBoJchu0MjTOx25VrwAAL7AwACsBRQSyyNoiKWAAF6NDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQxWkjA8y-2UMOwzj1Tr_WsDjTwDfZAAJhBAACUjFAS9oRstxtVCDzNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQxmkjA8wVAAF-i9Vy6WT0Xswu4TUBcwAC-QMAAkuBUUvwdaLfIQ4vRjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQx2kjA8yVU4qipEa25augaRB6rRtXAAL8AwACsBRQS2_kcNQWs7isNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQyWkjA_boCnF6VB4t2JpdL3G-KvuAAAIgBQACYcpZSwkqYujR8GJuNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQymkjA_Y2gcYXulI8T_Zwy1dVjSobAAIhBQACYcpZS4ayA1k9VjcQNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQy2kjA_YbWMRfFyplOYepAWL-dgPGAAKUBQACsBRYS02VP_uioriDNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQzGkjA_bw7kltU8MenuLQ2LRB5MqsAAIiBQACYcpZS7tBmvk-aBteNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQzWkjA_ZT1QntefgbI4o7VJxmX58SAAIjBQACYcpZS1rOsgM0vO4SNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQzmkjA_bY1fO6K4L-W5B3HY3ufXzcAAIkBQACYcpZS39H-iyNEbT2NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQz2kjA_ZRK08BCqbsUDZLO0-m5399AAJAAwACYcppS6XZV188qypANgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ0GkjA_ZkR6-GKFvudv2TA9ACVSXkAAKvBAACkHhoSxuYzV8EMPNbNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ0WkjA_bjYhMW3Ohpx0Y52yf21WHyAAJDAwACYcppS_afWn_ifW7kNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ0mkjA_YXtniN3As1vVVHwtDaLzDtAAJGAwACYcppSzubk9pQS19mNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ02kjA_YZciiY4ebwLdlbwPfutgUsAAJHAwACYcppS8bqaQeO-XywNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ1GkjA_ZsvZneFF1bG0ER0ZKXiDz7AAKwBAACkHhoS_g8lKcMZM1wNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ1WkjA_bW3yFPrpVPeW2k-7q-HLJzAAKxBAACkHhoSwoud6bA5zdiNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ1mkjA_bFQh-FyO8g4IwziRSmYvWdAAKyBAACkHhoS2tQzGLHHOA4NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ12kjA_YUsdVVepnhkFiVi43MWOjCAAJJAwACYcppS9fDNTWWR7nKNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ2GkjA_Zxo9rXbW9HiI-EuS-b04-8AAK0BAACkHhoSzhUmvJDfN43NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ2WkjA_aGV8qnS30VCPbcrIRLrkWeAAJjBAACHm5xS5aOsiOBaAHvNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ2mkjA_Z3DNy7CdgfJ1dUyQlHqYqdAAJkBAACHm5xS0URxB1f0br3NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ22kjA_bqND3kjG6tPZjkBfBijMSFAAKeBAACBJZwS-3NAAF9fuabRTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ3GkjA_aCiuESqtzT3o8ipMNcS8nmAAJlBAACHm5xS1IsXJKmfvvdNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ3WkjA_bA8g8eDOgiGUSKt8nhvSqnAAJmBAACHm5xS2bwQPvYAAETzTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ3mkjA_ZtdyUael6L4M4a66DqgyfUAAJnBAACHm5xSwHWijiGOmLeNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ32kjA_Y4DzWvgdK80Ikfti1DoKUSAAJoBAACHm5xSxB2duPUhwABhTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ4GkjA_Yi9pWLUcya3oM4KJQzhxzCAAKfBAACBJZwSxObsMoeMNqoNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ4WkjA_aocfLBJvuybwKEkFcfFGpYAAJpBAACHm5xSwzZ5cg82NyJNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ4mkjA_ZstoIRczqNXtbtK-HhyydTAAJqBAACHm5xS4VYQ2gVfmreNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ42kjA_b5QoXWIrZwHokffymLLBzUAAKABAACTXN4S1pL1mu5QITONgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ5GkjA_Z_0ktqGdjQhkr7o_XsWxRWAAKBBAACTXN4SwiLk2mU3PTxNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ5WkjA_ZOEucbX754RaN6ogdS67srAAIuBQACNc14S_Ln-7GECF2KNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ5mkjA_b2F5vj5gzqMa4xAWAd2gpKAAJfBgACBJZ4S4gGCaAM3RUbNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ6GkjBBa1l8LFuuZbt4UirvcxyL2RAAIvBQACNc14S1U_IpjnaQ5CNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ6WkjBBYi7JAW06j7svOm_jdSHQ4wAAJgBgACBJZ4S20fl18MlzIdNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ6mkjBBYoOksgcptjUEVNJaQLDo7dAAIwBQACNc14S8cKiOD1bOQMNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ62kjBBZUVS5ro7K2-BN8GcQYuWDnAAIxBQACNc14S-YKBHbSgpJmNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ7GkjBBZDV-SbPF95WCCWlAtfTVytAAJhBgACBJZ4S2RM2J-aWD2jNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ7WkjBBZjxcDQuZiUTnkz0mMN_dTcAAJiBgACBJZ4S8aDvcepfjSsNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ7mkjBBb0yo9yDHDbctisdC-nz3U0AAIyBQACNc14S7qagLhNUY1nNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ72kjBBYLkcuPXt2EKTxMxLBaBFFPAAL5BQAC8fGBS8kB3WHMvYw7NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ8GkjBBYFjVbFUjYGCpuQXTYF90Z8AALFBAACTXOAS0t7m-yRHBfSNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ8WkjBBbOJsJ6rTsc-licA6ey9rSJAAJZBQACNc2ASwy8m_apk2zMNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ8mkjBBaiB4wY2l0RNCmjCaae2MCrAAJaBQACNc2AS2UnMUONy3idNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ82kjBBYK3M5holUKNhLFP2eIpzFsAAL6BQAC8fGBS5az4xK4MR04NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ9GkjBBapsC68POKCRm4NNHCzW_yIAAJbBQACNc2ASw_sNwMcjUskNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ9WkjBBZEhAc9xzyMzmoO9hgwIt5WAAL7BQAC8fGBS8EFzdgP-bmdNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ9mkjBBbRWuSI-CqyPVp6Bky0Zl5YAAJcBQACNc2AS-9za6fQGMvZNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ92kjBBahrsevMRhr9Q1Aa9fMIja6AAL8BQAC8fGBS9PW9M63d4z0NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ-GkjBBaxAYLS1qqAHThmlNDPvcfkAAJdBQACNc2AS735mtCTLjWQNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ-WkjBBbNniKYzSVIvnfKFiDzU-P7AAJeBQACNc2AS1mdVgOo3PfaNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ-mkjBBZBNB1XDKGy4IUrTJW_6mY6AALmBAACVs6QSz6C7qS2G9hXNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ-2kjBBbYIf8NEpPkpwNB8wiO5LGRAAJLBQAC-E-JSxBowxmHy2F_NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ_GkjBBZ-x4C7dP0Zhxm7gDDxQo1hAAJMBQAC-E-JS36tVVQz-rMlNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ_WkjBBY3yWS2NW9X4P8pDZWTxNquAALFBQAC8mqIS_7ztpQn1pFONgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ_mkjBBboWKOEqrvjOu8YVUnAq0akAALGBQAC8mqIS1DXJlFeTRWCNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIQ_2kjBBaxu-9zySF_HavGObjhD6MTAALHBQAC8mqIS06fPwAB_4wpUjYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRAAFpIwQWIRsBqT8UcFPr1pXq3CDDkQAC5wQAAlbOkEsG8dCSL_1F5jYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRAWkjBBYSCmUe9yXNfcznKffzV8TTAALIBQAC8mqISwNYlhhlXc5rNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRAmkjBBacRl7JzK9EfyO9mrxG4pzCAALJBQAC8mqIS-bP6H95Hk-9NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRA2kjBBYOWgqqVAHjuGbEPMTunWY3AALKBQAC8mqIS98tID2RiaBZNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRBGkjBBbXQryHwHzT5WiqghhoA8YuAALLBQAC8mqIS64Lvpaezs-TNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRBWkjBBbZyduzrj9lRg9w5_HU1BAeAAIxBAAC_PqYSz-rliEguJ6UNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRB2kjBDAOzQ3nDjoUnR2dZfgvWElrAAIyBAAC_PqYS9-zqv_tyuf8NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRCGkjBDCJyrnjYQUjhuitj0vbXhiRAAIzBAAC_PqYSywbpJ02aRiaNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRCWkjBDBYZF_3mwOTC_ZNMJ8-N-4rAAI1BAAC_PqYS4e84qXthVw5NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRCmkjBDBzHCkp-nwCD3ln7iklOVJ4AAI2BAAC_PqYS1ZKWKpKb0_fNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRC2kjBDBA3yG3q46YeiKRm209jxLlAAK7BAACpVKRSwN0QsRRdWdsNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRDGkjBDDBg9GQfrx3kg6xrYNYv5guAAI3BAAC_PqYS4-I-kPzkQ13NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRDWkjBDDxvhXBHdTtg_Do86cb2IZbAAI4BAAC_PqYS8XNAAELvdvUHTYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRDmkjBDB62RBhsq2wvcF1m1Dn5WBIAAK9BAACpVKRS-P9XsLCDt1yNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRD2kjBDCQNfzmV098orH0_LWi84TOAAI5BAAC_PqYSxIlUjM5M8wrNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIREGkjBDAcl4OHt4O_r0tQ5DwWBszGAAK_BAACpVKRS6LTKTB_aoAAATYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIREWkjBDDD_4rcalCEWhe7Ein3UPMtAAL1AwACu6CQS9Is4UeDViYJNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIREmkjBDADsPX8n09ZqJWFYVKga8ckAALABAACpVKRS2aGqALDe_gbNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRE2kjBDBawebw48iaFUkPtVj4Ou4MAAI6BAAC_PqYS44peWROmmuzNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRFGkjBDC-zFYt7y1I77YWd5oJg-3jAAI7BAAC_PqYS8sAAZ5nRF9rizYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRFWkjBDDHObuHkthrxo857ZoIExiPAAI8BAAC_PqYS2DkKe-7wge8NgQ", "type": "audio"}

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="O'gay ona")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIRF2kjBFpQB0aHVcyQIE-9PAf88-C5AAJYAwACL4agSswt0ayltvk0NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRGGkjBFrsSLsSUQa-0b3wCu-IG2rhAAJKBgACryagSshijVyw84L9NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRGWkjBFqC5TnDyMKj5ahfoEZGIvb4AAIrBQACauGhSi3U5rr9iS3ANgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRGmkjBFopYMwVv8RdSwi03KDk-7vEAAJvBgACryagSqWWS7OM_cI9NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRG2kjBFoaOFAehre7wi-Mizc3dHQOAAIkBQACd6ygSoRtG-fwm1dyNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRHGkjBFpLwfqMTzPEm3lDMTMoZzl3AAJ_BgACryagSq0vRrZfUmNXNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRHWkjBFr4hUXWlXIKtGn7QhWffkPuAAIpBQACd6ygSpKvVHeJYTILNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRHmkjBFo3HZDyc2TummJ3Pz1M84MAAy4FAAJ3rKBK68FN8hWlIXg2BA", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='Chingiz Aytmatov - "Jamila"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIRIGkjBHsWMCWqMKQZMq1L2oXQX0NCAAL3AwACRg3hSSaGXk81QiqRNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRIWkjBHuyVHtOSSYzpjh8wIgjCGaXAAKNAgAC0lfhSZGMdGNdmCoCNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRImkjBHsQRoGzPDExcpe0ouriAAGKQwAC-AMAAkYN4UncGE_pbiZHYzYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRI2kjBHue8wABfWDJkkwjGz0tnIYomwAC-QMAAkYN4UlJo7akwml4vDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRJGkjBHukvkLVBPsZdU3n63Zk4zB_AAL6AwACRg3hSR07JIp7DV73NgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRJWkjBHv_c-TzoA2JdpXYZupVeYy-AAL7AwACRg3hSaKCOpqfEZPrNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRJmkjBHshTIGdV70_4AABItyuZoDSbQACjwIAAtJX4UmKiM247DmHkDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRJ2kjBHte1GY2NZ4NTgzYRjEvc0p6AAKQAgAC0lfhSZxWDUTUFEmJNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='Paulo Koelo - "Alkimyogar"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIRKWkjBJykaLedMe6R5bwLTRu8heZSAAK_AgAC9ftoSGxgXkyejbSuNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRKmkjBJxkgFD9IGnlv8Ap4AbJWFuyAAJVAwACwexwSN6_AAGJjVoDyDYE", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRK2kjBJyscpHlOS1zMXa7fmfHQ1nNAAJZAwACwexwSIsuzfxMM_EcNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRLGkjBJxfTqPwPN9qJcnwcI_0H57PAAJgAwACwexwSD5dF9ef_9oDNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRLWkjBJw9wlkxrKHa3b6Ia21-z7IHAAJmAwACwexwSDY8LrMFW88pNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRLmkjBJy5OR0s479VTr7TVP6QeTeHAAJnAwACwexwSDtFelyZHXNZNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRL2kjBJxON37ctWa-uwHQY4AJ5ixdAAJoAwACwexwSKsLPy-72nmjNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRMGkjBJygRfv9ijh9KvTquQFbT0iWAAJpAwACwexwSO5_1QLb8QjINgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRMWkjBJy-II2KK377iPaKH5ldkApZAAKoAwACn1JxSOYnRHP2EFuMNgQ", "type": "audio"},
        {"id": "CQACAgIAAxkBAAIRMmkjBJxtY1CX4esqS3APlSjm0hTnAAJqAwACwexwSDU3mUxfa2uHNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text='Chingiz Aytmatov - "Chingizxonning oq buluti"')
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "CQACAgIAAxkBAAIRNGkjBLaux80VRkQ5yHrCZr-5GWpNAALlBQACZ8CYSmyKahM3aKBlNgQ", "type": "audio"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📗 1-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAIROmkjBTHC3YQnacmIMLMKobz-PikfAALCCgACa75gUNMChhRAGIXvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRO2kjBTFKhV7Qnk0a7ZspYUI4DktWAAIRCQACPJN5SOhFn1BEduS4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRPGkjBTF6TZRHBTSkYKwduzxyFNyTAAIXCQACPJN5SOndZ1fTtmkUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRPWkjBTGiXTK7xrZKDuiGsJnZmR2vAAIWCQACPJN5SFCa_h2JDeifNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRPmkjBTF0EdC8tFUvKh_Vkbuw4xIRAAKzCAACPJN5SGiD0eVC5nb8NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRP2kjBTHYjAk0_5YMP5DmIluV5v3aAAIVCQACPJN5SGZzUEr2tgogNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRQGkjBTH3qc3dDMYytSPNHSmUeZIZAAMJAAI8k3lIvdGtFTF5Wbo2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRQWkjBTHWrMtaIszPs0rL1GrGK-f5AALaCAACPJN5SMQsIJ_20ByJNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRQmkjBTGaD3lBFJZ0Zj6vFxg4p2hGAAITCQACPJN5SE-g3-m2xUi6NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRQ2kjBTGXC_T57hT0JVgaXW1rXGqPAAIJCQACPJN5SDp35sJRk6QJNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRRGkjBTGUBOnfMVKsfIJjWX0afpR7AAIKCQACPJN5SBXp3oW6FrRgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRRWkjBTFCjtqgDhgEDo-fmiduL73TAAILCQACPJN5SIxWRKgy9jiBNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRRmkjBTHt7qVBlCi27BgulvAyL64EAAIZCQACPJN5SJFp81sTyWIMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRR2kjBTEoltn3WgQjDt9MpWXK6Te-AAIHCQACPJN5SBBsMuP9Lsv-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRSGkjBTEak7g5NqBQDg_u6r-XtxPAAAIFCQACPJN5SIJ7KMexXzueNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRSWkjBTHIt2kYKdoMFtGl8dmcIASfAAKaAgACWJX5ShrBofN2EPBmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRSmkjBTFjPDwOPc8Bz4l278qWCI1MAALNCAACPJN5SBjCsJH71j1JNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRS2kjBTHq1zNtmmo_QWZjlPkKAAF1pwACCAkAAjyTeUh78Lrgm80ciTYE", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="💯 Top 100 kitoblar")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIROGkjBO6uOeFF9ArnJDDnyH-74uI5AALfAgACb4_QSLY0PWhnFUpuNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📗 2-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRYmkjBdwSyUsepdkVp2-Ip3NY4hkUAAJSCQACPJN5SCD5J6Fhj2mQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRY2kjBdxEaHhFRmFLJXJ-jmvGtmBcAAJgCQACPJN5SEXdWN-Ks7gtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRZGkjBdyA0KST7qlAOWe4kiiQaldSAAJlCQACPJN5SPKJ4wjlls7LNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRZWkjBdyT6lUYYEBjJfycD45IjwPgAAJjCQACPJN5SMOGHt5ze89CNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRZmkjBdx5aClznyUdzSieRfPJuGnPAAJnCQACPJN5SIzrn5YmuVW_NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRZ2kjBdxrfQ6RJdywNOP2LmERTlcqAAJoCQACPJN5SIfRqugK_o5PNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRaGkjBdyDXuyW2Pjg0rgFBojbZqVsAAJqCQACPJN5SNE-1WuETXcZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRaWkjBdwpJW3vTeO4RqQFAAFGAs0jzwACbQkAAjyTeUgay_g_v4KWCTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRamkjBdyMYO5w9Ymc4uHOZsWL404sAAJuCQACPJN5SFvvkhkRWyoNNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRa2kjBdz9GLjN4vZrsBOfXPyAyXhgAAJwCQACPJN5SFIaUoBcFk_iNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRbGkjBdxmjJ7p4glRzBgYQ8ckybvnAAJxCQACPJN5SO0U9zP1lEyLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRbWkjBdzG3FeW-COOmBeJFuwMxr-HAAJ2CQACPJN5SDzEQby9esygNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRbmkjBdzcCuK15X8XLeFUOvzSrUlxAAJ5CQACPJN5SNT39vRXg3JcNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRb2kjBdxZTE2fWJqpxw9NTfBur0UiAAJ-CQACPJN5SDSZ54_oKYaUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRcGkjBdzyZk8eJbrM3tfdoDpFyKrsAAJ_CQACPJN5SNJ-NUwypBBuNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRcWkjBdy49gT4P6wVExEDv6lc7DNWAAKyAwACYwXgSIbvtgFmVRkLNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📗 3-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRTWkjBX7spCg_mzJ3znxJ6A02nVqgAAKxCQACPJN5SBpNXCM2IguwNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRTmkjBX4_Ng8xL2DLcm2Df9S-Dey6AAIzCgACPJN5SAiWwsB_5YjgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRT2kjBX7RzU9fowwwzOhpnB6lb65fAAKvCQACPJN5SAORu0HKYMuFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRUGkjBX7oPsWJjuYgJc6ZJZGjfbGeAAKwCQACPJN5SErJ280VOOL0NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRUWkjBX4oNlKot_YlSAI5AtGaAAHKvgACyAkAAjyTeUiACjT-fx0gSjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRUmkjBX799LMow83FpEtPsKrPhGhdAAL2CQACPJN5SAYFyMS5BVBbNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRU2kjBX5w2jlT4GcoWZH_YyYoW-WvAAL-CQACPJN5SKyAYkknAS1ONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRVGkjBX5bBlhZLdTJv45z41kzvreIAALvCQACPJN5SIPZhKKLXIgfNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRVWkjBX4W1A_54z_fFNwQ0B4U-X9oAAI1CgACPJN5SBd6EUzIyjsRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRVmkjBX6cE0pdNg8ULoF9JzHYiRtUAAIFCgACPJN5SIMfoUtxFq6FNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRV2kjBX5vwm0uWxYwGVlKqSyBvizFAAIBCgACPJN5SKnNcxoUE_qtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRWGkjBX5R3oH5xxwAAbteYK5KBAkJswACCQoAAjyTeUgdmuuBnqOeyjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRWWkjBX7wDmlBei-LMw745pk8p3LRAAIHCgACPJN5SAYmK9r24QhSNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRWmkjBX6Koyol1JrAsNrU6NQTC0zbAAIKCgACPJN5SPosDX7neRlsNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRW2kjBX6xSZeZh4sH7lKeKXX-TU-JAAIQCgACPJN5SB2QHhzGKfgUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRXGkjBX7_aMftPTJotI6s-26Ozhf1AAIRCgACPJN5SPrJBlrV-1d1NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRXWkjBX6i9Ax-OWYkHLQBKgXyKp43AAIXCgACPJN5SF6f7oDx3VJfNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRXmkjBX7fpAYzFOxdijdZPIxyi9KDAAIVCgACPJN5SDN6VXDV66jNNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRX2kjBX6ZYL0w3oDF8alFTHOmxyFGAAIeCgACPJN5SFCc9dwso8NONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRYGkjBX6jH2-cnkAJP-xwXZCa9EdkAAIfCgACPJN5SKzVf1c_WIT8NgQ", "type": "document"},

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])

@dp.message_handler(IsPrivate(),text="📗 4-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRc2kjBilkL9C-NkNLlYRYH5bJxEEMAAI5CgACPJN5SM8deXVH2OKsNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRdGkjBilh3j2aNearPMdQSSlck-T8AAI6CgACPJN5SAxk9YTzg6uMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRdWkjBimnJjj-61PeVbIYDEf4dupyAAI-CgACPJN5SKO8GUs1cAzKNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRdmkjBinjYbtYNMM1RcS4pOsEN17LAAJgBQACbuKASM4x6hVKf1PGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRd2kjBikN0WcKIoVIhGljrddQ6lUYAAJhBQACbuKASD2ZVpVLRE-hNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIReGkjBinVN4N2Pj_UdR-YfWgrdC_PAAJiBQACbuKASGDw23TjNKCINgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIReWkjBinGwgTe_k2nbrD9X2GCaQSyAAJqBQACbuKASI66vLo-9qF-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRemkjBimGrBVJPZ9F6dKn8_8AAYp0EAACbQUAAm7igEgFaGW1CewAAXc2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRe2kjBinptJaFP0OeaHUzQpqzqoXdAAJnBQACbuKASFXB9uFf7JmCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRfGkjBindeT6JV6-WvMX-cHUGDTqOAAJmBQACbuKASPYJgdMOGhrNNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRfWkjBiluhUwQaJr8gxTt8J4POfqJAAJpBQACbuKASHHQB6AQMPIQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRfmkjBimYu5PanwAB1EMfcYR7cnJ70wACawUAAm7igEgsuZYujKCQWTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRf2kjBimGT8aQEDaT345F-1jeSd_3AAJjBQACbuKASMhQpi1HmvWQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRgGkjBinhE-CplD5ewwHz1TfLO4LNAAJlBQACbuKASOA_Qeb7g7dHNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRgWkjBim3orponz1lkUKeWU7XykeAAAJoBQACbuKASDfmqZKmCTGcNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRgmkjBinQj05bMMSLAAFJSd14OHufoQACbgUAAm7igEhkKh8priTSDDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRg2kjBikKcvIR5AoyKt94dn8vkCvMAAJsBQACbuKASNM2wcFZHdJKNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📗 5-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRhWkjBlaDy3V4j7G-1wVsBYk_U-GMAAKdBQACbuKASGlGbkn1E7YXNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRhmkjBlbV-dWLz3G-6iFSpju3_gPxAAKeBQACbuKASJKn8kDMlE-PNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRh2kjBlasmrUC9lthlPqs6XgewSVgAAKcBQACbuKASDndXK1nj57dNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRiGkjBlZp376elvI5KjOKOwG7C7nkAAKfBQACbuKASByRgKd0IN_CNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRiWkjBlarryWsJW_0E-ao_2P-LtFDAAKgBQACbuKASDaQc3zo5h_nNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRimkjBlaN9nPSltA6U-iF6EoTaPvAAAKhBQACbuKASGZtqqWKqu6ONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRi2kjBlYOQaeOGsvU6kahAfgUkqxuAAKiBQACbuKASJ4BHYWkHPFhNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRjGkjBlYYjHvAKJePx7QWyUAtX745AAKjBQACbuKASLC_7dQlbuTvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRjWkjBlYzOxL1OVyfDKn2IOYCtrCLAAKkBQACbuKASNyO_tmah_RzNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRjmkjBlb7WRhoybUJLMZUIMtWDtNQAAKlBQACbuKASBWTy9oQwWe2NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRj2kjBlYVcy0H2NDb0nS3dgE2qNY1AAKmBQACbuKASNWiAcVMoVGdNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRkGkjBlYwWrA0znbqm7whKDLRfZYKAAKoBQACbuKASJR5ifU0oB3vNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRkWkjBlbMRCLAQC9KRyoeEKjuuagWAAKnBQACbuKASLKAUAXSIj3ONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRkmkjBlZ2lwhg6fGeNMU7C5aBiwABSwACqQUAAm7igEiQA3KrLBW98zYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRk2kjBlY8zfkjXlyUiFB01BRsvSBiAAKqBQACbuKASM3uh97KA_kkNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRlGkjBlZSgH84lzMNpdkXbfQfhomEAAKuBQACbuKASL1nL7WHrI3YNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRlWkjBlZSwx9RbqQ3wzD3V04ZNR46AAKxBQACbuKASLZB6UI1HkHxNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRlmkjBlYuadpjJWa7h3Rvpp2ix2k2AAKsBQACbuKASNyK0jyIroi2NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRl2kjBlZUDytOalODsCR1LRwinh_fAAKtBQACbuKASILIBsMPJWjgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRmGkjBlYp6FgIF0QxrauiipZhTFLoAAKvBQACbuKASEA7rxEtFvpkNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRmWkjBlaXjqA8-PntAhRkKixAt9eWAAKwBQACbuKASGSKad3YIT6LNgQ", "type": "document"},

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📗 6-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRm2kjBou65eN2fZ617Hp6sHkJl5REAALZBQACbuKASBo3_lbv6dubNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRnGkjBosUvstUm2nsHZF27gL9Bs6TAALaBQACbuKASBL9BoUbMTYQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRnWkjBovvMCQbHdAwzakvJyyE-ENLAALdBQACbuKASEyQjvWXI_UONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRnmkjBovW5gNk7D1U08a6BPlxSsB1AALhBQACbuKASIaB5jccDIAvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRn2kjBotthWbwydg48Va1e-v5qUvrAALsBQACbuKASHGmm3nNOsKRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRoGkjBouNWH93lu3DYE359hjjYLgIAALuBQACbuKASKLIx9lTjB1INgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRoWkjBovxp2A9LeAw4qnj2ESO1F0aAALyBQACbuKASDPqLQ5b_ZaCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRomkjBovz5uPn2-u29v3j3eJD5RfEAALxBQACbuKASIXvL23VHk1aNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRo2kjBou3N35_NPX3eCO94_mY5c7VAAL4BQACbuKASAe5sjz-JWuINgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRpGkjBoszFTVelOarp-zVVLtUn1w0AAL6BQACbuKASC-ZGjdJOeF_NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRpWkjBosS8DLxSQw8M1THh68TBWd5AAL7BQACbuKASEy4uiQUPt5TNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRpmkjBoumrz2EmKxww_mWMzZA3misAAMGAAJu4oBIVaZfkZTDQlA2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRp2kjBos01aGKeYB3DrSP-2u1XMNgAAIGBgACbuKASKJk6Jb3QBzWNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRqGkjBouWLKoph1sePS6VD6Mide3QAAIHBgACbuKASKgdy6BL7AwaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRqWkjBouLcgTmC9EzlAMAAYWn1G8EhgACCAYAAm7igEj6DrjH5EaOIzYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRqmkjBous2rzyA2Fync3mkQtMc-72AAIKBgACbuKASKuMXh75aAABuzYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRq2kjBosRcRYv2MCucGcSnccwus7qAAIJBgACbuKASPoKfuGroL6wNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRrGkjBouPxvzYfIyNhQyC6zOCmvD6AAILBgACbuKASPCLEIkxbdSBNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRrWkjBov2KpxgdKCWAsZtzh393hYJAAIMBgACbuKASCKlhhvJHxPBNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRrmkjBos_J6ITNI6SbnpIOacj-20GAAINBgACbuKASPVetjLodw-kNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])

@dp.message_handler(IsPrivate(),text="📗 7-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAISTWkjCBg7R6UiDVSafbGCMGV6d1gcAAIlBgACbuKASD8_s1gBd7u9NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISKWkjB8w6uh7_30D5n0BWz5r61QABRQACKgYAAm7igEiLzGF9kryBXzYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAISTmkjCBiLX1J-XgABHsgxTl_JclswdwACJgYAAm7igEgc46OClaemfTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAISO2kjB_KL7omDSDLO56pPRAOF8webAAI6BgACbuKASB1tU5ddIPfnNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISFmkjB6bPYAFhWBOIE-uSCg9XcRsxAAJMBgACbuKASOAM0X7pqWLJNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIShmkjCP9CzBkJtCbyBBlNQk9eIDkFAAJPBgACbuKASM38toN3MLgdNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISZGkjCHbOVthiaV6Y4vHIpnULbhRYAAJeBgACbuKASOyc3O56SNDbNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISemkjCNicPT4YZe1qnXXjFnB2f2a3AAJTBgACbuKASH1mRcjyLZrTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISh2kjCP_Z793HASakv_bXsAOHoNToAAJbBgACbuKASDwGCC3KRm8PNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISamkjCJ0IM03vb6cvIk2HgoMjk07GAAJnBgACbuKASCY4kogL1LEZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISiGkjCP9hSsc2IKh-JaZxvRD8-5RiAAJiBgACbuKASCU2_8-79qLaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISKmkjB8zpcXWbGFDTDYKbOJkUK13vAAJvBgACbuKASDn-Da-qRbFgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIZr2kjJDqhLJKGnOTsfCqB3PWwmjJCAAJxBgACbuKASBaD8Zb8XL7ANgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISmWkjCUVIJXXXF_IyrLG5ouZjRALWAAJuBgACbuKASKquXp4w_82WNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIZsWkjJDq3VB8XKWS7oyu2OQUlmCY1AAJgBgACbuKASMhq7v5vz_8oNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISPGkjB_JaxirTIr4Yu0n4RuZ-e4RBAAKcBgACbuKASFx86ihaAi_BNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISC2kjB4TeWGUKx2Vs-3UWaNcoEcHTAAKdBgACbuKASP6_VGCIo19ZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISpGkjCV1cyQdXjVKaWDktuIZyeOmZAAJoBgACbuKASLGY0e2aYU04NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISa2kjCJ1rHh4gg_mtkew1ZppUSID8AAKeBgACbuKASGAx0ZKszOVKNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISXGkjCE-YBRQZRZ4dnRBJm0-k14DQAAKhBgACbuKASEEbaAjQ06TbNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIZt2kjJDrUct9VyJz_YWS2Maeg5pEbAAKkBgACbuKASOnk_UYGEo4JNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIZuGkjJDq-kTZaeMxvoEuX3Vj-PI6VAAKwBgACbuKASGd2azk0v-QhNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISk2kjCSlJj1DAwsHGVKEvGYGgoOPdAAK7BgACbuKASJPbJzqw6E2dNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIZumkjJDp_iK6B1zGxeV-4ynad0pziAAK8BgACbuKASMMw2UvmHFnWNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📗 8-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRsGkjBsbF9jKyGqZfPOR4PPsMQh9YAAKKBwACbuKASKGCGqRGzAQaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRsWkjBsb3tcroyohS8vYhqfu45g4HAAJuBQACbuKISMms1c7nMxinNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRsmkjBsbF0wmun55damYyPKXUhEIrAAJvBQACbuKISBj_CF6pSVIHNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRs2kjBsbqJdN0xgvdQ-p_i2Mp1x-sAAJwBQACbuKISLTTDfkUKUmRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRtGkjBsYLCizCamDptq6_UrTc2MMfAAJxBQACbuKISPa373Nz3jkINgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRtWkjBsYV9HdHq_4d5NdRtixnnVhtAAJyBQACbuKISC5RoRrqJSooNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRtmkjBsaVb01fTbRFTPxwQ7FC0KYeAAJzBQACbuKISA7JAAF0vkr-tTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRt2kjBsYT-lwOUa9qruyxFoitRvIzAAJ0BQACbuKISP9y5qujkEY7NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRuGkjBsaOBkS8gJWlGEkq3kunkuSGAAJ1BQACbuKISGC1Eyvn3pjXNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRuWkjBsb1ezqavMh4pcFn9mSJPt36AAJ2BQACbuKISGqr3LrnVERlNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRumkjBsYYFHvMEbBtEZ_mD5EgOvY2AAJ3BQACbuKISAbWXi3wDaXqNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRu2kjBsbbMfeDT86Yt4H0KrlGwF-wAAJ4BQACbuKISK6qtOIwnHT-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRvGkjBsZwReyzYaZPDxAUdrx1G8qrAAJ6BQACbuKISDJvDNgSZc3RNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRvWkjBsYAAa6dPHlCR3z4umTAeMTujgACewUAAm7iiEjEtBokcsR_GTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRvmkjBsZy-hl-6Sw8QMk-iWdEv0opAAKFBQACbuKISD6drv6g6E9dNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRv2kjBsYHHMVt_ANn2EqYEriVgLXNAAKGBQACbuKISNj36NMHgjxaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRwGkjBsbBGQsaUrBfiU4NqpwdOU5YAAKJBQACbuKISJFg36MGoBISNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRwWkjBsYchOHldEKSnuBUgLGfIVVUAAJ5BQACbuKISPa4zHe7tgSUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRwmkjBsZsTwKkcgABhteBg0iXN2Hc7gACfgUAAm7iiEibdMuFOxeXQDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRw2kjBsa7rmTHd92EHBy3BdziUR8vAAKMBQACbuKISMx1Sq-X3QuPNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRxGkjBsaeOpjBMjVwROPrAAFmMNOqswACjwUAAm7iiEh7K4sTAc0jKDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRxWkjBsY7qFx6vmw56oiITXZs-gmGAAJEAQACotwSAAGm7Go6NAAB-mo2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRxmkjBsYr_Lv86PvMhTHT6TkTJRXbAAKqBgACzNCZSAVmoTKvFu64NgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📗 9-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRyGkjBuarbMOL6D9CwHhOtKk6QisGAAL5BQACbuKISFGD86PdpgpyNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRyWkjBubS8NX2H_DMW1nghOdu2J1dAAL8BQACbuKISNgUPtZd2FX5NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRymkjBuYVnDx5x9N-9WAqUM0e8zDWAAIGBgACbuKISOAWo28PGU6JNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRy2kjBuZBVYBV63HC2Wh_7xTRfwVIAAIIBgACbuKISDRO08ERAAHmmTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRzGkjBubcGwHWMTzuoSZNksApPwvaAAIJBgACbuKISLkIwrI8qYWuNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRzWkjBuanajLmuMxs6riNRuCLce5dAAIKBgACbuKISKdCO6GsFr4jNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRzmkjBuZPJpLwvVj_vqLe6HKz8-77AAILBgACbuKISN2DFTZQtQ7fNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRz2kjBubSWJRsuM0fo1kG4nNuRg06AAIMBgACbuKISLXO5DjX7xVrNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR0GkjBuZMjGE6VnvyTSyqUdOYqDKzAAINBgACbuKISI_tMcg7TBn9NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR0WkjBuaVL7EcKgk05wFDJcX9dPU3AAIOBgACbuKISHbYQT_4n6UBNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR0mkjBubG5jptrJ9ICDuektgpTUpxAAIPBgACbuKISBRg72d-cPMWNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR02kjBua3ltyB6nEHIvqS4FRAMagcAAIQBgACbuKISKabmEHRHv9SNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR1GkjBuah0bl4knOVHcBCXJEtBOtDAAIRBgACbuKISMfJ2RkxVixDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR1WkjBubRJi3uVmEtGS2Y4-oVKPP3AAISBgACbuKISAgrKCe5FgEKNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR1mkjBuZg-yHAT6IBHRLJuAWgnxtRAAITBgACbuKISKMqI0pqIOpONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR12kjBuYyklKUgBnVonfB5pgSpcHVAAIUBgACbuKISPvU_KxTprHzNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR2GkjBuYpnohIYNvrSPj5XOLuogABywACFQYAAm7iiEj5pwrJQSY_EjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR2WkjBuaAhZmB9q3YfUNyfHDeSARaAAIWBgACbuKISAz_HFm247DBNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR2mkjBuayMCelNZaNDGGGAYubt2JNAAIXBgACbuKISIp_VRfgCQ0mNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR22kjBuZw_7tBzu6LIB3-hSykAkjjAAIYBgACbuKISJE6gDLGucOhNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR3GkjBubZsJ9eJozjQ_uYmFVY0ILNAAIZBgACbuKISGUS1jL7jfk-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR3WkjBuaYMOpoYWuN6HcOshHb2wz5AAIaBgACbuKISL-jXWo8BulsNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📗 10-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIR32kjBwsBOihioC7L1wABjnAW_z-C-wAC5QYAAm7iiEjqmmoLsnm6hTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR4GkjBwvUTYZSl0-XNut_XzbDQ-TCAALnBgACbuKISNLxr9QHsTc4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR4WkjBwsl_Uya6QcsX6zBa-jv4ZfEAALtBgACbuKISG59EPY6PYAtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR4mkjBwvDXDK9VLIHvLYSEZpfvFniAALyBgACbuKISIpogPMsHy73NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR42kjBwvdoTj1RGvV0OsHO8TGj8xJAAL1BgACbuKISBudPw0y_FToNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR5GkjBwsHXuTm582aJR-_xtJAZ99_AAL2BgACbuKISDUZQfmspILHNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR5WkjBwtHEIL_l7iv9MAZOu9iQCfAAAL5BgACbuKISBt_4-8_tj_gNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR5mkjBwu5kd9I_ql-kfqar_dQr3MaAAL4BgACbuKISPL6iz8NZq6GNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR52kjBwskMEX_eFDyAbz-zsUfgcQpAAL3BgACbuKISHHJumDjMSh5NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR6GkjBwvklgRH4PYjrY22FXoG28knAAL6BgACbuKISCEkx5vmVwP7NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR6WkjBwtN3xQQAlGOaevb-POavJj0AAL7BgACbuKISGcWZ7IuggLiNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR6mkjBwtKv9Jqtc57xJSetApXlXkTAAL8BgACbuKISCP9pPVfYuERNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR62kjBwutTbQnsFJeG5ZDlLi7Ntj8AAL9BgACbuKISPGS3bXbThFTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR7GkjBwuyZC1_Tjyk9kvceynq2NJWAAL-BgACbuKISKk6e5osRajBNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR7WkjBwt_Wx0I5kVVI5foH0tT2v0DAAIEBwACbuKISOKRQyLgRzo7NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR7mkjBwvq_-vX0tKZ0AEgWZ_ifyP6AAMHAAJu4ohIjaQaSCVaXNk2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR72kjBwslFao8Sqyi-KCjkRm9QDOnAAL_BgACbuKISFhjauFwrQABjDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR8GkjBwuv2YpSpknawJW8dSPsZN9sAAICBwACbuKISBpc_iwXAnxoNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR8WkjBwsOwnDhb59kg0_UD4C7R_CUAAIDBwACbuKISNu1Iz-nB8ogNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR8mkjBwuUck9wDDa5utzniPNY4LIEAAIBBwACbuKISE6CnLcQd61yNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📗 11-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIR9GkjBzbI1ZdhlTTMjPQSyjJqtXQvAAL7BgACzNCZSC35XGYra53ONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR9WkjBzaFYCGJpiftSPP7adBIclfpAAL8BgACzNCZSLJDZqhpP1nwNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR9mkjBzY_1uzPxnLIrmN1BfFy-WG0AAL_BgACzNCZSAvk4T3gAp2eNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR92kjBzZDyXsQ92iCIViMpYbNuW1rAAIEBwACzNCZSMUAAZOKD_VqkDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR-GkjBzYETgpYrB5mSR8S6PV8NemOAAIFBwACzNCZSM9pjH_bmWwAATYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR-WkjBzboH5rFp83XUVIOi1OMYFbvAAIHBwACzNCZSAPUYr_SefS2NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR-mkjBzaEwWg6UaM2-N7ucv_2d8vSAAIIBwACzNCZSCgYp8pE9YKmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR-2kjBzZykJNJWdgrnIx8IXjxdNJrAAIJBwACzNCZSO19mc6a8YtmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR_GkjBzbuBpToQse4QoqBk1IvIXJ0AAIKBwACzNCZSEXju3pIZEY4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR_WkjBzYF0zPNDeX5arPIuNYTsOgsAAILBwACzNCZSKyj-s-GczNtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR_mkjBzZ-YnWE-dgFqQ6E6__5Zw5HAAIMBwACzNCZSH46xl0LKUftNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR_2kjBzaTIHvbd72jFD-LIXYAAX4SvQACDQcAAszQmUhGBCN4qzCEoDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAISAAFpIwc20lx9GutP89MLYoel-Sg-xwACDgcAAszQmUj57I8FO8f8WzYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAISAWkjBzbgdbanFYmw7XRqvV5YdxI8AAIPBwACzNCZSAq8LZJxOSPNNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISAmkjBzaxFei6cfSDyOgWmC5U_gE0AAIWBwACzNCZSCNOU2eUKG6ENgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISA2kjBzbFh1BgtgoKEC0MSMYXATi-AAK4CAACUxARS6IGoC1aOcfRNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🇺🇿 Ona tili")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRO2kjBTFKhV7Qnk0a7ZspYUI4DktWAAIRCQACPJN5SOhFn1BEduS4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRa2kjBdz9GLjN4vZrsBOfXPyAyXhgAAJwCQACPJN5SFIaUoBcFk_iNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRW2kjBX6xSZeZh4sH7lKeKXX-TU-JAAIQCgACPJN5SB2QHhzGKfgUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRfWkjBiluhUwQaJr8gxTt8J4POfqJAAJpBQACbuKASHHQB6AQMPIQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRk2kjBlY8zfkjXlyUiFB01BRsvSBiAAKqBQACbuKASM3uh97KA_kkNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRqGkjBouWLKoph1sePS6VD6Mide3QAAIHBgACbuKASKgdy6BL7AwaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISC2kjB4TeWGUKx2Vs-3UWaNcoEcHTAAKdBgACbuKASP6_VGCIo19ZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRv2kjBsYHHMVt_ANn2EqYEriVgLXNAAKGBQACbuKISNj36NMHgjxaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR22kjBuZw_7tBzu6LIB3-hSykAkjjAAIYBgACbuKISJE6gDLGucOhNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR8GkjBwuv2YpSpknawJW8dSPsZN9sAAICBwACbuKISBpc_iwXAnxoNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR-GkjBzYETgpYrB5mSR8S6PV8NemOAAIFBwACzNCZSM9pjH_bmWwAATYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAISA2kjBzbFh1BgtgoKEC0MSMYXATi-AAK4CAACUxARS6IGoC1aOcfRNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📚 Adabiyot")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRhWkjBlaDy3V4j7G-1wVsBYk_U-GMAAKdBQACbuKASGlGbkn1E7YXNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRhmkjBlbV-dWLz3G-6iFSpju3_gPxAAKeBQACbuKASJKn8kDMlE-PNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRm2kjBou65eN2fZ617Hp6sHkJl5REAALZBQACbuKASBo3_lbv6dubNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRnGkjBosUvstUm2nsHZF27gL9Bs6TAALaBQACbuKASBL9BoUbMTYQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISFmkjB6bPYAFhWBOIE-uSCg9XcRsxAAJMBgACbuKASOAM0X7pqWLJNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRsGkjBsbF9jKyGqZfPOR4PPsMQh9YAAKKBwACbuKASKGCGqRGzAQaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRy2kjBuZBVYBV63HC2Wh_7xTRfwVIAAIIBgACbuKISDRO08ERAAHmmTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR42kjBwvdoTj1RGvV0OsHO8TGj8xJAAL1BgACbuKISBudPw0y_FToNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR5GkjBwsHXuTm582aJR-_xtJAZ99_AAL2BgACbuKISDUZQfmspILHNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR9GkjBzbI1ZdhlTTMjPQSyjJqtXQvAAL7BgACzNCZSC35XGYra53ONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISHGkjB6aXPzNOitTiLbnHX5Q97Ad3AAIxCAACa5RRS6_Z1rMjvn8INgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🇬🇧 Ingliz tili")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRPmkjBTF0EdC8tFUvKh_Vkbuw4xIRAAKzCAACPJN5SGiD0eVC5nb8NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRY2kjBdxEaHhFRmFLJXJ-jmvGtmBcAAJgCQACPJN5SEXdWN-Ks7gtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRaWkjBdwpJW3vTeO4RqQFAAFGAs0jzwACbQkAAjyTeUgay_g_v4KWCTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRUmkjBX799LMow83FpEtPsKrPhGhdAAL2CQACPJN5SAYFyMS5BVBbNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRU2kjBX5w2jlT4GcoWZH_YyYoW-WvAAL-CQACPJN5SKyAYkknAS1ONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRc2kjBilkL9C-NkNLlYRYH5bJxEEMAAI5CgACPJN5SM8deXVH2OKsNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRdmkjBinjYbtYNMM1RcS4pOsEN17LAAJgBQACbuKASM4x6hVKf1PGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRjGkjBlYYjHvAKJePx7QWyUAtX745AAKjBQACbuKASLC_7dQlbuTvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRjWkjBlYzOxL1OVyfDKn2IOYCtrCLAAKkBQACbuKASNyO_tmah_RzNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRo2kjBou3N35_NPX3eCO94_mY5c7VAAL4BQACbuKASAe5sjz-JWuINgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRpGkjBoszFTVelOarp-zVVLtUn1w0AAL6BQACbuKASC-ZGjdJOeF_NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISKWkjB8w6uh7_30D5n0BWz5r61QABRQACKgYAAm7igEiLzGF9kryBXzYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAISKmkjB8zpcXWbGFDTDYKbOJkUK13vAAJvBgACbuKASDn-Da-qRbFgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRt2kjBsYT-lwOUa9qruyxFoitRvIzAAJ0BQACbuKISP9y5qujkEY7NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRuGkjBsaOBkS8gJWlGEkq3kunkuSGAAJ1BQACbuKISGC1Eyvn3pjXNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRyWkjBubS8NX2H_DMW1nghOdu2J1dAAL8BQACbuKISNgUPtZd2FX5NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR02kjBua3ltyB6nEHIvqS4FRAMagcAAIQBgACbuKISKabmEHRHv9SNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR4GkjBwvUTYZSl0-XNut_XzbDQ-TCAALnBgACbuKISNLxr9QHsTc4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISAWkjBzbgdbanFYmw7XRqvV5YdxI8AAIPBwACzNCZSAq8LZJxOSPNNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🇩🇪 Nemis tili")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRP2kjBTHYjAk0_5YMP5DmIluV5v3aAAIVCQACPJN5SGZzUEr2tgogNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRYmkjBdwSyUsepdkVp2-Ip3NY4hkUAAJSCQACPJN5SCD5J6Fhj2mQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRaGkjBdyDXuyW2Pjg0rgFBojbZqVsAAJqCQACPJN5SNE-1WuETXcZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRWGkjBX5R3oH5xxwAAbteYK5KBAkJswACCQoAAjyTeUgdmuuBnqOeyjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRWWkjBX7wDmlBei-LMw745pk8p3LRAAIHCgACPJN5SAYmK9r24QhSNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRdWkjBimnJjj-61PeVbIYDEf4dupyAAI-CgACPJN5SKO8GUs1cAzKNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRkGkjBlYwWrA0znbqm7whKDLRfZYKAAKoBQACbuKASJR5ifU0oB3vNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRkmkjBlZ2lwhg6fGeNMU7C5aBiwABSwACqQUAAm7igEiQA3KrLBW98zYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRqWkjBouLcgTmC9EzlAMAAYWn1G8EhgACCAYAAm7igEj6DrjH5EaOIzYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAISO2kjB_KL7omDSDLO56pPRAOF8webAAI6BgACbuKASB1tU5ddIPfnNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISPGkjB_JaxirTIr4Yu0n4RuZ-e4RBAAKcBgACbuKASFx86ihaAi_BNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRvWkjBsYAAa6dPHlCR3z4umTAeMTujgACewUAAm7iiEjEtBokcsR_GTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRwmkjBsZsTwKkcgABhteBg0iXN2Hc7gACfgUAAm7iiEibdMuFOxeXQDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR2mkjBuayMCelNZaNDGGGAYubt2JNAAIXBgACbuKISIp_VRfgCQ0mNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR4WkjBwsl_Uya6QcsX6zBa-jv4ZfEAALtBgACbuKISG59EPY6PYAtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISQWkjB_KcD4cgHlkLdSH0DfN3mV6MAAJCBgAC453YSpjD-LMPIThhNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🇫🇷 Fransuz tili")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRQGkjBTH3qc3dDMYytSPNHSmUeZIZAAMJAAI8k3lIvdGtFTF5Wbo2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRbWkjBdzG3FeW-COOmBeJFuwMxr-HAAJ2CQACPJN5SDzEQby9esygNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRcWkjBdy49gT4P6wVExEDv6lc7DNWAAKyAwACYwXgSIbvtgFmVRkLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRTWkjBX7spCg_mzJ3znxJ6A02nVqgAAKxCQACPJN5SBpNXCM2IguwNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRVGkjBX5bBlhZLdTJv45z41kzvreIAALvCQACPJN5SIPZhKKLXIgfNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRdGkjBilh3j2aNearPMdQSSlck-T8AAI6CgACPJN5SAxk9YTzg6uMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRiWkjBlarryWsJW_0E-ao_2P-LtFDAAKgBQACbuKASDaQc3zo5h_nNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRlmkjBlYuadpjJWa7h3Rvpp2ix2k2AAKsBQACbuKASNyK0jyIroi2NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRn2kjBotthWbwydg48Va1e-v5qUvrAALsBQACbuKASHGmm3nNOsKRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRpmkjBoumrz2EmKxww_mWMzZA3misAAMGAAJu4oBIVaZfkZTDQlA2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAISTWkjCBg7R6UiDVSafbGCMGV6d1gcAAIlBgACbuKASD8_s1gBd7u9NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISTmkjCBiLX1J-XgABHsgxTl_JclswdwACJgYAAm7igEgc46OClaemfTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRsmkjBsbF0wmun55damYyPKXUhEIrAAJvBQACbuKISBj_CF6pSVIHNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRs2kjBsbqJdN0xgvdQ-p_i2Mp1x-sAAJwBQACbuKISLTTDfkUKUmRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRyGkjBuarbMOL6D9CwHhOtKk6QisGAAL5BQACbuKISFGD86PdpgpyNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR0GkjBuZMjGE6VnvyTSyqUdOYqDKzAAINBgACbuKISI_tMcg7TBn9NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR32kjBwsBOihioC7L1wABjnAW_z-C-wAC5QYAAm7iiEjqmmoLsnm6hTYE", "type":"document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🇷🇺 Rus tili")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRSWkjBTHIt2kYKdoMFtGl8dmcIASfAAKaAgACWJX5ShrBofN2EPBmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRZWkjBdyT6lUYYEBjJfycD45IjwPgAAJjCQACPJN5SMOGHt5ze89CNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRXWkjBX6i9Ax-OWYkHLQBKgXyKp43AAIXCgACPJN5SF6f7oDx3VJfNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIReWkjBinGwgTe_k2nbrD9X2GCaQSyAAJqBQACbuKASI66vLo-9qF-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRgmkjBinQj05bMMSLAAFJSd14OHufoQACbgUAAm7igEhkKh8priTSDDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRh2kjBlasmrUC9lthlPqs6XgewSVgAAKcBQACbuKASDndXK1nj57dNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRq2kjBosRcRYv2MCucGcSnccwus7qAAIJBgACbuKASPoKfuGroL6wNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISXGkjCE-YBRQZRZ4dnRBJm0-k14DQAAKhBgACbuKASEEbaAjQ06TbNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRymkjBuYVnDx5x9N-9WAqUM0e8zDWAAIGBgACbuKISOAWo28PGU6JNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR4mkjBwvDXDK9VLIHvLYSEZpfvFniAALyBgACbuKISIpogPMsHy73NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR-mkjBzaEwWg6UaM2-N7ucv_2d8vSAAIIBwACzNCZSCgYp8pE9YKmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRxmkjBsYr_Lv86PvMhTHT6TkTJRXbAAKqBgACzNCZSAVmoTKvFu64NgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🗺 Geografiya")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRimkjBlaN9nPSltA6U-iF6EoTaPvAAAKhBQACbuKASGZtqqWKqu6ONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRomkjBovz5uPn2-u29v3j3eJD5RfEAALxBQACbuKASIXvL23VHk1aNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISZGkjCHbOVthiaV6Y4vHIpnULbhRYAAJeBgACbuKASOyc3O56SNDbNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRtWkjBsYV9HdHq_4d5NdRtixnnVhtAAJyBQACbuKISC5RoRrqJSooNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR1WkjBubRJi3uVmEtGS2Y4-oVKPP3AAISBgACbuKISAgrKCe5FgEKNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR6mkjBwtKv9Jqtc57xJSetApXlXkTAAL8BgACbuKISCP9pPVfYuERNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🔍 Tarix")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRqmkjBous2rzyA2Fync3mkQtMc-72AAIKBgACbuKASKuMXh75aAABuzYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAISamkjCJ0IM03vb6cvIk2HgoMjk07GAAJnBgACbuKASCY4kogL1LEZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISa2kjCJ1rHh4gg_mtkew1ZppUSID8AAKeBgACbuKASGAx0ZKszOVKNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRumkjBsYYFHvMEbBtEZ_mD5EgOvY2AAJ3BQACbuKISAbWXi3wDaXqNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRw2kjBsa7rmTHd92EHBy3BdziUR8vAAKMBQACbuKISMx1Sq-X3QuPNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRxWkjBsY7qFx6vmw56oiITXZs-gmGAAJEAQACotwSAAGm7Go6NAAB-mo2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR1mkjBuZg-yHAT6IBHRLJuAWgnxtRAAITBgACbuKISKMqI0pqIOpONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR3GkjBubZsJ9eJozjQ_uYmFVY0ILNAAIZBgACbuKISGUS1jL7jfk-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR6GkjBwvklgRH4PYjrY22FXoG28knAAL6BgACbuKISCEkx5vmVwP7NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR7GkjBwuyZC1_Tjyk9kvceynq2NJWAAL-BgACbuKISKk6e5osRajBNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR7WkjBwt_Wx0I5kVVI5foH0tT2v0DAAIEBwACbuKISOKRQyLgRzo7NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR9WkjBzaFYCGJpiftSPP7adBIclfpAAL8BgACzNCZSLJDZqhpP1nwNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR-WkjBzboH5rFp83XUVIOi1OMYFbvAAIHBwACzNCZSAPUYr_SefS2NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR_2kjBzaTIHvbd72jFD-LIXYAAX4SvQACDQcAAszQmUhGBCN4qzCEoDYE", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🔬 Fizika")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRnWkjBovvMCQbHdAwzakvJyyE-ENLAALdBQACbuKASEyQjvWXI_UONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRnmkjBovW5gNk7D1U08a6BPlxSsB1AALhBQACbuKASIaB5jccDIAvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISemkjCNicPT4YZe1qnXXjFnB2f2a3AAJTBgACbuKASH1mRcjyLZrTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRz2kjBubSWJRsuM0fo1kG4nNuRg06AAIMBgACbuKISLXO5DjX7xVrNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR6WkjBwtN3xQQAlGOaevb-POavJj0AAL7BgACbuKISGcWZ7IuggLiNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISAAFpIwc20lx9GutP89MLYoel-Sg-xwACDgcAAszQmUj57I8FO8f8WzYE", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🔢 Matematika")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRPGkjBTF6TZRHBTSkYKwduzxyFNyTAAIXCQACPJN5SOndZ1fTtmkUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRPWkjBTGiXTK7xrZKDuiGsJnZmR2vAAIWCQACPJN5SFCa_h2JDeifNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRcGkjBdzyZk8eJbrM3tfdoDpFyKrsAAJ_CQACPJN5SNJ-NUwypBBuNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRV2kjBX5vwm0uWxYwGVlKqSyBvizFAAIBCgACPJN5SKnNcxoUE_qtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRf2kjBimGT8aQEDaT345F-1jeSd_3AAJjBQACbuKASMhQpi1HmvWQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRj2kjBlYVcy0H2NDb0nS3dgE2qNY1AAKmBQACbuKASNWiAcVMoVGdNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRpWkjBosS8DLxSQw8M1THh68TBWd5AAL7BQACbuKASEy4uiQUPt5TNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIShmkjCP9CzBkJtCbyBBlNQk9eIDkFAAJPBgACbuKASM38toN3MLgdNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISh2kjCP_Z793HASakv_bXsAOHoNToAAJbBgACbuKASDwGCC3KRm8PNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISiGkjCP9hSsc2IKh-JaZxvRD8-5RiAAJiBgACbuKASCU2_8-79qLaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRsWkjBsb3tcroyohS8vYhqfu45g4HAAJuBQACbuKISMms1c7nMxinNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRtGkjBsYLCizCamDptq6_UrTc2MMfAAJxBQACbuKISPa373Nz3jkINgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRzGkjBubcGwHWMTzuoSZNksApPwvaAAIJBgACbuKISLkIwrI8qYWuNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR0WkjBuaVL7EcKgk05wFDJcX9dPU3AAIOBgACbuKISHbYQT_4n6UBNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR7mkjBwvq_-vX0tKZ0AEgWZ_ifyP6AAMHAAJu4ohIjaQaSCVaXNk2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR8mkjBwuUck9wDDa5utzniPNY4LIEAAIBBwACbuKISE6CnLcQd61yNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR9mkjBzY_1uzPxnLIrmN1BfFy-WG0AAL_BgACzNCZSAvk4T3gAp2eNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🩺 Biologiya")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRiGkjBlZp376elvI5KjOKOwG7C7nkAAKfBQACbuKASByRgKd0IN_CNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRoGkjBouNWH93lu3DYE359hjjYLgIAALuBQACbuKASKLIx9lTjB1INgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISk2kjCSlJj1DAwsHGVKEvGYGgoOPdAAK7BgACbuKASJPbJzqw6E2dNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRvmkjBsZy-hl-6Sw8QMk-iWdEv0opAAKFBQACbuKISD6drv6g6E9dNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRzWkjBuanajLmuMxs6riNRuCLce5dAAIKBgACbuKISKdCO6GsFr4jNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR52kjBwskMEX_eFDyAbz-zsUfgcQpAAL3BgACbuKISHHJumDjMSh5NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR_WkjBzYF0zPNDeX5arPIuNYTsOgsAAILBwACzNCZSKyj-s-GczNtNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🌡 Kimyo")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAISmWkjCUVIJXXXF_IyrLG5ouZjRALWAAJuBgACbuKASKquXp4w_82WNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRwWkjBsYchOHldEKSnuBUgLGfIVVUAAJ5BQACbuKISPa4zHe7tgSUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR12kjBuYyklKUgBnVonfB5pgSpcHVAAIUBgACbuKISPvU_KxTprHzNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR8WkjBwsOwnDhb59kg0_UD4C7R_CUAAIDBwACbuKISNu1Iz-nB8ogNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIR-2kjBzZykJNJWdgrnIx8IXjxdNJrAAIJBwACzNCZSO19mc6a8YtmNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🏃‍♂ Jismoniy tarbiya")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIRR2kjBTEoltn3WgQjDt9MpWXK6Te-AAIHCQACPJN5SBBsMuP9Lsv-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRZGkjBdyA0KST7qlAOWe4kiiQaldSAAJlCQACPJN5SPKJ4wjlls7LNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRUWkjBX4oNlKot_YlSAI5AtGaAAHKvgACyAkAAjyTeUiACjT-fx0gSjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRd2kjBikN0WcKIoVIhGljrddQ6lUYAAJhBQACbuKASD2ZVpVLRE-hNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRjmkjBlb7WRhoybUJLMZUIMtWDtNQAAKlBQACbuKASBWTy9oQwWe2NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISpGkjCV1cyQdXjVKaWDktuIZyeOmZAAJoBgACbuKASLGY0e2aYU04NgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📙 1-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAIROmkjBTHC3YQnacmIMLMKobz-PikfAALCCgACa75gUNMChhRAGIXvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISp2kjCbujChvV6Xj7uF9tfIURrGPSAAIgCQACPJN5SO3-YTuXCEqANgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISqGkjCbsXLxjSNRZTaliIR7DdzszIAAItCQACPJN5SGI1r7_Q1yHTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISqWkjCbutIWMXgmDIgqGH4XQoRaIGAAImCQACPJN5SKNblagVtRzdNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISq2kjCbtRzGsfMRi4pG2pPZMvwnvFAAIlCQACPJN5SPxChlyqQq03NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISrGkjCbsPC9wBYZlIvWSbW68rBrq6AAL0CQACl8dhSKt8Th8wuzsWNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISrWkjCbvgkgOq5thE8XKUjt23yP3MAAI4CQACPJN5SDM2WIWULP-hNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISrmkjCbtRNWYNlsre4fec5wKPshr1AAIjCQACPJN5SM0V2qcJb9K3NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISr2kjCbtPXv6qE1N979xAK0SY4DuoAAIcCQACPJN5SFo9XlJNwfDUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISsGkjCbvomrwZU7fYH2vDdlVJgsR_AAIdCQACPJN5SGfQzAvgmKMUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISsWkjCbvSi1JBnuYcaUIizw6MkSoVAAIfCQACPJN5SFQHc3NqmbnqNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISsmkjCbta0uTN2u-952OiEnmUBlTYAAIwCQACPJN5SNFwHXF4Xty-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISs2kjCbuY7qjZMzh3b2mkhlYNL5AjAAIrCQACPJN5SNElC8-Jx5HCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIStGkjCbv02mzrrt1xVRuX77LVmtCNAAI0CQACPJN5SLtl246YQDgLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIStWkjCbujoV9ZIQpeSfoYFGFFIleiAAIiCQACPJN5SOTO0YKFuQwrNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📙 2-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAISt2kjCdssag4vAxPOminWZRQx5F_AAAKgCQACPJN5SM2byzGg0O-9NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISuGkjCdsJFMQfq1v_IuiSJ3iUYHW8AAKhCQACPJN5SEp1SFRK536tNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISuWkjCdvcPWYlTcm7LypO6790YahVAAKiCQACPJN5SH2ELoo8hvSMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISumkjCdsLss5XeU_L7qAb-ZTdd4YVAAJeCQACPJN5SMmmRIpaDfFVNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISu2kjCdtHGdW9H6WGwpu6wreV8mUPAAKECQACPJN5SN7UNa-3HFOiNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISvGkjCduQhW3fk7MDTJj1jptXkIKuAAKKCQACPJN5SP4KvJUz0mTPNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISvWkjCdtxVDfQ7Nx3nGKz5NfQYp7XAAKRCQACPJN5SL4RQNdiJjvDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISvmkjCdvinv6WHUioX-eVGGHi5T2UAAKWCQACPJN5SHg_m4SvZi5ZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISv2kjCds3H1shtRVQAAF91nncrNyMtwACjgkAAjyTeUgcOm3mUtkuGTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAISwGkjCdvnVNOXvd8S1Cxoo8OIgdRhAAKbCQACPJN5SM-a5GSxVUmGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISwWkjCdvEv5fqBa3TWo9dKYTnKmUIAAKcCQACPJN5SEtdip42EhphNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISwmkjCds0tti7RQ0Bag6JM5bFu30cAAKdCQACPJN5SAixD93Z2hPPNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISw2kjCdumI9NE2RzGuoXhewABzE6KBgACnwkAAjyTeUgo9FAeYp2p4zYE", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📙 3-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAISxWkjCf-vMdvWr9gW9Zububnj6lLnAAIwCgACPJN5SAcWbqjkYpfzNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISxmkjCf8YZeTdsbwy6fUs9QOeiFmnAAIyCgACPJN5SByGZTlIqrbxNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISx2kjCf-Oh2tQP4xuDadERWhaKi-BAAI0CgACPJN5SGo78bR8Vz0RNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRVWkjBX4W1A_54z_fFNwQ0B4U-X9oAAI1CgACPJN5SBd6EUzIyjsRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISyWkjCf8kxT6zuu0hoUK0dmD7uEmFAAI2CgACPJN5SBhJook_9wfYNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISymkjCf_PGP_0q941Nei1bR96yLipAAI4CgACPJN5SBTl-bRZspzbNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIRW2kjBX6xSZeZh4sH7lKeKXX-TU-JAAIQCgACPJN5SB2QHhzGKfgUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISzGkjCf-KnInLWl39GxNfU-kIqXsPAAIpCgACPJN5SBydlwJXtY3HNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISzWkjCf_-6q8njGN-1xGF7HveqT3jAAIrCgACPJN5SPuNd9NeeJvpNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISzmkjCf-_P3ifv2ClGVqhEBvG5uQxAAIqCgACPJN5SGdC-K8r3J8eNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAISz2kjCf9B6C_Cl7mJ6P5BZacYOZ2MAAIsCgACPJN5SJ5PjftyP_QgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS0GkjCf-XCxqbzWOgNC8-EYXy2PAHAAItCgACPJN5SCQ1nXjjgCDqNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS0WkjCf8sW0iD-ZdGoJHc48Ed6VhTAAIuCgACPJN5SNwOnnG8JbR8NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS0mkjCf-RFqQK5_uYSpU3eZYgdh4OAAIvCgACPJN5SCMdGiKheBVJNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📙 4-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIS1GkjCiWK3qF_Xokkb2HgkzpVqYMvAAJ5BQACbuKASPt7NO4EGF9jNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS1WkjCiW9QbtcsRMq95Nf2jrbUdsIAAJ7BQACbuKASOmQpRpnzgABOjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS1mkjCiU9-_AW0ERFjq2fRXWHu0byAAJ6BQACbuKASC8Clz9OK5KmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS12kjCiXw1s3N3rTtDuvtmwAB3SjeOAACdwUAAm7igEhpcR69NYdf3zYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS2GkjCiXtrUbNrRNmJH1ele_7ND5aAAJ9BQACbuKASAk5_5j7RcBzNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS2WkjCiW-U6MlWYmPpmvINTvVTV67AAJ-BQACbuKASM62MnDwKUiFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS2mkjCiV2JUGwabn6dyxzDkX72n7uAAJ_BQACbuKASDJvUifeXZ6oNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS22kjCiUwcdMaIcVAUtEbbvUGFJY4AAKABQACbuKASLHpgphZBsxZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS3GkjCiXWQj_d_1EHnblLlqOAqBgcAAKBBQACbuKASCWQRcUTLU3CNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS3WkjCiVDUoe_3EYhtAG5jpu0BUfMAAKCBQACbuKASC9S14TbxRdANgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS3mkjCiVUPhWyqkK9qsvZgyYvzB7gAAKDBQACbuKASJZzDLAKSl7dNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS32kjCiW3v1VL0XbOUpjynNZM-OXZAAKHBQACbuKASGNhDgTjPBQlNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS4GkjCiUWCqGSxJ2YK5xv1ZaMnQ74AAKEBQACbuKASF8gBpGaqX3TNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS4WkjCiVFKD83YZ9Rxm92Qt6H_8guAAKGBQACbuKASBhh7BKxqHzZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS4mkjCiUrnoHfCKRTIEBQn-xOMWgtAAKIBQACbuKASJ1QQDX3KHXxNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📙 5-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIS5GkjCkWaECx1C6cIb0SLAAEzs8kK4gACswUAAm7igEiPuDIVwAz3qjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS5WkjCkXPFjLPBRAT6W5iuSfynjOjAAK0BQACbuKASGRehN5S6jzVNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS5mkjCkW8wcmuNXDeBqNhv0fTdjHkAAKyBQACbuKASK01SaiLzkN3NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS52kjCkX5PGIZ8pCwJS8GHMKZXmpvAAK1BQACbuKASKhC4P2ZQwYoNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS6GkjCkUzMz-n22FLn45n7QslGzhKAAK2BQACbuKASAsM08Xz7L7fNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS6WkjCkUzZzTHOHG0ntmu9d-Af1l4AAK4BQACbuKASF4w4S6NN6HqNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS6mkjCkVnl_RgHH7BfeYPQbEUIow9AAK3BQACbuKASLtfsgS8AmihNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS62kjCkUSNmEzLXT262yvJ2WDO3QfAAK5BQACbuKASF_FyYHtVLeENgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS7GkjCkV182bxRSQP8fLMomZGx1FJAAK6BQACbuKASMTKJpFfuMkXNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS7WkjCkWnJUmC0aGuLA8zpIAR5g0pAAK7BQACbuKASJj_-hc9TercNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS7mkjCkW9wSgCervE0QQXeqLmFf9rAAK8BQACbuKASNBCvRaLXl9kNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS72kjCkV3YgvxY44LsUNbzyaeXhdGAAK9BQACbuKASEBTTarwMlkkNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📙 6-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIYwGkjIdn2q8QWc2Hn_uZbsn_yUfSNAAIOBgACbuKASMMeQAABoPlbLzYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYwWkjIdkiv6rPqXUYUOlhrOJVtl8uAAIPBgACbuKASJX9dHi5_6noNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYwmkjIdknlMFpXp6IH8R2OJkjikTkAAIQBgACbuKASAdeBjjjqrtGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYw2kjIdkOfbQEFs4x6-PCFgpTKLO6AAISBgACbuKASLDl3NVAhqFzNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYxGkjIdnlGC5A-peQZN38diR6qs5DAAITBgACbuKASAF6kNFdXLlPNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYxWkjIdnegsc5vBf1ZvtQD3elV2X6AAIRBgACbuKASFnizP4suPnaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYxmkjIdlu09fsrbV_JLtna3B0XXvPAAIUBgACbuKASLO-DmnfNYvjNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYx2kjIdlzQn1Joe7LCWYdsAcPQxpXAAIVBgACbuKASFc1uE1gjvoxNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYyGkjIdlOOF7FG9uES971U7btH6U1AAIWBgACbuKASPJ5OI5Hx5ZGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYyWkjIdmPqCxfPUUwK5Tchy1uGeW7AAIXBgACbuKASHlAn6AybROONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYymkjIdmGAAEM5gW4tsX3Kdh9A5WHKgACGQYAAm7igEgDDO2KKV-_tTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYy2kjIdknLYv-4eOOmyAWVyZMUSkjAAIaBgACbuKASGJP9y4WeAO6NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYzGkjIdkvY60TA6iehvAt3bJGgmH6AAIcBgACbuKASO9xFJvB3dZhNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYzWkjIdlMzrczlS5QNGSCe9LhOucdAAIbBgACbuKASBwjE3vPVqDcNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYzmkjIdknc5VIGcYsJtePXpLJ9GkIAAIdBgACbuKASNNkr7Y6w5oBNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIYz2kjIdlpezjTWOe1sDsy2TTOCwgHAAIeBgACbuKASO-OD80LBD1yNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIY0GkjIdmXhmcen6dn1OKQV3DmuFLsAAIgBgACbuKASIoow_nJYrilNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIY0WkjIdlabasdxVpIwFSXpDmUaOewAAIfBgACbuKASGfG9D3n4nLyNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])

@dp.message_handler(IsPrivate(),text="📙 7-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIS8WkjCmWuJBu-fMhNA2W-PDP2YOvqAALVBgACbuKASIaPPdpFGGiXNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS8mkjCmU__HF5lqHSBJAMz-W2SJ_gAAK-BgACbuKASMO867Mb-WIcNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS82kjCmVgpX9VstOBFoKUbfHyQq2uAALABgACbuKASF0RGN2M2ZNfNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS9GkjCmULZ4KG1ag7a44514vYtU1rAALBBgACbuKASFMvZd07cgYgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS9WkjCmX4RahKdk4albxOCxP7FnK9AALCBgACbuKASOzFo369hDLRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS9mkjCmXJEEqvYskPJEItr6ZPjiweAALDBgACbuKASHyzxK389Um2NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS92kjCmWwozFHdE6w5N4zfs2XuGpRAALEBgACbuKASPayci3xonJkNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS-GkjCmU8xITGDuy4VjnybdgyImioAALGBgACbuKASOq58xJbSXnRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS-WkjCmWyMTrAe1JqHe91HERRA7TEAALFBgACbuKASIYLwnSLoMtdNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS-mkjCmW89F0MHD2KMEcr6TsCeK7CAALHBgACbuKASFXH0WaAWVFfNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS-2kjCmV6erRoA164bD3z3B2K3YaSAALIBgACbuKASJMbuoBrNiuCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS_GkjCmXZsGzibEPm1BDWEIphKYIFAALSBgACbuKASH-EKr-s2pnGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS_WkjCmWkNY-vye7AGBXiaOe29Z_zAALQBgACbuKASCxpu6NhelRONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS_mkjCmVrxNtXIL_F1cWvz_rCViRSAALJBgACbuKASGK4B3UY-TkFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIS_2kjCmU6msL1t11IZvr9S1rhaFfdAALPBgACbuKASM1WO1d-v5MZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITAAFpIwplHhCUwOPiIGLBGY4qOdw1lwAC0wYAAm7igEhchGqbD8oocTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAITAWkjCmXxSvlvGJSgDTqnx_VpEnRbAALRBgACbuKASJnL1L1mTVMcNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITAmkjCmXRlac0Ik2xUDUb6wtBip3iAALUBgACbuKASC3Op30HkMLoNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])



@dp.message_handler(IsPrivate(),text="📙 8-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITBGkjCzzGAgYBrYdnp42l0iUJbZkgAAKsBQACbuKISO9AO0edTKLwNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITBWkjCzz3a-j_3CoH4z3aEXue4IanAAKkBQACbuKISAURwc2UeP9xNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITBmkjCzypxI2xEXiJfKlch8Nl3vTmAALSBQACbuKISLMMwrkBYSy2NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITB2kjCzxVKXnkG7EYUsSNbs9Ft5X4AALcBQACbuKISHuDAnw-ILu4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITCGkjCzwd_n6wuNx9n2zrSqpYFO1QAALVBQACbuKISFZHnXspu92mNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITCWkjCzwXXoCaLo7w0JFogjA_NWsvAALWBQACbuKISKhUCwErnsKtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITCmkjCzzoa0d-rbz7k9Zc4fp_mzx3AALTBQACbuKISLYI-aBQFFFANgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITC2kjCzxnLrlCOkuhGXNK13BgnL2qAALdBQACbuKISJ1fBPmOBc6rNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITDGkjCzyUIb9N7BOcP-He3OD25M0NAALXBQACbuKISF9yBM6M4vDCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITDWkjCzz0FmscGVIwM2Pu8lNDuDnVAALYBQACbuKISLmJ__3skRRINgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITDmkjCzxf87DxVRUigtf-6DKkhyWAAALZBQACbuKISA6v1ku4EYZNNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITD2kjCzwtIQN8AYjdZt8ZJKVhdLQWAALaBQACbuKISPgvn483y50_NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITEGkjCzzCoQQeivtC8YARhrrbx5XlAALbBQACbuKISHvrY5yybPpvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITEWkjCzwvRgFpAAGKernjyx21Kze8mgAC3gUAAm7iiEjO6mP8VgrxITYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAITEmkjCzw7XoGn9A8uAW3YmS821neQAALfBQACbuKISKhsZtGkCaJtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITE2kjCzw1z7izE9GEwBaipCnlY1CvAALgBQACbuKISFqBvjheZTzQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITFGkjCzxfl_Qx096XBTILjLvrhpPXAALiBQACbuKISBqUSDPsWWddNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITFWkjCzwWTYtATw24WavxswVU7o3HAALjBQACbuKISBpbRu7CCZCgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITFmkjCzy9twhXWVG9q0rtOVXyQDg5AALhBQACbuKISCtK9_f4J6ugNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])

@dp.message_handler(IsPrivate(),text="📙 9-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITGGkjC3BgksnkQjDtL66GszbcAAEpTwACGwYAAm7iiEgnQLHy-lIcxDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAITGWkjC3BybI6hHai4XbbcH4ZTO3fEAAIcBgACbuKISMTGDUWbFE-RNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITGmkjC3DJ3ePcdrlTIrdcNo_dkWvaAAIdBgACbuKISCIx6CDXQBjeNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITG2kjC3Dq8CdChfisVbRNMMc9NVOcAAIfBgACbuKISBtuxFM6pZjMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITHGkjC3C8JTI86gLUO5iVv4Mnjw17AAImBgACbuKISF3wRhFrzxDwNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITHWkjC3D34aL9DVCagJKF7ycUts8AAycGAAJu4ohIrDZZll519KQ2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITHmkjC3ATCL2fOx-Xwl4uk97KnxHtAAIoBgACbuKISJDlwOYkyna3NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITH2kjC3BedGza_q0kvjlyVGtpRxbzAAIpBgACbuKISMYIfxbGPWLUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITIGkjC3AzdpGjLQyKxPfsypnv6v9zAAIqBgACbuKISNjezKpX0ry5NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITIWkjC3Bv1HHi6W4KBiGJEwYh7I1DAAIrBgACbuKISD7DuUkYe8QDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITImkjC3AgNBoJQnScQ6_cotbQS162AAIsBgACbuKISOHt0_clIcxsNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITI2kjC3BhTp8fj_v5cxCkcbaTX31FAAIeBgACbuKISH6YXOJJT3qCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITJGkjC3DKv4jM4CjgZu6srJNNH3f4AAIhBgACbuKISN_U3vDrSn5RNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITJWkjC3DmDOL7FcioS7_yTZrVRi80AAIgBgACbuKISK3TDEIneqUAATYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAITJmkjC3BeIaQXNgXacgaX6M-1rte7AAIiBgACbuKISNwJyUBsLzjuNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITJ2kjC3C0VU-kncPDSLSkXMVY_SJHAAIjBgACbuKISJPUFW-NZpeaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITKGkjC3DFTgWEspsPzdz45TAixIEZAAIkBgACbuKISM0P-jHpTJyGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITKWkjC3DnQ68SLHgDCdjJOMG2nZCmAAIlBgACbuKISLonBZnSPfjINgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📙 10-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITK2kjC6Ty3GQ_2Dn10hKCtA4LGn1KAAIGBwACbuKISIUtiM-qVONmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITLGkjC6Sen8zzYlEPy31yRNwlrrYUAAIUBwACbuKISIWas-1JUrihNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITLWkjC6TepLBeDLH-oTviBBAql9K_AAIHBwACbuKISBrxXu1tZaWSNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITLmkjC6QsLxSEmLdfMLM6FmB33sc4AAIMBwACbuKISHVIb8XWnZ00NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITL2kjC6QnkRI-PlPhPnbo-0Dvj5c-AAINBwACbuKISI_p7M6JIzuTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITMGkjC6QC1rKHCot7lwnWMC81yjpIAAIJBwACbuKISMMU1OxR81TINgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITMWkjC6QBtpy7iSE3Nvz2QjZ_DjGjAAIOBwACbuKISCbxKSOi8LmwNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITMmkjC6Qj6lEIUgGnKBkEM0iHA8qyAAIKBwACbuKISOoqcH7V2lgCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITM2kjC6TUa2vVCBisaEUcegZDpO7PAAIPBwACbuKISLNSjzuk5wUmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITNGkjC6RBv6jqFnwvLA5X-kNCDqvnAAILBwACbuKISMOmyy5uzDWUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITNWkjC6Qnt_XAEo9Z3ERiHZUalCjkAAIQBwACbuKISI3yFXd4g0WyNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITNmkjC6QrYgmwcZyHFbN1j7Oc2qzQAAIRBwACbuKISGmKXUL3k5rpNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITN2kjC6QtQgKXMAZSap1ka0mcUcxtAAISBwACbuKISEpgPzT1dLsINgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITOGkjC6RPwdHjrjrsFuY8VHTF_QgGAAIVBwACbuKISExPV1qhsAjDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITOWkjC6QJDNEsyDIZFmHouRnB_tsNAAIXBwACbuKISAJ8B1av-MZFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITOmkjC6Rrvzx22WzpERgriFQUvTYiAAIYBwACbuKISOzD2wLN5pSENgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITO2kjC6SdxGwDjV6RK7ZMRW0ZQkzfAAIIBwACbuKISBCUNQcpLl2YNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITPGkjC6Sy_F6wy7c-GCUUX3gM45aCAAIZBwACbuKISGBCWdQwu-a5NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITPWkjC6T0wk7VWp_W8STHvU2WdAcQAAIWBwACbuKISNmBgT5ZlfKGNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📙 11-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITP2kjC8hse77nqxenfH_pGLbJ0xoTAAKlBAACziPBSE2iXQRfzjDYNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITQGkjC8gQ0B8L4qY7l6CgcXiOmqAqAAKnBAACziPBSEG2MNLF79zcNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITQWkjC8i9iJdxfl4ivhLRjZSNS70gAAKoBAACziPBSJx8laf9b70NNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITQmkjC8g_zY5ybComLzlUY4fhQc1aAAKpBAACziPBSIEi94OrpTQzNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITQ2kjC8ifpvZWKqDOUlf4RGAnJPhOAAL-BAACGsLJSKiUWRhiubjXNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITRGkjC8jTnvDoVi-CrxYHvPl9quIOAAL_BAACGsLJSF_5ZP_4El2uNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITRWkjC8jOpRsoylhQsp_18Nyjg7izAALEBQACziPJSBB4ya59cTPQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITRmkjC8iekBAAASt0kC-AHBS8-VmYGQACwwUAAvGgwEhsc1KruwxhnjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAITR2kjC8gUx9hEAsoPcyTrCWEB3aldAALNBQACziPJSDbZLQcAASTg2DYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAITSGkjC8jekA_6VagRrMg1D03Xa45RAAIJBQACGsLJSJObPEP78fRsNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITSWkjC8gSjZPbFULIz8MfftQvWkcbAALPBQACziPJSOMH-FcXDTiwNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITSmkjC8iJca7EXnHSptybA5EhExDbAALRBQACziPJSAYNGkqhPs36NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITS2kjC8hCO7XLSiTKCK2Q-4WKxn98AALTBQACziPJSA3d8ggopQ9sNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITTGkjC8j4vRSMmTBCHu7nyYmeDluwAALUBQACziPJSAnlqpc43Q26NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITTWkjC8iXBG0SBJC7ksoXHejiIytsAALVBQAC8aDASLqO3LB5QKdbNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Tafsiri Hilol")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgUAAxkBAAITT2kjDwhPmP_iZg464Pt2P5vlXpGSAAJHAQAC60eAVB2_3Qj8rdLZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITUGkjDwiznYDCjgHYGx5wSIIcW8YJAALQAwACtAogS5WOqXIRLZzmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITUWkjDwgmUaJ8N8Wxy-iqi7lj4U6UAAK1AANNvlhJJya_Es5CwGI2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITUmkjDwgwrRGU6GOWw0UC28bTJtiUAALRAwACtAogS5yWGys7Sf8pNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITU2kjDwjr4SPzIOW8rssQg7GPdGawAALTAwACtAogS4bv5gnq-YEZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITVGkjDwhbnpW9w_oz5FI2GyXcEFpyAAJeBAACCpAhS3B_o0pJIzfBNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITVWkjDwhALWxyZVn1VhsI0NF8I5SFAALUAwACtAogSxZ6iz3LiD0QNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Jannat vasfi")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITV2kjDyHbXhrJ_viGMcZL1NaZzXvBAALJBAACTWYwSAOHtI1_jnuTNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])





@dp.message_handler(IsPrivate(),text="Keng rizq va baraka omillari")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITWWkjDzoOa9Dfn8JEFPPX1cOytVrwAAJnAwACqAfwSFxhVz6rWX6cNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Istig'forning 40 xosiyati | Salovotlar")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAITW2kjD1qGgNaMcIs-MopdHOU5PrYPAAJyCQACdtd5UHz2RzAnYJr0NgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Qur'on - qalblar shifosi")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITXWkjD36bLaMdR4WW49JKw2nchLUJAAJZAQACWs0pSKpt1HobVTTpNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Baxtli hayot sari")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITX2kjD5QiSqe8w-p7q1yV_MrkB_rzAAJIAgACpPxQSClXGoZpErkENgQ", "type": "document"},

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Payg'ambar uyida bir kun")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITYWkjD8U5t4u0AamGhzTfMSiCKUg8AALRBgAC5Jm4SB_V_7conKtYNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Shamoili Muhammadiy")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITY2kjD9_bVxi8FSfWJbvQNgjCPTYiAAK6AgACgQ9hS_U1T-d7LErmNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Abu Bakr Siddiq")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITZWkjEDF--HJ72Picz7E2R8d3lTqkAAKRBgACpQAB8Uj8GsM4o0dmEzYE", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Sunani Termiziy")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITZ2kjEEng0K7pafk7jszsXGKQLbTwAAJeBgACYg4AAUjeXcOKb9JuAjYE", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Hazrati Umar ibn Xattob")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITaWkjEGTFoj2R_56JHPsGReVU86bNAAJxAgAC-wfgSTfN63xNAalyNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Musnad")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAITa2kjEJCtX9P0eyfji2CibwjoEXW6AALzDQACeE0kCCLyjFsYXmDyNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Mukoshafat-ul qulub")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgEAAxkBAAITbWkjEMSWC9XbjL9PdZlGrtydYfZyAAKJAAPB7KlHRJK9QKTiK642BA", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Ramazon va taqvo")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITb2kjEQebWrDrYchcOrSKcWE4aV8bAALUBAAC0bwhScZ0DXIa7uPmNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🗂 Pdf lug'atlar")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgEAAxkBAAITcWkjEVYKbeAqzH84RUr3_dwSkKqzAAJ3AQAC9DKIR4tIxpWoeMouNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITcmkjEVb9j5bWyexePS-J58bLpkISAAI7AgACmbmJS-ibWe9TdYzdNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITc2kjEVZME1xKnKWtDwTdbqOD3FMtAAJEAwACoJSJS-pbh8W8xnFiNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITdGkjEVY2o9g7mWb1YemK7a-T10hOAAI9AgACmbmJSyO8Dx6-Q7INNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITdWkjEVYLd_b_BtslkoFsRV_pFZAFAAI-AgACmbmJSyEpPwoj8-DFNgQ", "type": "document"},
        {"id": "BQACAgEAAxkBAAITdmkjEVarB7WpORI7P234la4eR4PgAAKmAAPwF4hHnhOYFmVwur42BA", "type": "document"},
        {"id": "BQACAgEAAxkBAAITd2kjEVZZ_wIZaExPJisF8QoQBziIAAJzAAOyUhFEzYQZ3vW6_aQ2BA", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📲 Apk lug'atlar")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgEAAxkBAAITeWkjEXVDnQpdKogZij9oidmsF-gJAAIeAQACJ1apR90gCBzwtLx1NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITemkjEXUrxyozwGkgGDij-kx8KwMpAAI6AgACmbmJS_VEnQWEfJrLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITe2kjEXWr6dsEgFLQQQxqZ4givQFAAAI4AgACmbmJS5Wa-H7WIEXiNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITfGkjEXUmyt-NobBKZ2In6_lW7wGaAAI8AgACmbmJS_ZuX2Ss4gPTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITfWkjEXXkWtQB9Zi17kPVSvXG5WvgAAI_AgACmbmJS3grGM_98A3uNgQ", "type": "document"},
        {"id": "BQACAgEAAxkBAAITfmkjEXX9m50Geb84YcNLNoIAAZ6MPQACdQEAAvQyiEc6yrunFsdAqjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAITf2kjEXVk_mijAAEPb5js0bYruMNKJQACQgIAApm5iUt7Tf0n2cFTTDYE", "type": "document"},
        {"id": "BQACAgEAAxkBAAITgGkjEXVijp7QdZa-9_NZMLJiIC4lAAJwAAOyUhFEQz80Up7JtfQ2BA", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🌐 Google tarjimon")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgEAAxkBAAITgmkjEZYEW05wjmY_Xm5-qFy-qrFjAAJ7AQAC9DKIR7_HgKewaPu6NgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Erkin Vohidov")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIThGkjEhpVseBrSy_JQNCCJsiCW69dAAJ7BwACajZhSk4CscVHtxsAATYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIThWkjEholMjrdGZq30gsiVJiVCwl6AAIRAwACyKPhSsGbhUzRyV-fNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIThmkjEhpwakAg9TU24sn63rb_qJMlAAISAwACyKPhSsWmNP4dNUQGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITh2kjEhqZua_WLqoywtEAAWmnH86CAwACEwMAAsij4Uq3tPV_QZWbDTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAITiGkjEhrQV9AIM1YPCrFi2QFq8o0YAAJoBQACM8B5SSMWnJY_BsnmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITiWkjEhpkCfzYSbTfWwWdLO32ZxfLAALCAgAC8q4AAUvJ-Cc5t2QgVDYE", "type": "document"},
        {"id": "BQACAgQAAxkBAAITimkjEhqN1wxvh2k2YFPXYl32d8jfAALmAQACeNpxULnaj6RO8HijNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITi2kjEhqigMmL9tRLhQ6owa_pLelnAALnAQACeNpxUNY82X6AoeYRNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITjGkjEhr_CIJHwwnucJeDxatRRkEYAALoAQACeNpxUBO9Nep681gqNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITjWkjEhoiktKt26iZ3SnLj1QejH9uAALpAQACeNpxUH32Ht_GCrnJNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITjmkjEhovhTJucLvtkujOaoZvjm10AALuAQACeNpxUDzh5MO5R598NgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITj2kjEhp8ku9TO1EQTxElkoLU09fMAAL6AAN0FohQy_uGOz5SfEA2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAITkGkjEhpXkRAyoGMKEUWef2Ip4t4uAAL5AAN0FohQ2ke7h68pFoM2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAITkWkjEhq8JW5cc6qDsk5271uk0qTpAAIEAAN0FpBQaCC77_eRkCM2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAITkmkjEhprYJ5nGrAm15RhMc_QnSimAALwAQACeNpxUCgT3VBr78oMNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITk2kjEhqd5OA3s2K7hD5BBRhMci1jAALvAQACeNpxUDbx6Ze-_oaLNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Abdulla Oripov")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITlWkjEjeMPdvi6_qwxekEPe2iw7U2AAKmAQACGMtRSU-3gd8CE0ayNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITlmkjEjePQRNyG1oeqbZIQGHvHBO6AALeAAPQ0UFJmxw-n_XJmjY2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITl2kjEjcRsOFZ-06Ml1v93JINzIytAAK0BQACN-IBSaCiODtxB_0zNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITmGkjEjeyoWJ1WcuD69W-cg7umsolAAICAwAC9JE4SFk0nz4c68BcNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITmWkjEjf8wlL61C-74qZZfvLAtfKDAALAAgACKcN4SpOG7R5JXKU_NgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Rauf Parfi")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgEAAxkBAAITm2kjElL8Fpu1W2lAXsLCOsk_bc0cAAJAAwACbHaZR_ncvkG87MM4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITnGkjElJXW_zXq7Mvg1NBkE4-B0TGAAJcAAPhgrBLmiT9DCefKDc2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITnWkjElKDRe8EaAL0rfjpXbv0xgVKAALkAAPLzywN9HVnFmn2fYw2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAITnmkjElKM5torU3oYKPs3XeD5OAPXAALcAgACeNpxUKZUnW2lLT93NgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITn2kjElLF4s6gbYqaJdn8vQGDzYiLAALeAgACeNpxULEQ3Rjk-08pNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIToGkjElIB86r5Uk09eMoUTj_UrP5KAALdAgACeNpxUM_aqxyH1qswNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Shavkat Rahmon")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAITomkjEnerfihId8mJ8DHy_S8sX7-iAAJXBAACgQlBSs99pAF1_64uNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="👤 Muhammad Yusuf")
async def qaytish(message: types.Message):
    fayllar = [

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📗 4-sinf")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgEAAxkBAAITpGkjEpYslbqIr_CSV-1lyEgxmFZVAAKiAANFEGhF4LD7Ohxcq-82BA", "type": "document"},
        {"id": "BQACAgEAAxkBAAITpWkjEpbOwz2NBWgKy33VWYnJRz6cAAKhAANFEGhFFmnbhz-YGzY2BA", "type": "document"},
        {"id": "BQACAgEAAxkBAAITpmkjEpbk7BNiBJCtPy3oA0lgkQhyAAKNAAPVRmhF-qLPYpib5N02BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITp2kjEpYWZOwgHkRDGF56_aUgEYL-AAIwCAAC5ymoS0tso27ShWqGNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITqGkjEpbFuJoWFV9PCWT5ULPP6XNzAAKXAgACeNpxUFTmLV2O3yZFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITqWkjEpb4kHU9PWYuadSowcYkPnn_AAIVAwACgb4QSsUWWvYrw3d6NgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITqmkjEpY9FoFAISiyns4QuOyQ2FCSAAKWAgACeNpxUK2ArnBjMCjWNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITq2kjEpb7S84KTqsmr6BTyqiRYYv6AAKeAgACeNpxUMKB5vFEgIA0NgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITrGkjEpYIBBxc8xNeudxxhSMvGPTsAAKVAgACeNpxUGI0CWERPnslNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITrWkjEpbhvI68oV7Ua52XocP5swHOAALhAAPQ0UFJpc9SpkYQW4I2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAITrmkjEpbaLs85ThXQrPmDyUecu5SWAAKZAgACeNpxULjYoCyskJ0rNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITr2kjEpbMch3gqZc51CBEmq0_fiJbAAKcAgACeNpxUH7eHNZXp2tONgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITsGkjEpbHz4zy_alOS6LZXilXHZvCAAKdAgACeNpxUIGnFrMDUOZ5NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITsWkjEpYPGqk62EJrvwPztL5Nn-iyAAJDAwACYKQwS9_vsVedVf82NgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📜 Alisher Navoiy asarlari")
async def alisher(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAITs2kjErhGjZ1Ni-TJfIT5omCCEtqzAAJ_AQACeNpxUPuZColzOqHTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITtGkjErg-M7O9RhK6XeweHc8DVPHfAAJXBQACeOg5SZQDLHF8W5-9NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITtWkjErjiDokDsyfZsY_54J-vYeP0AALxAgACdzwgS_5FD4IHi21RNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITtmkjErhSBexzZW3-krtAAAEF0AR_mgACPQMAAjTXKUpzgxjEfEqVvzYE", "type": "document"},
        {"id": "BQACAgQAAxkBAAITt2kjErizxU33BJjUjBmgKke06QpJAAKMAQACeNpxUGJXyHa_GhJMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITuGkjErhf3Pl2X3cHV4hXlibqpihjAAIMAQACPQjwSwZLl8032JCdNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITuWkjEriG70_zaD3UBTJFI-j-YTiFAAKGAQACeNpxUPLl-hmFac1eNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAITumkjErifY3A1cpLMN4aPK1sjGZqtAAKKAQACeNpxUIQKtO5_-BT3NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITu2kjErgqY2Eb6ETtOO7p3JbbFIi1AAIKAANfM6oO2_nISoN1MLQ2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITvGkjErhFPCgSE4S0Oca9d1cihy2aAAIcAANfM6oOA8SNFnM6E3I2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITvWkjErhWIH0SnHF6pQN3s-KqK-bsAAILAANfM6oOZQ7t4QrzKxU2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITvmkjErgdvvrxWh2XR8QxwK4MMJKeAAIMAANfM6oOvhA81AnR7ZI2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITv2kjErhtWAQ6ZrJSsFVuuSPH5rZ2AAINAANfM6oOVnYteKwsgwY2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITwGkjErgNKHQZQE9JlmEqYSwnxOyoAAIOAANfM6oOEGpioJ4P1xs2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITwWkjErhhhl-Eiw9bUWwzoMQErGZoAAIPAANfM6oOjUcVLLXO8ws2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITwmkjEriotVqbuAkUMtmqT5SmVYZDAAIQAANfM6oORsx67fQ1iV42BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITw2kjErgJkbfvp_AT6mVfrK5Zs3NOAAIRAANfM6oOg5cdMxyt5Dw2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITxGkjEriuj_bmnKQ00xJURBIHPckPAAISAANfM6oOd2YXzytEUDU2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITxWkjErgz1Xbvmnx5-FDwyrGmh6sDAAITAANfM6oOpVYg76EjinM2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITxmkjErh0AqxM6pM5JUzrIcDjtREnAAIUAANfM6oOWcXuTEXs34U2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITx2kjErg7JInzcwOinOKzdFbY41OYAAIVAANfM6oOGXsxcrME6mU2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITyGkjErhgJxU7l5WPHMQQaBL_nuadAAIWAANfM6oOc0nnL4uckxw2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITyWkjErjVIabCQF8otMTGjVlaiVG_AAIXAANfM6oOJ6tbgfRSK282BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITymkjErhh01HQFd0JgCq-7iglMHxKAAIYAANfM6oONgJm57fUfC42BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITy2kjErgq6HBOLM-Xxef5UFHejTMoAAIZAANfM6oOGbPjiSFtbJg2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITzGkjErgAAdd2aEOZ2UGySQxcn2sXIAACGgADXzOqDnI47OSbqnTpNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAITzWkjErhz4VXy-NfH0o4dZ1MlJljzAAIeAANfM6oOr1qrXOTnPJg2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAITzmkjEriVvxch-AsxbMH6De-kVGNZAAIbAANfM6oOYLylRLO71SQ2BA", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📜O'zbekiston Milliy Ensiklopediyasi")
async def ens(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIT0GkjExHNhBWc4S4yvmak79hMja8OAAL9AgAClBwxS5bTyzVhKA9uNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT0WkjExFh7C4RCVFBW-_EbBeS-RcMAAIwAwAC7IEpS-u9qnh2frF-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT0mkjExFv6JRU041RHjLLm8YMauhYAAIxAwAC7IEpS5jLXnDK97dkNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT02kjExED1WPeqzIdBXY0X2E9lajaAAIzAwAC7IEpSwGUHhTaFiEdNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT1GkjExEHYpu1Z1PmvmmkN0ZoNbtrAAI0AwAC7IEpS3Xdrj5In_ELNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT1WkjExGHqja8OrZxIEAOG3N8tTYIAAI1AwAC7IEpS8mWnHX3170SNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT1mkjExE_fR1YZdTK5l7moIOLSUyqAALBAgAC7IExS-rGVNMXIQvtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT12kjExGJj-AGb2IIwXQ8M3JGQn-BAALCAgAC7IExS9IIPeFRYFQHNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT2GkjExEgQ0fXGFez6-TVetpNJhVfAALDAgAC7IExS_IB6zkoq6h_NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT2WkjExGOFtnp1Eo-Fwz_GhqdAAEB9gACxAIAAuyBMUtzfY7t5Nk3EzYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT2mkjExEDUtfDeBw4QKy3LzkZtx6UAALFAgAC7IExS9h2XX65OnVqNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT22kjExG4fEVteRDnGkRlaHFJkh07AALGAgAC7IExSySCc2GiknUJNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT3GkjExFui-LEzUV2al4xtiZSLyy9AALHAgAC7IExS5ZW0x-P9LVLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT3WkjExEeEYKUbtG2OrfjNpXpTqhOAALIAgAC7IExS_39Sb9OsHQZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT3mkjExE74JOYnthHRElYVXn3g-vBAALJAgAC7IExS1wXHtNVlxdNNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT32kjExFfKQ8Swa9Sc4ShXV2BVhWiAALKAgAC7IExS5YvrSX0xIajNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT4GkjExEg5EhJ0tQauFul4luawywLAALLAgAC7IExSzFkvF8NN7T7NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT4WkjExFhRbxAkkX54L0aFQ4qKYSGAALMAgAC7IExS3Fcj-MTCM7ONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT4mkjExE4ftLa7wMCnm2fYvLRiCAKAALNAgAC7IExS41T57Eoi65GNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT42kjExEfNhGW3UAXWapBpsqIz0IKAALOAgAC7IExS-R8KgrptJybNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT5GkjExEfjbgRlHETFFLRdjtPYywgAALPAgAC7IExS75DsoCO8xqhNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT5WkjExGAvsoQ16m6dfg6ktDxwLn0AALSAgAC7IExSxoxN5-C5twVNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT5mkjExFGEtWhzaRZa73kXehodzSWAALTAgAC7IExS4v1FSnw-3fDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT52kjExHdps59fPHfdBaoAlYYKdUxAALUAgAC7IExS0vSDIQNvjd3NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT6GkjExHQH9WlRxa6p7G9hU-uXAH-AALVAgAC7IExSz0SsMmEW4HgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT6WkjExFnd8CXbgEHl1-BK2hLYoqmAALWAgAC7IExS9RBGZFo_gVMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT6mkjExG4xQOCO38xQMNMLXA-agN1AALXAgAC7IExS9j1z2dBz0J1NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT62kjExFoXAXF2Y_2EFzPzdZ3qvblAALYAgAC7IExS05AVFPF_L--NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT7GkjExEVZu53jEACoa79QiSUDl5-AALaAgAC7IExS8pssXF43GweNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT7WkjExFO2-D98a1zyDdLhiSqt1BkAALbAgAC7IExS_MPEbvzvfWWNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT7mkjExG2huZOs2KbCp5iCZsiniSoAALcAgAC7IExS50mEvBWzSdlNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT72kjExGeKcuRtZ700giq3AI3SiwiAALdAgAC7IExS01u7QABydJMWzYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT8GkjExEjQ03TOj7rVT5OspPhICSYAALeAgAC7IExS7VWylK8jIxLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT8WkjExFfGuGSCaqV16zpA1qWRw-xAALfAgAC7IExSz6KuZ0ggKW2NgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="🔍 O'zbek tilining imlo lug'ati")
async def imlo(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIT82kjEzU1vZubcOas0d_-8zMW1mQMAAKpBgACgX9JS1yvFcKK6tuBNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT9GkjEzUy-zQ-GpBWuycqI7uIXnXDAALyBQACqS6wSgqXpXAqOqw_NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT9WkjEzUKb5_cUm0hmcaznWNbu21nAAJTAQACmg4QSMRA_GLnUp09NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT9mkjEzXhgq9A-B-jvVTlrBG0FZdrAAJCBAAC5o_xSj6wwZ4-zvJoNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📋 O'zbek tilining izohli lug'atlari")
async def izoh(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIT-GkjE4NhYU3Dv5B3DduF23Ng69xSAAKnAANfM6oOxgAB4U3cU5qxNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT-WkjE4P6TU6nz4VIg-u-XtwQuAuNAAKoAANfM6oOViQJa1NBgUM2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT-mkjE4P1NeE0yBQWPjjM0pHFCQLaAAKqAANfM6oOBBvmOVYtPCY2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT-2kjE4MHrZfabBk5fVyoNhxpekDqAAKrAANfM6oOZLkj4e5zw9k2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT_GkjE4Ob3vwN_w6qwgXEFpAYobhnAAKsAANfM6oO1_9qq76kqKI2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT_WkjE4OaqU2wuE5X8NXucTfOFiK3AAKtAANfM6oObz2LmaAlc4g2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT_mkjE4MhSTi05r3gieb0ulNnV1MSAAKuAANfM6oO1B0gIxdrmTU2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIT_2kjE4Mu1LSene6Hq-z31CcvudADAAKvAANfM6oOboVAqZW2rSY2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUAAFpIxODpnPMhyOdLcPQAfjBdxx8kgACsAADXzOqDmPxObjvZPr4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUAWkjE4NB5KeEzyce88Cj2ztFG2BRAAKxAANfM6oOZoznx5mPRtM2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUAmkjE4OJCSOgSTPPwkI0a2svWOGCAAKyAANfM6oOKH5GAbEkv3U2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUA2kjE4PlRtf9IGmXlbcqgTObhNMoAAKzAANfM6oOqlE3gOvpYtw2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUBGkjE4OC-WUtMTseU1V__RiWmEOrAAK0AANfM6oO-nPogLwSX9s2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUBWkjE4MiVxq6QGBO0GQXfr7m1SgbAAK1AANfM6oO-Rm5jjkNzLU2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUBmkjE4MVYdqGELSSfws2DDOLjqSyAAK2AANfM6oOxa540595qB02BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUB2kjE4MM2_16oxVOIrRoT57Kc5ZIAAK3AANfM6oOceFGDRnrHxo2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUCGkjE4OvnLZ1Hliaqtks0DhWIjwtAAK4AANfM6oOgPwsWhk1jB42BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUCWkjE4NiGZ89BGHNHYNee0thBdH_AAK5AANfM6oOeNqcUA-vOFQ2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUCmkjE4NQEHqkvxQiweW7pIuxpnbxAAK6AANfM6oOT2PVGT9j40w2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUC2kjE4Oe8zCWtvwd05VhOt6ECmMOAAK7AANfM6oOkVHroKRw4eo2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUDGkjE4MFA_MKvyIU2uRSDOt2NbW5AAK8AANfM6oOcwzeXpnkcvY2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUDWkjE4Neqaug40_LSvMsCyvVZPaVAAK-AANfM6oONGSRSkvW8Ns2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUDmkjE4PW-lLIseoZvxHWdcu9o4YLAAK_AANfM6oOpszjl_aIU8s2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUD2kjE4ONHrQlMIsXlnzqV8ZTdz2pAALAAANfM6oO7bpT3ZupqPk2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUEGkjE4NpGVo4aOWEUENliP0TKl8rAALBAANfM6oOiy5EIQYpOoI2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUEWkjE4NCSLqRwFl-jQKmK8-wW-X1AALCAANfM6oOoh2T0Kt4T5g2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUEmkjE4NLWgABw0aw6XXwml464aJeUAACwwADXzOqDuE5g8tASL32NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUE2kjE4Mek6sBx50s4Ey-M5dg6sfSAALEAANfM6oOrhmPGG4G4N82BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUFGkjE4Pvp3pZJ8dRCYJF39itOdXtAALFAANfM6oOBLRUuywCGqE2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUFWkjE4N35Py7MEzrpujYOi-YBX_rAALGAANfM6oO6U0njfWmGXM2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUFmkjE4N6xaGDhlCXy5KSgppBFFhrAALHAANfM6oOSi-o6AmKNjk2BA", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Islom Karimov asarlari")
async def asaaar(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAIUGGkjE7C4mD1QWZpMvCBz60rDUNH4AAIEAAN42nFQz2QTAU_IoXM2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUGWkjE7DX2Rjqysc3vSrQfdRgfOWRAAIFAAN42nFQOF_9NAbtOBA2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUGmkjE7ClBaZInBu3qCIyHWLPmgEXAAIGAAN42nFQGNjVzCCnQf02BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUG2kjE7DhG1ztiPehzGj8TYgp7LgPAAIHAAN42nFQsDb0mrgDHoI2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUHGkjE7BEPtp7LQULC64-9t9qxWyAAAIIAAN42nFQebuePkrDYts2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUHWkjE7BNirpLhj9wCmntc0eZ60n-AAIJAAN42nFQGoB7BcD4liA2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUHmkjE7D91FtB0pUuVOwfzl30xtenAAIKAAN42nFQavrHOb1lQw02BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUH2kjE7Dqk7BFPlE0LSCdUidubH0fAAILAAN42nFQCSI6MxqUp9g2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUIGkjE7BzJw_rytN6p2MNTPdemmT4AAIMAAN42nFQvPahXdmzISE2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUIWkjE7Dd4C8Hrukg8UCLK6G9C9irAAINAAN42nFQvylNbE_DKlw2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUImkjE7CfQ62lAztyFA6pazkMV5tFAAIOAAN42nFQURcuIqqQvaI2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUI2kjE7B1QrloSlpJJlhWNGhSvmG8AAIPAAN42nFQOPkUswvRy5A2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUJGkjE7DVVy4Bt0C7sPKFMXZFXJu6AAIQAAN42nFQxbSgZLLqOFQ2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUJWkjE7B-qf5C85MS_lEcWgHXlt7RAAIRAAN42nFQCsHvdH7pOoU2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUJmkjE7CBbmpZwsdppRqCOHGVkKMYAAISAAN42nFQabXSB1OBYMg2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUJ2kjE7BCYvjs8hG4Z9XnjuwJTI6ZAAITAAN42nFQ0klrihywUX82BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUKGkjE7DviR3AHEZ7MY7nLfvcyr_6AAIUAAN42nFQ1lJiKi5JihM2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUKWkjE7CLFs-2W2KcCcmDGuW1-NaMAAIVAAN42nFQGxI1Ta-qZ7s2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUKmkjE7A7YfpD71G4PNqhUjb5Td7sAAIWAAN42nFQ5GkNYp6E0302BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUK2kjE7BrZRgduVJ9_5-D411__RXHAAIXAAN42nFQvsOJpvDEs002BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIULGkjE7AnYkd8OeFpdIIc0QABupx8lQACGAADeNpxUDVe5dFk6paPNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIULWkjE7AR08mP2hfsWi0VntMuJjAvAAIZAAN42nFQMadmsPTBZZw2BA", "type": "document"},
        {"id": "BQACAgQAAxkBAAIULmkjE7BrUS51UOneFz_F2O0wTEMPAAIaAAN42nFQzzNE4m1sOQY2BA", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="Shavkat Mirziyoyev asarlari")
async def asaar(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIUMGkjE9Hv6mJRCYFwQ-cOjE35VphUAAJEAAMN0-hIoRIosS_Kt7k2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUMWkjE9ELdGewT2XnSZZnsnPExaTmAAICAAMN0_BIlKMNaGMpYW82BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUMmkjE9EmTRAd5JQ0XOhCpLlfShmIAAJHAAMN0-hIYvZR2Wi6m7k2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUM2kjE9HdW-EzLCx_iy5DDVVCyxsiAAJGAAMN0-hIkqFc6XCoJDY2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUNGkjE9G11CIrpUY1xLkCJRpRb0d3AAICAAPKcXFKfEvCZf3Y88k2BA", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📒 Pdf kitoblar uchun")
async def pdf(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIUNmkjE_pZMURVPJcslOUo08qRq7o8AAKkAAPMOSsEI_bP859Yh6M2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUN2kjE_o6arcENRQS1rXqRtyEyj03AAKlAAPMOSsEJoExkhOppa42BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUOGkjE_oW7RecTeMaDt3mAAHJQL5p_QACpgADzDkrBLHCPfeWHFeBNgQ", "type": "document"},
        {"id": "BQACAgUAAxkBAAIUOWkjE_opILFDmzj_SbvH0S9-KeNtAAIBAAPJ7PhVIvGIAoeEDJM2BA", "type": "document"},
        {"id": "BQACAgUAAxkBAAIUOmkjE_qAAAGClHqOm3ArXWPBupHwXwACAgADyez4VXcTClXDK_3INgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUO2kjE_qVuk2mpRzVl_pKMYadh3dKAAI1AAOmT9BImE_Uk0UTE6Y2BA", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📒 Djvu kitoblar uchun")
async def djvu(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIUNmkjE_pZMURVPJcslOUo08qRq7o8AAKkAAPMOSsEI_bP859Yh6M2BA", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📒 Epub kitoblar uchun")
async def epub(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIUP2kjFEHe5BxQ5_41hCu8lXVWF8LGAAIVAAPUZLhJiGA9PNf5y3w2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIUQGkjFEGNtNbrztJ2fjfIz6etg_p4AAIaAAPUZLhJFTEai_kDMe02BA", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="📒 Zip kitoblar uchun")
async def zip_kitoblar(message: types.Message):
    fayllar = [
        {"id": "BQACAgQAAxkBAAIUQmkjFGPTK1T4FG4N1Gr4O9Id3YbXAAJMCQACdtd5UA68Z7h87PTVNgQ", "type": "document"},
        {"id": "BQACAgQAAxkBAAIUQ2kjFGM7RU3NzUU0P40b3xHyQf-IAAJNCQACdtd5UPZlLyv3GpXbNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])



@dp.message_handler(IsPrivate(),text="🔄️ Yangi nashr")
async def nashr(message: types.Message):
    text="Yangilangan o'zbekcha darsliklar\nTanlang👇"
    await message.answer(text,reply_markup=yangi_nashr)


@dp.message_handler(IsPrivate(),text="1-sinf 📗")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIqRmktKlEK3JqOwJJHR2lehaIlkNf7AAIdjAACbh9pSeMCjLkMJQw2NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqR2ktKlG30OYHhn-NDOItj8ugpEAVAAIejAACbh9pSZpQv9bIph9oNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqSGktKlHvfjgzxxHZJDj0VNDqogkiAAIfjAACbh9pSWhXogmsJfO-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqSWktKlGsjwxdVyCg944xeS7XHfHUAAIgjAACbh9pSR_dmYd0VEG2NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqSmktKlFpdoASh3FD7du11d96MqYvAAIhjAACbh9pSTIrGNOd5Sr7NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqS2ktKlF2Fq5_uxEyFkkuUnc16jKJAAIijAACbh9pSXFiR2vU-7noNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqTGktKlEK2B-WqK0n0YGZCxudW3ODAAIkjAACbh9pSQHYN_g5YEDZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqTWktKlEt_MVn3ReIeyiTfdLHFaXWAAIjjAACbh9pSecplKFmpqVLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqTmktKlF7Z6I0J8wnRkofJGph9QpOAAIljAACbh9pSfeUMHgjsLP6NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqT2ktKlGh4KHdVZ88UC_L-rwg1eFQAAImjAACbh9pSfuYwkSiBTedNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqUWktKlU3wDrzjYB060d2D_HtPFp5AAInjAACbh9pSW_8c6bYQ9bMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqUmktKlX9YGXHmrV4RpzE1kRaYiCqAAIojAACbh9pSVOw7tPxZeAMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqU2ktKlXmFeIDnes2ynBmKAwtn143AAIpjAACbh9pSTJdSmCAa6gDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqVGktKlXIJVyeW-3Mg-rDTCYJyPvZAAIqjAACbh9pSYMgfHyh9JkCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqVWktKlVSWyMgd975DXSVSTL80jTKAAIrjAACbh9pSdR1rU97F98ONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqVmktKlWdMKC_S3t_Ib6I3kAfzUIZAAIsjAACbh9pSZiBHPEizCiHNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqV2ktKlVgxPZdn7VGjmIxQAABNg8-8QACLYwAAm4faUmYZT2_tm_CmjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqWGktKlXD8w6EL02RKGRlnSSVDyHrAAIujAACbh9pSfYxOrLO1UFlNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqWWktKlXHBXEt5CtJyjL3whaflL1kAAIwjAACbh9pSQQLne4eSJleNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqWmktKlUhmIQH3B7cMUgAASBKUYr33AACMYwAAm4faUn7poY85kIxjTYE", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"],caption="""❗️1-sinfdan 11-sinfgacha bo‘lgan darsliklarning eng yangi elektron variantini bizning botdan yuklab oling. 

✅BOT MANZILI: 

👉 @E_KitobXazinasi_Bot
👉 @E_KitobXazinasi_Bot""")
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="2-sinf 📗")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIqeGktnkNWWhSHpI1zMwVbVpJOmS_lAAKQlAACbh9pSaF-Y9tzVBW3NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqeWktnkPAHAAB-rF1nSYVDRflY0Li8QACk5QAAm4faUlk2MQYW-mn3zYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqemktnkNef5HWDsWkr0QdXOYrlnTWAAKVlAACbh9pSfzyYznOchIlNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqe2ktnkPyf5i4Etc3W4lud1P4HlCxAAKWlAACbh9pSe47qBV2g-vpNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqfGktnkPhja4Yburu8VtL4YnaHZ_RAAKXlAACbh9pSdmRzJdGRdxDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqfWktnkN8CCyYX0_7mYjvDTWtDuDpAAKYlAACbh9pSQmJjcJTyfpyNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqfmktnkPakmM09yqqeI99yAAB-cQtcgACmZQAAm4faUmWRd5KfXfiBTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqf2ktnkNsepty7eU0PXdEDWsBR7b7AAKalAACbh9pSbQG2YXR8S7KNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqgGktnkM-z0mMTLF4D8cnZ1utXkNrAAKblAACbh9pSYxX8G9iuuguNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqgWktnkPFkq35bUXPVaKAua4D73T0AAKclAACbh9pSXVETx0mHB2MNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqg2ktnkmi1Jbv3reH4FO2GYx76APLAAKdlAACbh9pSb1UNd7kYZkINgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqhGktnkk7-NvmxL29_heUbkS5uvsGAAKelAACbh9pSeAFL_xUNjzONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqhWktnknDCiT0iSwnpTx0utuFLOpIAAKflAACbh9pSd7r1osYCcXyNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqhmktnknsUuSKMC2VIf6sU04pwPW8AAKglAACbh9pSekP0cJST30KNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqh2ktnkktUL-_3ymVwCkgnOoR-LCdAAKhlAACbh9pSQ4LzrckXhN4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqiGktnkn2883k1E3nN160Toc_RJKrAAKilAACbh9pSYospdsPH8TvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqiWktnkkojY44BiBLewMFgO0IEtc7AAKjlAACbh9pSdf0Id3MtSp1NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqimktnkn4GcBlAAHG5eEzTjrfUky3-AACpJQAAm4faUk0kSimjBOEyDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqi2ktnknD5ETrVHBBzDSgHYV1bFaQAAKllAACbh9pScwRcBgjSKKpNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqjGktnkmJJvdTMdqj8a2iq9-MFDZlAAKmlAACbh9pSVFvRcrLnPu6NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqjmktnks4mWgB9kKwUmzr0YAfBIRTAAKnlAACbh9pSUVuCCED5gZaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqj2ktnktlVUhB39RyZh9P1-zO0RKAAAKolAACbh9pSeDiF2XLWAZaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqkGktnkv9yAF6lI_1b4qs-r1dKbSWAAKplAACbh9pSTaFd_S_IdB8NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqkWktnkvC2Z_rprh8ziUS50I6-Pf4AAKqlAACbh9pScVu662bzTEUNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"],caption="""❗️1-sinfdan 11-sinfgacha bo‘lgan darsliklarning eng yangi elektron variantini bizning botdan yuklab oling. 

✅BOT MANZILI: 

👉 @E_KitobXazinasi_Bot
👉 @E_KitobXazinasi_Bot""")
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="3-sinf 📗")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIqk2ktnydKnIZ31vMKpNW4JjvHriwhAALOaQACQ9uISuHsmolUH5JcNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqlGktnydx0xHHwQWbfCSwuWFexsLMAALPaQACQ9uISg8MpjyEiZULNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqlWktnyddvJN8VdgvsbbK3n9IXo4SAALQaQACQ9uISlAYMlyQP7RgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqlmktnycF1w92EtUeLEDZKu5LGdnXAALWaQACQ9uISgk5XdoeEiweNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIql2ktnyem3VsOgLPKJ_fwrHVjTglRAALEaQACQ9uISttvvgfmVAdKNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqmGktnydu6zEUGRd1YEkILr_bUcT8AALNaQACQ9uIStmXotybpmTpNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqmWktnycwLY5GKrml9RAkHB6CtsVgAALRaQACQ9uISh2f2x-Uu1VsNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqmmktnyeMAeiwvnqF2cuJesrUQKioAALSaQACQ9uISvXCiml6EIseNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqm2ktnyckHhuFYBbe_AVzDfmQH80SAALGaQACQ9uISkOQEswR9vy8NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqnGktnycDPvfHy2y7X2mbfnDJcq3iAALIaQACQ9uISlph6GsYN91tNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqnWktnyexjYKev3xHN5fyHk5BPeDuAALMaQACQ9uISmHNCdABc7d3NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqnmktnycMY0VS0SRVTafj6Zlsy7YZAALHaQACQ9uIStmn__BwX1b0NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqn2ktnydMGe-VbTY_iXKRg9_jDHBPAALXaQACQ9uISgLsFAvfSWkONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqoGktnydUXCFEMBJN2cNDuM29hT9nAALUaQACQ9uISu7Je-SgO68RNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqoWktnyfiGPfVjRb0qUN5Jnay7uywAALJaQACQ9uISgrT6I58B8IENgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqomktnyd9drz2yL4cao_N8Co3zYfyAALbaQACQ9uISgak6h3lnLrvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqo2ktnye1036GjuZ8Rxvf67P49AOmAALYaQACQ9uISojBK6f8lT0fNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqpGktnyf1xVcRGNZ5DpH9LMa6h5BQAALTaQACQ9uISpdGdZERZ4NFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqpWktnyc-fkCmb4sdrUqjSfmwwXeiAAIbagACQ9uISt8pFoYrEItgNgQ", "type": "document"},
    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"],caption="""❗️1-sinfdan 11-sinfgacha bo‘lgan darsliklarning eng yangi elektron variantini bizning botdan yuklab oling. 

✅BOT MANZILI: 

👉 @E_KitobXazinasi_Bot
👉 @E_KitobXazinasi_Bot""")
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="4-sinf 📗")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIqu2ktn8_YBM4nLx-9Ad5lbQpxEhjzAALMagACQ9uISpCn7subkhyUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqvGktn8_sJ2PHtexZAAHcYNFdQXix2AACzmoAAkPbiErK1zjdWkq56DYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqvWktn89vCjtMlFJx9tjnRj6L9i0JAALPagACQ9uISsqdg1PZocZENgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqvmktn8_x7XD7Cixg6bfv6pBPKgq2AALQagACQ9uISihxwhVvfULxNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqv2ktn89brvwSlrUGe-z63947cddEAAK3agACQ9uISpi2hGGU7zITNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqwGktn894u9rxWcqVJqvdVa686k-CAAK6agACQ9uISoCRrQWewzQAATYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqwWktn88Ms2K6NF44OiBqEnTWhmInAAK7agACQ9uISs5--SzxQxXfNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqwmktn8-YIf5nYSDAxtvY9czPJwEpAALAagACQ9uISvVUQqnH4MHFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqw2ktn88sJyBv8_hV7LeW3WInpdG8AAKwagACQ9uIStBRtJ1oFmqlNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqxGktn8_xYAgDkmeK64kFGZoe2vCaAAKxagACQ9uISmiGutHVCBQ5NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqxWktn88pCzUa_VnWf99agea6HMaBAAKvagACQ9uISsIr9J_MWCeTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqxmktn8-ZqlnQ-dR4xJhchus2yDgWAAK1agACQ9uISlmjRL2R4fLFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqx2ktn8-p-50dw46EAAFyCbrbwabFOQACvWoAAkPbiEriv-KkJevyLzYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqyGktn8-7mEZa1IuhkWRh7lH-QzjIAALGagACQ9uISjjo5j6QFiDoNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqyWktn8_Ppa2dEQRa9M1Y5aBYhwFDAAK5agACQ9uISncdtrh9x5FONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqymktn8_8TzY2fYwji21q3zivHWvOAALDagACQ9uISlUG2QFuy530NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqy2ktn89scKfOoq_dvhRS3Z4jmqUJAALRagACQ9uISvrHKLKdAAHotDYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqzGktn8_5QhqKAg6DQgc_ExxQoYF6AAKzagACQ9uISp3eyEtJ0HWNNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqzWktn8_62gb91KOLZEbJh5-Bfn0cAALBagACQ9uISobLyo5xAv4RNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqzmktn8_xNy9INFJfqLRr5Z3Ib2BmAALJagACQ9uISthf9JctVb6vNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIqz2ktn8-Sbi35Li-UTBmCnVuFxtoxAALFagACQ9uISgS22HvhJajRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq0Gktn88bbspG5xFxvN9HPmzs-_4xAALKagACQ9uISksgjjfejyskNgQ", "type": "document"},

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"],caption="""❗️1-sinfdan 11-sinfgacha bo‘lgan darsliklarning eng yangi elektron variantini bizning botdan yuklab oling. 

✅BOT MANZILI: 

👉 @E_KitobXazinasi_Bot
👉 @E_KitobXazinasi_Bot""")
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="5-sinf 📗")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIq1GktoFc6ZJcCS4isjZ5UaLpTelz0AALRawACQ9uISu_7p2MufY7INgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq1WktoFf831KYbisf6pl0f4dkRfFcAALSawACQ9uISkuGJ1EBW0fZNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq1mktoFe0bIrVDGFkTtXClLQ_uPwpAALMawACQ9uISozdDXJCwZHCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq12ktoFcz5Xbem4haBf0KWWadjZ5AAAK0awACQ9uISu-Z3Ww1CJwSNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq2GktoFeDqozABmr560zZb8iuAnUsAAK4awACQ9uIStV5jmCwRNB0NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq2WktoFfs-SydismRZuh7L2NvXA9yAAK3awACQ9uISqtk7NNs210VNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq2mktoFdjwP3s3jNDrBOb1dkg-XfkAALGawACQ9uISuHpJbUlAlpcNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq22ktoFd6y_jUFnkGX5l7BORDtJHrAALKawACQ9uISuAxF5kBWK6ENgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq3GktoFdzVq5JjAnWdJcAARDvOkxKGgACxGsAAkPbiEobLS5KVjR71zYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq3WktoFdFKFhXMDIm6fMIZkLB2MKBAALBawACQ9uIStSDyx2VWQ9UNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq3mktoFdtpJvCU5MiowmYpB8X5R5rAALDawACQ9uISk52_A6dmJ7oNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq32ktoFfEq-vNujJ2S9mH2DEonUcvAAKrawACQ9uIShJOl6cbrddzNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq4GktoFcGK3GJkQiQpJ04UBPDpkA4AAKzawACQ9uISluFiHYNKaeANgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq4WktoFf30BOJ5w-BRWuLBUB851UnAAKxawACQ9uISjNiPg3bjj12NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq4mktoFdaSqnSoY8QkrBmEJtLmXkQAAKvawACQ9uISsJy_uZFmSuCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq42ktoFfLDcVyQ8vNNiO9V-35g9EgAAKyawACQ9uISr2FaiglOjRPNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq5GktoFcRERPPJTXE4N6JMfWGGrMQAALZawACQ9uIStgfJi4gkCJmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq5WktoFd7lTgIe3oBQGgMLc0KiuDsAALWawACQ9uISg0YM_RD9VOjNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq5mktoFft2igIW-3oVeB1hn4q1O-7AAK7awACQ9uIShLZ2nI-tKGyNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq52ktoFdjD6rCh7n1T20_29p4z_7IAALCawACQ9uISojd-t2kVXVlNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq6GktoFc5Y-jUP0eO5oYBmOZNCoN-AAK5awACQ9uISgShLWZ8BiLTNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq6WktoFeXbM0QIOzehBtm0FXsEqnKAAK_awACQ9uISgxIV03Cy6thNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq6mktoFd0J6nX4BK4l6iCXaWxdtpJAALJawACQ9uISu0Zz5QYejNFNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq62ktoFdcQ0qHbPbbkOUq-q_llVoRAALNawACQ9uISg9ED0ph8tLINgQ", "type": "document"},

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"],caption="""❗️1-sinfdan 11-sinfgacha bo‘lgan darsliklarning eng yangi elektron variantini bizning botdan yuklab oling. 

✅BOT MANZILI: 

👉 @E_KitobXazinasi_Bot
👉 @E_KitobXazinasi_Bot""")
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="6-sinf 📗")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIq72ktoL5OoLJKeR7ozLNzrpnOgw7GAAKdZgACQ9uQSqMB20QeP2cLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq8GktoL5STXkP5YmCB9qIUaydfZS4AAKXZgACQ9uQSthj-oDZtg2pNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq8WktoL5bjFNhqo38G-nKNgEQVtRCAALOZgACQ9uQStymqFLcJ-RVNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq8mktoL7bFLPZS1XPMepdIHpkzpzTAALaZgACQ9uQSkLF3GjxAW-RNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq82ktoL5ZPatL53b58LNKeX-HwOcyAAKvZgACQ9uQSsPtncOUCkqjNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq9GktoL4lLfnSTJAoTWfIUg5t2_teAAKzZgACQ9uQSrsKKggksW8uNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq9WktoL5jGvDIG52IChJpvzlaKOoOAALZZgACQ9uQSnYystpwpxs7NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq9mktoL7ipWy2DbJC_9sMCD_NMcarAALUZgACQ9uQSoQDrHwujfnRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq92ktoL68AzmS9s12l85D0mvWLRvNAALRZgACQ9uQSsjOd35U5enSNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq-GktoL7gO8dsbwTZvtR0SKiUsoErAALSZgACQ9uQSkJpxFTq1PjsNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq-WktoL4ZhGm8N7MxOPqpIzCRKEuSAAKgZgACQ9uQSi47CKZcLbPgNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq-mktoL537Izrrpht28BCBinPL_PsAAKwZgACQ9uQStBLvYU_m2rqNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq-2ktoL5XDeRtcXRdSF0DahD-mjrnAAJ9ZgACQ9uQSl16_0aJopuCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq_GktoL62phSnW3Q0YFtCCd1Ei3CVAAJ_ZgACQ9uQSuRa6pWRCjgUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq_WktoL42BAx2MQYr4m1VPP961fciAAJ6ZgACQ9uQSqxUZSnDqfzoNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq_mktoL48ICXkve0ReRnc6ZaxY2LJAAJ3ZgACQ9uQSlR2STA66r44NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIq_2ktoL41fhsJAsbPIUUM_rg4KBEEAAJ5ZgACQ9uQSqV75KDL1HkhNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrAAFpLaC-OpRthLqRWPC26pv0_ck1KgACcWYAAkPbkEqQHSsAAXspmEY2BA", "type": "document"},

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"],caption="""❗️1-sinfdan 11-sinfgacha bo‘lgan darsliklarning eng yangi elektron variantini bizning botdan yuklab oling. 

✅BOT MANZILI: 

👉 @E_KitobXazinasi_Bot
👉 @E_KitobXazinasi_Bot""")
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="7-sinf 📗")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIrBGktoQn-8PYqwqBnl88o9VpD8wAB3wAC_2kAAkPbkEqdOYaKrAAB1xY2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrBWktoQnbvH9LYANaJVSWsL9mFyGXAALxaQACQ9uQSize5G-DpXkLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrBmktoQk74Q2azRV1wit3Bq56McO2AAL6aQACQ9uQStQM4BhwkKUcNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrB2ktoQnjkp5lIhVwvBOfcIgUgbnUAAILagACQ9uQSkXb49XkQuvRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrCGktoQk70CrMvwgZJlnlRTxx80QFAAL7aQACQ9uQSmo72Cw8JK57NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrCWktoQnrJKzeBmT0MJehA_fssQ2_AAIFagACQ9uQSiccwkZ9YHCaNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrCmktoQmQ9H_YoBOu6v1LTDW4qtUuAALvaQACQ9uQSk88ah6hzE3sNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrC2ktoQmmuRK-mLlU5jYvQZRi06exAAL8aQACQ9uQSpF8HkRhV4lLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrDGktoQnnGyhcNXmlrcGJe8twMnK0AAIGagACQ9uQSleRjkZQSj8yNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrDWktoQmW0SY79woGpBIq59d_S_a4AAL2aQACQ9uQSncBLo7xlqkwNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrDmktoQkDxrbPdOrAbCu9W3cHhHXOAAL4aQACQ9uQSobyYL0YJbNbNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrD2ktoQmTg5Q5xTeNOc1sC2qIUwABYgAC_WkAAkPbkEpZKj5XfYtUOjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrEGktoQkBDuzVh5rz2X7cISqthVk9AAL-aQACQ9uQSs6xMu_X1RC3NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrEWktoQkoXNG-dfSQHwbJAAH-dLV16gACCGoAAkPbkEqEtXAhBvgnxTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrEmktoQn09lvZ0j9bTySaVcf_etN1AAIJagACQ9uQSiw0arDtocO4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrE2ktoQki8j3_m8u_DG_yn6SJUky8AAINagACQ9uQSpSJAyIkwBZ3NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrFGktoQm7T6CdiLBzfoVDbdy3cGRAAAIPagACQ9uQSoT6SykBMZVDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrFWktoQm7cU202ngl1bV4E2cMrzqcAALzaQACQ9uQSkBETPlpbUEQNgQ", "type": "document"},

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"],caption="""❗️1-sinfdan 11-sinfgacha bo‘lgan darsliklarning eng yangi elektron variantini bizning botdan yuklab oling. 

✅BOT MANZILI: 

👉 @E_KitobXazinasi_Bot
👉 @E_KitobXazinasi_Bot""")
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="8-sinf 📗")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIrGWktoWHX70g_JtnW2GnQODLi9XVqAALLagACQ9uQSqFFDtrBZNaCNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrGmktoWHSWH6QMuuYeuMq2mmSsRAKAAKkagACQ9uQSnsDxUep1f7CNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrG2ktoWE_LLMHp0JvMOSRVOud7jfXAAK9agACQ9uQSnr9D3ZQJcU8NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrHGktoWGJBvkHfejrRY0zl8CeRU2oAALBagACQ9uQSmYO9NWEQUpMNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrHWktoWEIXs6twkBqyVmGslbqJUw8AAKyagACQ9uQShSNBAvpcv38NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrHmktoWFkDqjKlqQmEV4zssuY8xXRAAKpagACQ9uQSv2wJTB75oq4NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrH2ktoWHRnmBrpnvBRelmPM7VlHthAAKzagACQ9uQSmeAwf_JwtMNNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrIGktoWHo5C8vh63ZjhhgsP3XB7GfAAK1agACQ9uQSgVaW1mUwD3qNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrIWktoWG5D8V9YUfGfhVcpueQIgHLAALAagACQ9uQSqPmZhuTsp96NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrImktoWH31WUOggV0thFYKfZNO4_9AALGagACQ9uQSqjMoct-m98SNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrI2ktoWHPjwJu58QoP1yfyBDyziA8AALEagACQ9uQSnB3UTKvbl23NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrJGktoWE0hf1H1UxfwjRZIpEiSQhwAAKwagACQ9uQSrpmMUx1cEahNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrJWktoWG3wyteAhGN-zcZxebIkchhAAKtagACQ9uQSuCPmCTqfQOUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrJmktoWGarGTHkO0NB4BYOwLi9D6WAAKoagACQ9uQSi-S9cZZuSvyNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrJ2ktoWHEj9mwb9gXcoeZPCnUhyXEAAKqagACQ9uQSiErBNMElgeuNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrKGktoWHbihzF6kB-HMVytCtI2QKhAAKsagACQ9uQSreFRi0bzDVKNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrKWktoWHoMMsyvShR8PmRaM6cGc0SAAK4agACQ9uQSrXjBX8-h-DtNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrKmktoWFbSb06oeT3XhvIV5BtaHoXAALMagACQ9uQSj8EQaSq3kKLNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrK2ktoWHyz50isWH_YtIWdrl5rRn9AALNagACQ9uQSooLHFrEO_IqNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrLGktoWEBfuwh6ObP4FK5KyDa0jvJAALIagACQ9uQStWqeEEfDobQNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrLWktoWE71oyaYhtyTlb7YxsGPY9lAALKagACQ9uQSrS399SbenLuNgQ", "type": "document"},

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"],caption="""❗️1-sinfdan 11-sinfgacha bo‘lgan darsliklarning eng yangi elektron variantini bizning botdan yuklab oling. 

✅BOT MANZILI: 

👉 @E_KitobXazinasi_Bot
👉 @E_KitobXazinasi_Bot""")
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="9-sinf 📗")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIrMWktobHn_5sSbGCihIRkMUdvYtYfAAI9awACQ9uQSpePFwQ1dY-oNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrMmktobGRnuB_CcbKQ5ZBmM16g5nWAAI8awACQ9uQSgIt2LGV_ONvNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrM2ktobH5gvP2XU-9Nhjyfm1lZJR6AAJNawACQ9uQSoqLXHL4L4hjNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrNGktobGRV3emDzqSifUMAAFt-uvNTwACP2sAAkPbkErrh8GkKKrTWjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrNWktobFHuwL5ZHi_rC9xsSwVSFbeAAJIawACQ9uQSptiH1QqKaxeNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrNmktobGLyx-wS2K6AAE6JrZBKXNivAACc2sAAkPbkEqgwm6JElWqmTYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrN2ktobGIsWXOThJLxfwb4H5Gsd99AAI3awACQ9uQStmDlxkIhM0ENgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrOGktobFMhFK6yt-meJOug4Wv7LwGAAJGawACQ9uQSmdGmmQnn_6NNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrOWktobE5ks8PM7iyRHPYaBbbemHfAAJ3awACQ9uQSl1fpvnR_Rs-NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrOmktobE6F0AGAaAQpz3WImeOG4szAAJLawACQ9uQSk2YL5vEEP3ANgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrO2ktobGxz6_FfBH8acMYkAMtzl7kAAI5awACQ9uQSrMqg2240muhNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrPGktobEP6AmIlNwGdb_eE4KGqPOHAAI-awACQ9uQSqUxKHTAA5nGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrPWktobEmihexfIcPm59pBulZBg0hAAJAawACQ9uQSh9qlSGe_dp9NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrPmktobF3pOA4f6nSd-bKIxjl0P4HAAJCawACQ9uQSha5ymEpHUtKNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrP2ktobGB51cqexzDMKhqYbgIFYdsAAJEawACQ9uQSgOa8YWSgotuNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrQGktobE8imp7wFp8T86a-zzHYlY6AAJFawACQ9uQSj7c6ug5JiguNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrQWktobFNhXX5E2pmppps5mvoHIppAAJWawACQ9uQSks4Iz-eketbNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrQmktobE8nzqi6ORuWQs7wRmaZ4k_AAJZawACQ9uQSqOt3MUk8sBANgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrQ2ktobGKgYvQGycOScbYPQqN4fhlAAJxawACQ9uQSsQ4EiuMPwxRNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrRGktobFzORjQLH56B5A8N8PP56XgAALdYgACS0uZSvTPhQUFIf3wNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrRWktobFsvEf_Qs7TB3p8puz8bbfsAALcYgACS0uZSmB_x0CIJWcnNgQ", "type": "document"},

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"],caption="""❗️1-sinfdan 11-sinfgacha bo‘lgan darsliklarning eng yangi elektron variantini bizning botdan yuklab oling. 

✅BOT MANZILI: 

👉 @E_KitobXazinasi_Bot
👉 @E_KitobXazinasi_Bot""")
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="10-sinf 📗")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIrSWktogvYXu9xsZyQ9vP59hlA0auTAAKGYwACS0uZSk7pQwOyM6APNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrSmktogtk_dxp0rlCNqN2o0ayOqBpAAKlYwACS0uZShtL9_wVMrBJNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrS2ktogu8jkr5GUYPFPjJAAG-212-tAACl2MAAktLmUql2eEC81PYLjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrTGktogthtum0VwYLDm9d3SGD5AnrAAKYYwACS0uZSgNf9O4D5SyuNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrTWktogsAAXo8grrEOtom_1cUO5OrmQACpmMAAktLmUoqzHY72XRBxjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrTmktogvMxxwxHFRWP442rS27Q-K_AAJrYwACS0uZSoI0egZsfeHnNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrT2ktogtuVFqVgRgVaqJRWv-UFASJAAJ0YwACS0uZSq1P47Ab-4-8NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrUGktogsOCIMPyYE94E9xTUkijin1AAJ3YwACS0uZSl-7Rbc6exCwNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrUWktogvWiPHCnR0AAVmfInTy7Bf_CwACi2MAAktLmUp5Tv_0cFsOJjYE", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrUmktogsVUubjhLu59CpwNa5WtVXBAAKMYwACS0uZSjvkuC5mg_fWNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrU2ktogtiOSeo-bjKxZGD8exmGhhoAAKOYwACS0uZSkAzBmgIeMqINgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrVGktoguQzJJGUMzoivVtsym4kyvyAAKjYwACS0uZSrb4k8acZIqGNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrVWktogvqysj2vgQoiN2lTzu4bwUaAAKUYwACS0uZSuzKzAcj4Bc3NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrVmktogvOLsUXyIGvWBmwmnk3y40WAAKPYwACS0uZSjbinR0fC-dONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrV2ktogsOmzMHRPXHc4QZqRawUU3uAAKTYwACS0uZSo6FIj0BLNFiNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrWGktogu9Nc-d4W0vYF4SpwVCbOwxAAKRYwACS0uZSlISjtWrG_0lNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrWWktogtIJBYIhbWtyyK3QP4M7k5uAAKVYwACS0uZSlSlWZ5B8cSqNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrWmktogvR6ML2jhUwc1XrS78lsRy-AAKfYwACS0uZSmr4CbkqrYuONgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrW2ktogvrvjNYwFlj3KPPLNH1j5bwAAKdYwACS0uZSl1ePytZjwpmNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrXGktogv2Sl20SLfS3P9mkTym7p3XAAKbYwACS0uZSgwm1Pv117xTNgQ", "type": "document"},

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"],caption="""❗️1-sinfdan 11-sinfgacha bo‘lgan darsliklarning eng yangi elektron variantini bizning botdan yuklab oling. 

✅BOT MANZILI: 

👉 @E_KitobXazinasi_Bot
👉 @E_KitobXazinasi_Bot""")
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])
@dp.message_handler(IsPrivate(),text="11-sinf 📗")
async def qaytish(message: types.Message):
    fayllar = [
        {"id": "BQACAgIAAxkBAAIrYGktonWMzFHzDSsE5iyy3ClGAawaAAJQZAACS0uZShdKYC2s1TzyNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrYWktonVWn4A1ZcGlu0BqhtKJBO_iAAJVZAACS0uZSpZl06Q41StkNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrYmktonWbi5BHjXHDVfOb6EuvPpC0AAJSZAACS0uZSgmZaTKWPuGWNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrY2ktonUAAbgC0ia1aGUAAXNAa1Jjs08AAkNkAAJLS5lKz1N9-TF7CRw2BA", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrZGktonU-sP6j_wk53xhSgWlbW7OSAAJHZAACS0uZSr2RCvV53g8lNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrZWktonV5mo7aWHfE0O7_nlfQVLPGAAJCZAACS0uZShSuW4cugZzSNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrZmktonWP21CbH8T9M2bgT_J-le8wAAJWZAACS0uZSsAVOiYfZY6_NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrZ2ktonUDRJY-8mEdAtjqXTgiXwUCAAJGZAACS0uZSotUy-yXQ9xDNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIraGktonXDRjws_kpQ9fB0SR2xv4RGAAJIZAACS0uZSpv46zXhcilpNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIraWktonVXPlqtp2QpLdu2QGjPNVFOAAJJZAACS0uZSlfhHcbpY9K9NgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIramktonX_ZJ8D-RGG5LrMXPMn0YuZAAJLZAACS0uZSud7qSDFR_CxNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIra2ktonUbggdOy0IlVCcSoV9o3lj8AAJNZAACS0uZSnxGn1tDpM2rNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrbmktonX9iE82aVHYfcpw12Cl00SJAAJOZAACS0uZShdDqmTEDy7MNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrb2ktonX_V4JZVQ18YU-rFYqegVEHAAJRZAACS0uZSvPciM6GwTNWNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrcGktonU0jqHgTUj4yDmWZROqK75VAAJUZAACS0uZSjhX8UMUJ0OUNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrcWktonVxQntFcazik_PzCUvC07StAAJYZAACS0uZSrdTua2bprzJNgQ", "type": "document"},
        {"id": "BQACAgIAAxkBAAIrXGktogv2Sl20SLfS3P9mkTym7p3XAAKbYwACS0uZSgwm1Pv117xTNgQ", "type": "document"},

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"],caption="""❗️1-sinfdan 11-sinfgacha bo‘lgan darsliklarning eng yangi elektron variantini bizning botdan yuklab oling. 

✅BOT MANZILI: 

👉 @E_KitobXazinasi_Bot
👉 @E_KitobXazinasi_Bot""")
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])











































































