import os, json, random, string, discord, asyncio

with open("markovdict", "r") as marko:
    markodict = json.load(marko)

def get_next_word(wd: str):
    wd = wd.translate(str.maketrans('', '', string.punctuation)).lower()
    if wd not in markodict.keys():
        return None
    return random.choice(markodict[wd])

def generate_chain(in_str : str):
    if len(in_str.split()) == 0:
        return ""
    
    r = random.choice(in_str.split())

    r_no = r.translate(str.maketrans('', '', string.punctuation)).lower()

    if r_no not in markodict.keys():
        generate_chain(r.replace(r, ""))
        return ""
    
    outstr = r
    
    while True:
        add = get_next_word(outstr.split()[-1])
        if add == None:
            return outstr
        else:
            outstr += " " + add        


async def get_reply(msg):
    reply = generate_chain(msg)
    print("waiting " + str(len(reply)/2000 * 60) + " seconds ")
    await asyncio.sleep(len(reply)/2000 * 60)
    return reply
    

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")
    
    async def on_message(self, message : discord.Message):
        if self.user.mentioned_in(message):
            await asyncio.sleep(1)
            async with message.channel.typing():
                print(message.clean_content.replace("@schizo", ""))
                rply = await get_reply(message.clean_content.replace("@schizo", ""))
                await message.reply(rply)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("token")


