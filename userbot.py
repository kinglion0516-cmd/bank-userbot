from telethon import TelegramClient, events

# my.telegram.org saytidan oladigan ma'lumotlaringiz
api_id = 31141003          # O'zingizning API ID raqamingizni yozing
api_hash = 'c329b9016b1426ba463f34a91909235e' # O'zingizning API Hash'ingizni yozing

# Bank botining username yoki ID raqami (masalan, bankning rasmiy boti)
# Eslatma: Ba'zan bank botlari raqam bo'ladi yoki username'ga ega bo'ladi
BANK_BOT_USERNAME = 'HUMOcardbot'

# Xabar tashlanishi kerak bo'lgan guruhning ID raqami (yoki username'i)
TARGET_GROUP_ID = -1002046847949  # Guruhning ID raqami (minus bilan boshlanadi)

client = TelegramClient('my_session', api_id, api_hash)

@client.on(events.NewMessage(from_users=BANK_BOT_USERNAME))
async def handle_bank_sms(event):
    message_text = event.raw_text

    # Faqat kartaga pul tushganini bildiruvchi xabarlarni filter qilish mumkin (ixtiyoriy)
    # Masalan, xabar ichida "tushdi", "UZS", "sum" yoki "karta" degan so'zlar bo'lsa:
    if "tushdi" in message_text.lower() or "uzs" in message_text.lower() or "so'm" in message_text.lower():
        # O'sha xabarni o'zingizning guruhingizga yuborish (forward qilish yoki matn sifatida tashlash)
        await client.send_message(TARGET_GROUP_ID, f"💳 Yangi to'lov keldi:\n\n{message_text}")
        print("Xabar guruhga yuborildi!")

print("Userbot ishga tushdi va bank xabarlarini poylamoqda...")
client.start()
client.run_until_disconnected()
