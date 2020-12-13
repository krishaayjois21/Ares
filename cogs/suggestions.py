from discord.ext import commands
from discord import Embed,
id = 784792384289767425
up = "👍"
down= "👎"
cross = "❌"
tick = "✅"

class Suggestions(commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command()
    async def suggest(self , ctx , s: str = None):
        if s is None:
            await ctx.send(":x: , Suggest something")
            return
        e = Embed(title="New Suggestion :fire:" , description=f"From {ctx.author.mention}" , color=0xFF4301)
        e.add_field(name="Content" , value=s)
        e.set_footer(text="Suggestions powered by Ares")
        c = self.client.get_channel(id)
        try:
            m = c.send(embed=e)
            await ctx.message.add_reaction(emoji=tick)
            await m.add_reaction(emoji=up)
            await m.add_reaction(emoji=down)
        except Exception as e:
            await ctx.message.add_reaction(emoji=cross)


def setup(client):
    client.add_cog(Suggestions(client))