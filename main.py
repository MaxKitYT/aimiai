import apiai
import json
import discord
import os

client = discord.Client()

def textMessage(s):
    request = apiai.ApiAI('token').text_request()
    
    request.lang = 'ru'

    request.session_id = 'aimitestai'

    request.query = s

    responseJson = json.loads(request.getresponse().read().decode('utf-8'))

    response = responseJson['result']['fulfillment']['speech']

    if response:
        return response
    else:
        return "Я вас не поняла :c"

@client.event
async def on_ready():
    print('Запустился бот {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    await message.channel.send(textMessage(message.content))
        
token = os.environ.get('TOKEN')
client.run(str(token))
