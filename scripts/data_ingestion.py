

import telethon
from telethon import TelegramClient
import pandas as pd

# Step 1: Setup Telegram API credentials
api_id = '26208008'
api_hash = '5c15901f0de2055cdb6a334a843c3a7f'
phone_number = '+60115689091'


# Step 2: Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def fetch_messages(channel_list, limit=1000):
    await client.start(phone_number)
    all_messages = []

    for channel in channel_list:
        entity = await client.get_entity(channel)
        messages = await client.get_messages(entity, limit=limit)
        
        for message in messages:
            all_messages.append({
                'channel': channel,
                'sender': message.sender_id,
                'timestamp': message.date,
                'text': message.message,
                'media': message.media
            })

    return pd.DataFrame(all_messages)

async def main():
    channel_list = ['@gebeyaadama', '@ZemenExpress', '@nevacomputer', '@ethio_brand_collection', '@modernshoppingcenter']
    df = await fetch_messages(channel_list, limit=1000)
    df.to_csv('EthioMart_NER/data/raw/telegram_messages.csv', index=False)
    await client.disconnect()
    print('Data ingestion completed successfully!')

# Run the script
client.loop.run_until_complete(main())

