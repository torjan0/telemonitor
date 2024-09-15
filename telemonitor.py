from telethon import TelegramClient, errors
from telethon.tl.types import UserStatusOnline, UserStatusOffline
import asyncio
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime, timedelta

# Configure logging to file with weekly rotation
log_filename = 'user_activity.log'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler(log_filename, when="W0", interval=1, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
logger.addHandler(logging.StreamHandler())

# Your details from my.telegram.org
api_id = 11111111 # Your API ID HERE (Replace 11111111)
api_hash = 'YOUR API HASH' # Your API Hash
user_to_monitor = '@xyz'  # Replace with the actual username

# Initialize the client with your credentials
client = TelegramClient('anon', api_id, api_hash)

async def monitor_user_activity():
    await client.start()
    previous_status = None

    while True:
        try:
            user = await client.get_entity(user_to_monitor)
            status = user.status
            if isinstance(status, UserStatusOffline) and status.was_online:
                if status.was_online != previous_status:
                    logger.info(f"{user.username if user.username else user.id} was last seen at {status.was_online.strftime('%Y-%m-%d %I:%M %p')}")
                    previous_status = status.was_online
            elif isinstance(status, UserStatusOnline):
                if previous_status != 'online':
                    logger.info(f"{user.username if user.username else user.id} is online.")
                    previous_status = 'online'
            await asyncio.sleep(60)
        except errors.FloodWaitError as e:
            logger.warning(f"Sleeping for {e.seconds} seconds due to flood wait.")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(monitor_user_activity())
