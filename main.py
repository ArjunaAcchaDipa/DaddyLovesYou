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

    help = ["Try send `$joke` or `$injoke` for Indonesian Jokes instead `$myLife`", "Stop sending `$myLife` as a joke, cuz its not" , "I mean, your life isnt a joke. Jokes has meaning"]

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
    elif message.content.lower().startswith("w") or message.content.lower().startswith("k"):
      isXIXI = True
      for indexCharacter in range (len(message.content)):
        if not (message.content[indexCharacter].lower() == "w" or message.content[indexCharacter].lower() == "k"):
          isXIXI = False
          break

      newMessage = ""
      if isXIXI:
        messageContent = message.content
        author = str(message.author).split("#")[0]
        await message.channel.purge(limit=1)
        for character in messageContent:
          if character == "W":
            newMessage += "X"
          elif character == "w":
            newMessage += "x"
          elif character == "K":
            newMessage += "I"
          else:
            newMessage += "i"
        
        newMessage = author + " said: " + newMessage
        await message.channel.send(newMessage)

keep_alive()
client.run(os.getenv("TOKEN"))