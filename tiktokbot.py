import requests
import lightbulb
import hikari
from bs4 import BeautifulSoup
from downloadtk import convert

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"


bot = lightbulb.BotApp(
    token="token",
    default_enabled_guilds=(123456789))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Launched !')

@bot.listen(hikari.StoppingEvent)
async def on_stopping(event):
    print('Stopped')


@bot.command
@lightbulb.command("help", "all commands")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx):
    await ctx.respond("\n/tiktokdl(link)-->mp4sending\n")


@bot.command
@lightbulb.option("link", "link")
@lightbulb.command("tiktokdl", "Upload the tiktok !")
@lightbulb.implements(lightbulb.SlashCommand)
async def tiktokdl(ctx):
        response = requests.get(ctx.options.link, headers={"User-Agent": userAgent})        
        soup = [BeautifulSoup(response.url, 'lxml')]

        soupcut = str(soup).replace("?", "/")
        splitsoup = soupcut.split("/")
        username = splitsoup[3]
        vidid = splitsoup[5]
        convert(username,vidid)

        filename = "tiktok.mp4"
        with open(filename, "rb") as fh:
            f = hikari.File(f'{filename}')
        await ctx.respond(f)


bot.run()
