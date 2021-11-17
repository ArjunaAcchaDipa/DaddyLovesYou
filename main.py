import discord
import os
import requests
import random
from keep_alive import keep_alive

client = discord.Client()

def getJoke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "text/plain"})
    return (response.text.encode())

def getIndonesianJoke():
  response = requests.get("https://jokesbapak2.herokuapp.com/v1/", headers={"Accept": "application/json"})

  file = open("joke.png", "wb")
  file.write(response.content)
  file.close()

@client.event
async def on_ready():
    print("Beep boop turning it on")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    prefix = "$"

    help = ["Try send `$joke` instead `$myLife`", "Stop sending `$myLife` as a joke, cuz its not" , "I mean, your life isnt a joke. Jokes has meaning"]

    if message.content.startswith(prefix):
        command = message.content.split(prefix)[1]
        if command == "joke":
          await message.channel.send(getJoke().decode())
        elif command == "injoke":
          getIndonesianJoke()
          await message.channel.send(file=discord.File("joke.png"))
        elif command == "help":
          await message.channel.send(random.choice(help))
        else:
          await message.channel.send("Wrong command!\nTry send `$help`")

keep_alive()
client.run(os.getenv("TOKEN"))