from discord.ext import commands
from .e import wlE , ipE
_map = {
 "wl": wlE,
 "ip": ipE
}


class AutoHelp(commands.Cog):
    def __init__(self , client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_message(self , message):
        if "whitelist" in str(message.content):
            wlE = _map["wl"]
            wlE.add_field(name="Instructions" , value=f"To whitelist your self , type `whitelist <username>` in {self.client.get_channel(784435495195115564)}")
            await message.channel.send(embed=wlE)
        if "ip" in message.content or "can't connect" in str(message.content) or "not able to connect" in str(message.content) or "can't join" in str(message.content):
            await message.channel.send(embed=ipE)
            
        
def setup(client):
    client.add_cog(AutoHelp(client))