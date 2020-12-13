from mcipc.rcon import Client
from discord.ext import commands
pwsd = "rcon!"

t = {
    "alpha": "playerranks.rank.alpha",
    "beta": "playerranks.rank.beta",
    "sigma": "playerranks.rank.sigma",
    "omega": "playerranks.rank.omega",
    "delta": "playerranks.rank.delta",
}

class Teams(commands.Cog):
    def __init__(self , client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def team(self , ctx , username:str=None , team:str = None):
        if username is None:
            await ctx.send(":x: , Username is required")
            return
        if team is None:
            await ctx.send(":x: ,  team is required")
            return
        team = team.lower()
        try:
            perms = t[team]
        except KeyError:
            await ctx.send(":x: , No Such Team!")
            return
        try:
            with Client('play.olympusmc.ml' , 2003) as c:
                c.login(pwsd)
                c.run(f'lp user {username} set permission {perms}')
            await ctx.send(f":white_check_mark: , Player {username} has been added to Team {team}")
        except Exception as e:
            await ctx.send(":x: , An Error occured")

def setup(client):
    client.add_cog(Teams(client))