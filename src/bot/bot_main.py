import os

import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="#")

# mongoclient = pymongo.MongoClient("mongodb://database")
# services_db = mongoclient["services"]
# guilds_col = services_db["guild_services"]

# server_id = 799761080720687164
#{"server_id":"799761080720687164","services": ["echo_test"]}
# {
#     "server_id":"799761080720687164",
#     "services": [
#         "echo_test"
#     ]
# }


# TODO add server to database when new arrival


gateway_url = "http://bot_gateway"

@bot.event
async def on_ready():
    print("BigBot is up!!!")

@bot.command(name='hi')
async def hi(ctx):
    say = "Hi " + ctx.message.author.name
    await ctx.send(say)

# TODO support for the echo_test //almost done
@bot.command(name='echoTest')
async def echo_test(ctx):
    packet = {"server_id":ctx.message.guild.id, "service":"echo_test"}
    data = requests.get(gateway_url, packet)
    if data.status_code == 200:
        message_json = data.json()
        
        if message_json == "This server is not subscribed to this service":
            await ctx.send("This server is not subscribed to this service")
        elif message_json == "The server is not setup":
            await ctx.send("The server is not setup")
        else:
            data = message_json['data']
            if data == "Not setup properly":
                await ctx.send("The service is not setup properly")
            else:
                await ctx.send(data)
    else:
        await ctx.send("Failed routing your request sorry")
        
bot.run(TOKEN)



# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')


# data {"phrase":"word", "n_times":int, "dt":int}
# need to receive a phrase from the echo test api then repeats it n_times every dt time

# Futher TODO support for google calendar

