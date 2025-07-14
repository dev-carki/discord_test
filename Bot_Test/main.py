import sys
import os
import discord

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common', 'constants')))

import constants as const

class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(int(const.CHANNEL_ID))
        await channel.send('Hello World')
 
 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(const.TEST_TOKEN)