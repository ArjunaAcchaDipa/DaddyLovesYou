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

    commandHelp = """Hello, this is a Discord Bot to satisfy your needs in dad jokes.

All that you need know is our prefixes is `$` and you can get the joke in english by typing `$joke` or in indonesia by typing `$injoke`.
If you need any help, try typing `$help`

One thing that you need to know, I will convert your `wkwk` into `xixi` because, thats what dads do right?
Enjoy the joke!"""

    if message.content.startswith(prefix):
        command = message.content.split(prefix)[1]
        if command == "joke":
          await message.channel.send(getJoke().decode())
        elif command == "injoke":
          getIndonesianJoke()
          await message.channel.send(file=discord.File("joke.png"))
        elif command == "help":
          await message.channel.send(random.choice(help))
        elif command == "command":
          await message.channel.send(commandHelp)
        elif command == "flip":
          result = random.randint(1,2)
          if result == 1:
            await message.channel.send("Head!")
          else:
            await message.channel.send("Tail!")
        elif not any(char in ["(", ")", "=", ","] for char in command):
          await message.channel.send("Wrong command!\nTry send `$help`")
    elif message.content.lower().startswith("w") or message.content.lower().startswith("k"):
      isXIXI = True
      newMessage = ""
      for indexCharacter in range (len(message.content)):
        if not (message.content[indexCharacter].lower() == "w" or message.content[indexCharacter].lower() == "k"):
          isXIXI = False
          break
        else:
          if message.content[indexCharacter] == "W":
            newMessage += "X"
          elif message.content[indexCharacter] == "w":
            newMessage += "x"
          elif message.content[indexCharacter] == "K":
            newMessage += "I"
          else:
            newMessage += "i"

      if isXIXI:
        author = str(message.author).split("#")[0]
        await message.channel.purge(limit=1)
        
        newMessage = author + " said: " + newMessage
        await message.channel.send(newMessage)

keep_alive()
client.run(os.getenv("TOKEN"))