from discord.ext import commands
from discord import Status , Activity , ActivityType , Embed

client = commands.Bot(command_prefix="$")
client.remove_command("help")
extensions = [
    "cogs.help",
    "cogs.stats",
    "cogs.autohelp",
    "cogs.suggestions",
    "cogs.teams"
    #"cogs.development"
]

@client.event
async def on_ready():
    await client.change_presence(status=Status.online , activity=Activity(type=ActivityType.playing , name="$help | Ares"))
    print("READY")
    
for e in extensions:
    client.load_extension(e)

client.run("Nzg0NDM3MjQ5NDY2NDMzNjE2.X8pSHg.jd1I1lPdPUxj3-D9I71PYJvpIu8")
    