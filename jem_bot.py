#Copied from https://discordpy.readthedocs.io/en/latest/quickstart.html#a-minimal-bot
#Starter bot
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

token = ''

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    words = message.content.split(' ')
    for word in words:
        if len(word) > 5:
            if word.endswith('er'):
                await message.channel.send(word + "? I hardly know 'er")

    if 'rat' in message.content:
        await message.channel.send(file=discord.File('images\surprised_rat.jpg'))

    if 'you\'re so right' in message.content:
        await message.channel.send('i\'m gonna sing now')
        
    if 'yippee' in message.content:
        await message.channel.send('yippee')

client.run(token)