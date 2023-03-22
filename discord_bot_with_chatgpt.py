import discord
from discord.ext import commands
import openai
import datetime

# Define forbidden words:
forbidden_words = ["spam"]

# Set up OpenAI API credentials:
openai.api_key = "openai_api_key"

# Create an intents object:
intents = discord.Intents.default()
intents.members = True

# Create a Discord client instance:
bot = commands.Bot(command_prefix='/', intents=intents)

# Define the ID of the channel where the bot can answer questions:
question_channel_id = 1234567

# Define function to generate answer using ChatGPT:
def generate_answer(question):
     # Define the prompt to send to ChatGPT:
    prompt = f"Please answer my question:  {question}?"

     # Use the OpenAI API to generate the answer:
    response = openai.Completion.create(
         engine="text-davinci-002",
         prompt=prompt,
         temperature=0.7,
         max_tokens=1024,
         n=1,
         stop=None,
         timeout=10,
     )

    # Return the generated answer:
    return response.choices[0].text.strip()

# Message about the successful launch of the bot:
@bot.event
async def on_ready():
     print("Geralt is ready to conduct philosophical reasoning...")

# Welcome new user:
@bot.event
async def on_member_join(member):
     # Greet new users in a separate "new_users" chat:
     new_wanderers_chat = bot.get_channel(1234567)
     await new_wanderers_chat.send(f"Welcome to channel, {member.mention}!")

# Ask a ChatGPT question:
@bot.slash_command(name="question")
async def answer_question(ctx, question: str):
    question_channel = bot.get_channel(question_channel_id)
    if ctx.channel != question_channel:
        channel_mention = question_channel.mention
        await ctx.send(f"Please ask questions in the {channel_mention} channel.")
        return
    # Use ChatGPT neural network to generate an answer:
    answer = generate_answer(question)

    # Send the answer back to the chat:
    await ctx.send(f"{ctx.author.mention}, {answer}")

# Reporting a user:
@bot.slash_command(name="report")
async def report_user(ctx, user_id):
     # Look up the user by ID:
    try:
        reported_user = await bot.fetch_user(user_id)
    except discord.errors.NotFound:
        await ctx.send("User with this ID was not found.")
        return

# Server information:
@bot.slash_command(name="info")
async def send_info(ctx):
    info_channel = bot.get_channel(1234567) 
    await ctx.send(f"Check out the information about the server in the channel: {info_channel.mention}")

# Help:
@bot.slash_command(name="help")
async def send_help(ctx):
    help_channel = bot.get_channel(1234567) 
    await ctx.send(f"Need help with code? Go to channel: {help_channel.mention}")

@bot.event
async def on_message(message):
    # Check if the message was sent in the "channel" chat and contains any forbidden words:
    if message.channel.id == 1234567 and any(word in message.content for word in forbidden_words):
        # Delete the message:
        await message.delete()

        # Send a warning to the user:
        warning_message = f"{message.author.mention}, please refrain from using forbidden words in this chat."
        await message.channel.send(warning_message)

        # Delete any other messages sent by the user in the last 5 minutes that also contain forbidden words:
        def check(m):
            return m.author == message.author and any(word in m.content for word in forbidden_words)

        await message.channel.purge(limit=100, check=check, after=message.created_at - datetime.timedelta(minutes=5))

    # Process commands:
    await bot.process_commands(message)


# Start the Discord client:
bot.run("token")
