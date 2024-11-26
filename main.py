import discord
from discord.ext import commands
from gerer_base_donner import ajouter_mot, afficher_mots, afficher_scores, clear_tables, initialiser_db, scan_dict
from keep_alive import keep_alive  # Importer la fonction keep_alive

# Garder le bot en ligne
keep_alive()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

GENERAL_CHANNEL_ID = 1244331373280362496  # Remplacez par l'ID de votre salon général

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    initialiser_db()  # Initialiser la base de données à la connexion

@bot.event
async def on_message(message):
    # Ignorer les messages envoyés par le bot lui-même
    if message.author == bot.user:
        return

    # Vérifier si le message provient du salon général
    if message.channel.id == GENERAL_CHANNEL_ID:
        m = message.content

        # Vérifier si le message ne commence pas par "!"
        if not m.startswith('!'):
            if scan_dict(m.upper()):
                if ajouter_mot(str(message.author), m):
                    await message.channel.send(f":white_check_mark: {m} a été ajouté sous le nom de : {str(message.author)}")
                else:
                    await message.channel.send(f"{m} a déjà été enregistré :cry:")
            else:
                await message.channel.send(f":x: {m} n’existe pas dans la langue française")

    await bot.process_commands(message)

@bot.command(name='mots')
async def cmd_afficher_mots(ctx):
    mots = afficher_mots()
    await ctx.send(mots)

@bot.command(name='scores')
async def cmd_afficher_scores(ctx):
    scores = afficher_scores()
    await ctx.send(scores)

@bot.command(name='clear')
async def cmd_clear(ctx):
    # Vérifier si l'auteur a le rôle "admin"
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role in ctx.author.roles:
        clear_tables()
        await ctx.send("Tous les mots ont été supprimés de la base de données.")
    else:
        await ctx.send("Vous n'avez pas la permission d'exécuter cette commande.")

# Remplacez 'YOUR_TOKEN_HERE' par le jeton de votre bot
bot.run('TOKEN')
