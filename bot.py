import discord
from discord.ext import commands
import wavelink

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await wavelink.NodePool.create_node(
        bot=bot,
        host='localhost',
        port=2333,
        password='youshallnotpass',
        https=False
    )

@bot.command()
async def play(ctx, *, search: str):
    vc = ctx.author.voice
    if not vc:
        return await ctx.send("คุณต้องอยู่ใน voice channel ก่อน!")

    if not ctx.voice_client:
        player: wavelink.Player = await vc.channel.connect(cls=wavelink.Player)
    else:
        player: wavelink.Player = ctx.voice_client

    track = await wavelink.YouTubeTrack.search(search, return_first=True)
    await player.play(track)
    await ctx.send(f"🎶 Playing: `{track.title}`")

@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("🛑 Stopped")

@bot.command()
async def pause(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        await ctx.voice_client.pause()
        await ctx.send("⏸ Paused")

@bot.command()
async def resume(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        await ctx.voice_client.resume()
        await ctx.send("▶️ Resumed")

bot.run("YOUR_DISCORD_BOT_TOKEN")
