from discord import Embed

wlE = Embed(title="Ares AutoHelp" , description="How to whitelist yourself. Trigger `whitelist`" , color=0xFF4301)
wlE.add_field(name="Instructions" , value="To whitelist your self , type `whitelist <username> in `")

ipE = Embed(title="Ares AutoHelp" , description="Server IP Address" , color=0xFF4301)
ipE.add_field(name="Server IP" , value="`play.olympusmc.ml`")
ipE.add_field(name="Alt IP" , value="`---`")
ipE.add_field(name="Website" , value="https://olympusmc.ml")
ipE.add_field(name="Server Version" , value="`1.16.4`")
ipE.add_field(name="Required Client Version" , value="`1.9.x -> 1.16.x`")