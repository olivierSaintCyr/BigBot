import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class BigBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = BigBot()
client.run(TOKEN)

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

# TODO support for the echo_test
# data {"phrase":"word", "n_times":int, "dt":int}
# need to receive a phrase from the echo test api then repeats it n_times every dt time

# Futher TODO support for google calendar
