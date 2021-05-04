import discord
from discord import channel
from discord import client
from discord.utils import get
from dotenv.main import load_dotenv
from keep_alive import keep_alive
import os
from PIL import Image
import redis
import pickle
import io
import requests
import json
import datetime


url1 = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict'
r = redis.Redis('192.168.0.133')
client = discord.Client()


@client.event
async def on_ready():
    print("Bot is up ")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    imsg = message.content
    if(imsg.startswith(".help")):
        await message.reply("this bot gives available vaccination data for your entered district")
    if(imsg.startswith(".vac")):
        async with message.channel.typing():
            p = imsg.split()
            district = imsg.split(".vac ", 1)[1]
            id = r.get(district.lower()+'_cid').decode('utf-8')
            print(id)
            x = datetime.datetime.now()
            date = (x.strftime("%d-%m-%y"))
            try:
                req = requests.get(url1+'?district_id='+id+'&date='+date)
                resp = req.content
                resp = json.loads(resp)
                for i in resp['sessions']:
                    print(i)
                    if i['min_age_limit'] >= 18 and i['available_capacity'] >= 0:
                        await message.reply(str(i))
                    else:
                        continue

            except:
                await message.reply('sorry')


keep_alive()
load_dotenv()
my_secret = os.getenv('mtoken')
# print(my_secret)
client.run(my_secret)
