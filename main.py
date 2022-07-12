import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "Eid Mubarak ┊ 24/7 Online ┊ Fast Respond ┊ Puasa bor. ┊ Nanti OFF 3 Tahun", url = "https://www.twitch.tv/Danish8409"))


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)