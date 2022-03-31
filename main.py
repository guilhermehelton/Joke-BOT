import discord

client = discord.Client()

@client.event
async def on_ready():
	print(f'Está logado como {client.user}')

@client.event
async def on_message(message):
	