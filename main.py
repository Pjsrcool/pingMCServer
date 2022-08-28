import discord
from mcstatus import JavaServer
from secret import token, ip, port 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$minecraft':
        try:
            if ip == "":
                server = JavaServer("vanillahub.net", timeout=3)
            else:
                server = JavaServer(ip, port, timeout=3)
            status = await server.async_status()
            await message.channel.send(message.author.mention + " ping success!")
        except:
            await message.channel.send(message.author.mention + " ping failed")

if __name__ == "__main__":
    client.run(token)