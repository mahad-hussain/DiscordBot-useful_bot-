import discord
import datetime, asyncio
import responses
from discord.ext import commands


async def send_message(message, user_message, is_private):
    #sends the message to the user in the birthday channel, the messaged channel or in a direct message
    try:
        response = responses.get_response(user_message)
        if is_private:
            await message.author.send(response)
            return
        elif user_message[0] == "/":
            await message.channel.send(response)
            return
        elif message.channel.name == 'birthday':
            await message.channel.send(response)
            return
    
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = "MTA1NTY1MjI3MDc0Nzk2MzUxMw.Gu_Hr6.-ZvUbu9GtiKSztgMR7GQ_GYlwUu-HTbVo5wi1I"

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))


    @client.event
    async def on_message(message):
        #splits username at # value 
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        #logs the messages in terminal
        print(f'{username}: {user_message} ({channel})')

        #keeps bot from messaging self
        if message.author == client.user:
            return

        #sends message to user in private direct message
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        
        #sends message to user in sever
        else:
            await send_message(message, user_message, is_private=False)
        

    client.run(TOKEN)

