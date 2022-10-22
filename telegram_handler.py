from telethon import TelegramClient, events

TELEGRAM_APP_ID = "16997236"
TELEGRAM_APP_HASH = "8d2ad8d14f11f66972686894a8d914ad"

client = TelegramClient("session", TELEGRAM_APP_ID, TELEGRAM_APP_HASH)

client.start()


@client.on(events.NewMessage())
async def handler(event):
    await print("Welcome")


