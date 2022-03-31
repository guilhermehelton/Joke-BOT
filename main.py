import discord
import os
import requests
import json


client = discord.Client()
TOKEN = os.environ['TOKEN']

def get_joke():
	response = requests.get('https://v2.jokeapi.dev/joke/Programming?type=single')
	json_data = json.loads(response.text)
	joke = f"Type: {json_data['category']} \nJoke: {json_data['joke']}"
	return joke

@client.event
async def on_ready():
	print(f'Está logado como {client.user}')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$joke'):
		joke = get_joke()
		await message.channel.send(joke)

client.run(TOKEN)
