import discord
import random
import os
import webbrowser
p = os.listdir('img')
intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(command_prefix='$', intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('Голбальное потепление'):
        if random.randint(0, 1) == 1:
            img = random.choice(p)
            with open(f'img/{img}', 'rb') as f:
                pit = discord.File(f)
            await message.channel.send(file=pit)
        else:
            webbrowser.open_new('https://www.un.org/ru/climatechange/science/causes-effects-climate-change')
client.run('token')

if __name__ == '__main__':
    pass
