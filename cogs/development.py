from discord.ext import commands
from discord.ext.commands.core import command
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionError, ExtensionNotFound, ExtensionNotLoaded

class Development(commands.Cog):
    def __init__(self , client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def load(self , ctx , extension: str = None):
        if extension is None:
            await ctx.send(":x: , Need an extension to load")
            return
        try:
            self.client.load_extension("cogs."+extension)
        except ExtensionAlreadyLoaded:
            await ctx.send(f":white_check_mark: , Extension `cogs.{extension}` is already loaded.")
            return
        except ExtensionNotFound:
            await ctx.send(f":x: , Extension `cogs.{extension} not found.`")
            return
        except ExtensionError:
            await ctx.send(f":x: , Extension `cogs.{extension}` has an error")
            return
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unload(self , ctx , extension: str = None):
        if extension is None:
            await ctx.send(":x: , Need an extension to unload")
            return
        try:
            self.client.unload_extension("cogs."+extension)
        except ExtensionNotLoaded:
            await ctx.send(f":white_check_mark: , Extension `cogs.{extension}` is already unloaded.")
            return
        except ExtensionNotFound:
            await ctx.send(f":x: , Extension `cogs.{extension} not found.`")
            return
        except ExtensionError:
            await ctx.send(f":x: , Extension `cogs.{extension}` has an error")
            return

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def reload(self , ctx , extension: str = None):
        if extension is None:
            await ctx.send(":x: , Need an extension to reload")
            return
        try:
            self.client.load_extension("cogs."+extension)
        except ExtensionAlreadyLoaded:
            try:
                self.client.unload_extension("cogs."+extension)
                self.client.unload_extension("cogs."+extension)
                await ctx.send(f":white_check_mark: , Extension `cogs.{extension}` reloaded.")
            except ExtensionNotFound:
                await ctx.send(f":x: , Extension `cogs.{extension} not found.`")
            except ExtensionError:
                await ctx.send(f":x: , Extension `cogs.{extension}` has an error")
                return

def setup(client):
    client.add_cog(Development(client))