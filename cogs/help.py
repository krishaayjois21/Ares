from discord.ext import commands
from discord import Embed

class Help(commands.Cog):
    def __init__(self , client):
        self.client = client
    
    @commands.command()
    async def help(self , ctx):
        e = Embed(title="**Ares Help**" , color=0xFF4301 , description="Command List for Ares")
        e.add_field(name="`$status <server>`" , value="Returns the status of the MC Server provided query is set to true. Deaults to Hypixel")
        e.add_field(name="`$suggest <suggestion>`" , value=f"Suggest something for the server in {self.client.get_channel(784792384289767425).mention}")
        e.add_field(name="`$team <mc_username> <team>`" , value="**ADMIN ONLY** , Assigns the specified username a team")
        e.add_field(name="`$server_info`" , value="Gives you connection details for server")
        await ctx.send(embed=e)
        
def setup(client):
    client.add_cog(Help(client))