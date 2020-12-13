from discord.ext import commands
import base64
from requests import request
from discord import Embed
from .e import ipE
class Status(commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command()
    async def server_info(self , ctx):
        await ctx.send(embed=ipE)


    @commands.command()
    @commands.max_concurrency(1)
    async def status(self , ctx , server: str = None):
        if server is None:
            server = "mc.hypixel.net"
        
        
        r = request(method="GET" , url=f"https://api.mcsrvstat.us/2/{server}")
        data = r.json()
        if data["online"] is True:
            o = data["players"]["online"]
            motd = data["motd"]["clean"]
            l1 = motd[0]
            l2 = ""
            if motd[1] is not None:
                l2 = motd[1]
            m = data["players"]["max"]
            e = Embed(title="**Server Status**" , description=f"Server stats of {server}" , color = 0x00ff00)
            e.add_field(name="IP" , value=server , inline=False)
            e.add_field(name="Players Online" , value=f"{o}/{m}" , inline=False)
            e.add_field(name="Server Version", value=data["version"],inline=False)
        
            #e.add_field(name="World/Level Name" , value=data["map"])
            e.add_field(name="MOTD" , value=f"{l1}\n{l2}",inline= False)
            e.set_thumbnail(url="https://api.mcsrvstat.us/icon/"+server)
            e.set_footer(text="Powered by Ares")
            await ctx.send(f"{ctx.author.mention}" , embed = e)
        else:
            e = Embed(title="**Server Status**" , description=f"Server stats of {server}" , color = 0x0ff0000)
            e.add_field(name="Status" , value="OFFLINE")
            await ctx.send(f"{ctx.author.mention}" , embed=e)
       
def setup(client):
    client.add_cog(Status(client))