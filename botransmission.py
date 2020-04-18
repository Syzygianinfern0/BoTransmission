from telethon.sync import TelegramClient, events

from configs import *

with TelegramClient('BoTransmission', API_ID, API_HASH) as client:
    client.send_message('me', 'Telethon Is Up!')


    @client.on(events.NewMessage(chats=triggerx_chat_id, from_users=delta_leechx_id))
    async def handler(event):
        await event.message.forward_to(leechx_chat_id)


    client.run_until_disconnected()
