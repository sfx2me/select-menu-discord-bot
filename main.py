import discord

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Bot started!")

class MySelect(discord.ui.View):
    @discord.ui.select(
        placeholder="Select something!",
        options= [
            discord.SelectOption(
                label="Vanilla",
                description="Pick this if you like Vanilla"
            ),
            discord.SelectOption(
                label="Chocolate",
                description="Pick this if you like Chocolate"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")

@bot.slash_command(guild_ids=[996051773527695400], description="Send a select Mneu")
async def select(ctx):
    await ctx.respond("Choose something!", view=MySelect())


bot.run("TOKEN")