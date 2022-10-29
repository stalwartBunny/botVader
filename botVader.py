import discord
import os
import random
from dotenv import load_dotenv

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intent = discord.Intents.default()
intent.members = True
intent.message_content = True
client = discord.Client(intents=intent)


@client.event
async def on_ready():
  for guild in client.guilds:
    if guild.name == GUILD:
      break

  print(f"{client.user} has connected to: {guild.name}. Guild id: {guild.id}")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == 'there is no escape' or message.content == 'There is no escape.':
    response = "Don't make me destroy you."
    await message.channel.send(response)

  if message.content.startswith("$hello"):
    await message.channel.send("Howdy!")

  if message.content == 'creeper' or message.content == 'Creeper' or message.content == 'CREEPER':
    await message.channel.send("Awww ya")

  if message.content == 'i have the high ground' or message.content == 'I have the high ground.' or message.content == 'I have the high ground':
    response = "You underestimate my power!"
    await message.channel.send(response)

  killerPerks = [
    'Bitter Murmur', 'Deerstalker', 'BBQ+Chilli', "SH: Pain Resonance",
    "Hex: Ruin", "Pop Goes the Weasel", "Surge", "Discordance", "Tinkerer",
    "Call of Brine", " Deadlock", "Lethal Pursuer", "Nurse's Calling",
    "SH: Floods of Rage", "Grim Embrace", "Darkness Revealed",
    "Infections Fright", "Hex: Undying", "Corrupt Intervention",
    "Thanatophobia", "Eruption", "Bamboozle", "Hex: Devour Hope",
    "Thrilling Tremors", "Hex: Plaything", "Monitor and Abuse", "Surveillance",
    "Whispers", "Save the Best for Last", "Sloppy Butcher", "I'm All Ears",
    "Enduring", "Make Your Choice", "Dissolution", "Hex: Haunted Ground",
    "Lightborn", "Hex: Pentimento", "Hex: No One Escapes Death",
    "Trail of Torment", "Franklin's Demise", "Remember Me", "Brutal Strength",
    "Dragon's Grip", "Merciless Storm", "Starstruck", "Spirit Fury", "Stridor",
    "Blood Warden", "Play With Your Food", "Dying Light",
    "Spies From the Shadows", "Hex: Huntress Lullabye", "Dark Devotion",
    "Hex: Retribution", "SH: Gift of Pain", "Agitation", "Rancor", "Nemesis",
    "Mindbreaker", "Shadowborn", "Oppression", "No Way Out", "Iron Maiden",
    "Mad Grit", "Overcharge", "Hex: Crowd Control", "Blood Echo", "Hysteria",
    "Coulrophobia", "Coup de Grace", "Iron Grasp", "Fire Up", "Distressing",
    "Hangman's Trick", "Deadman's Switch", "Hex: The Third Seal", "Deathbound",
    "Hoarder", "Forced Penance", "Knock Out", "Unnerving Presence",
    "Hex: Blood Favour", "Hex: Thrill of the Hunt", "Unrelenting",
    "Sceptic Touch", "Zanshin Tactics", "Bloodhound", "Gearhead",
    "Beast of Prey", "Territorial Imperative", "Cruel Limits", "Furtive Chase",
    "Insidious", "Predator", "Overwhelming Presence", "Monstrous Shrine"
  ]

  if message.content == '$dbdkiller':
    response1 = random.choice(killerPerks)
    response2 = random.choice(killerPerks)
    response3 = random.choice(killerPerks)
    response4 = random.choice(killerPerks)
    outputMessage = f"{response1}, {response2}, {response3}, {response4}"
    await message.channel.send(outputMessage)

  survivorPerks = ["Boon: Circle of Healing", "Borrowed Time", "Iron Will", "Kindred", "Spine Chill", "Dead Hard", "Unbreakable", "Lithe", "Adrenaline", "Prove Thyself", "Decisive Strike", "Sprint Burst", "Soul Guard", "Overcome", "Boon: Shadow Step", "Resilience", "We'll Make It", "Deliverance", "Quick & Quiet", "Bond", "We're Gonna Live Forever", "Balanced Landing", "Head On (apply directly to the forehead)", "Inner Strength", "Windows of Opportunity", "Alert", "Desperate Measures", "Boon: Exponential", "Parental Guidance", "Dance With Me", "For the People", "Detective's Hunch", "Built to Last", "Resurgence", "Blast Mine", "Botany Knowledge", "Fixated", "Smash Hit", "Flashbang", "Empathy", "Object of Obsession", "Breakout", "Urban Evasion", "Self-Care", "Distortion", "Residual Manifest", "Blood Pact", "Pharmacy", "Better Together", "Counterforce", "Plunderer's Instinct", "Bite the Bullet", "Tenacity", "Any Means Necessary", "Mettle of Man", "Rookie Spirit", "Boil Over", "Inner Focus", "Vigil", "Diversion", "Small Game", "Aftercare", "Off the Record", "Hope", "Repressed Alliance", "Dark Sense", "Deception", "Saboteur", "Breakdown", "Leader", "Red Herring", "Clairvoyance", "Autodidact", "Fast Track", "Boon: Dark Theory", "Self-Preservation", "Poised", "Deja Vu", "Flip Flop", "Power Struggle", "Stakeout", "Lightweight", "Streetwise", "Appraisal", "This Is Not Happening", "Second Wind", "Solidarity", "Technician", "Buckle Up", "Wake Up", "Ace in the Hole", "Visionary", "Empathic Connection", "Open-Handed", "Calm Spirit", "Lucky Break", "Overzealous", "Babysitter", "Camraderie", "Corrective Action", "Left Behind", "Sole Survivor", "Slippery Meat", "No Mither", "Premonition", "No One Left Behind", "Up the Ante"]

  if message.content == '$dbdsurvivor':
    response1 = random.choice(survivorPerks)
    response2 = random.choice(survivorPerks)
    response3 = random.choice(survivorPerks)
    response4 = random.choice(survivorPerks)
    outputMessage = f"{message.author} your perks are: {response1}, {response2}, {response3}, {response4}"
    await message.channel.send(outputMessage)

  if message.content == "$dbdsurvivor_reroll":
    response = random.choice(survivorPerks)
    await message.channel.send(response)

  if message.content == "$dbdkiller_reroll":
    response = random.choice(killerPerks)
    await message.channel.send(response)
  d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
  d4 = [1, 2, 3, 4]
  d6 = [1, 2, 3, 4, 5, 6]
  d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  d12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  if message.content == "$d20":
    response = random.choice(d20)
    await message.channel.send(response)

  if message.content == "$d12":
    response = random.choice(d12)
    await message.channel.send(response)

  if message.content == "$d10":
    response = random.choice(d10)
    await message.channel.send(response)

  if message.content == "$d4":
    response = random.choice(d4)
    await message.channel.send(response)

  if message.content == "$d6":
    response = random.choice(d6)
    await message.channel.send(response)

client.run(TOKEN)
