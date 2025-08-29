from telethon import TelegramClient, events
import asyncio

# 👉 Completa con tus datos de API
api_id = 123456   # tu API ID de my.telegram.org
api_hash = "tu_api_hash"
phone = "+5491112345678"  # tu número con código de país
grupo_destino = "https://t.me/amor_828388383"  # link o @usuario del grupo

# Crear cliente
client = TelegramClient("session", api_id, api_hash)

async def reenviar():
    while True:
        try:
            # Tomar el último mensaje de Mensajes guardados
            mensajes = await client.get_messages("me", limit=1)
            if mensajes:
                await client.send_message(grupo_destino, mensajes[0])
                print("✅ Mensaje reenviado")
        except Exception as e:
            print("❌ Error:", e)
        await asyncio.sleep(600)  # 600 segundos = 10 minutos

@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("Bot iniciado ✅")

async def main():
    asyncio.create_task(reenviar())
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
  
