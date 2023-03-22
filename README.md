# discord_bot_with_chatgpt.py

This is a Python script that sets up a Discord bot to answer user questions using the OpenAI ChatGPT API. The script uses the "discord" and "discord.ext" libraries to handle bot events and commands.

The script defines several events that the bot can respond to, such as greeting new users, answering questions using ChatGPT, reporting a user, and providing server information and help. The bot can also detect and delete messages that contain forbidden words in a specific chat.

The script initializes the OpenAI API credentials and sets up the "generate_answer" function to generate an answer using ChatGPT when a user asks a question. The "question" command uses this function to generate and send a response back to the user.

The "report" command allows users to report another user by ID, while the info and help commands provide information about the server and how to get help with code.

The script uses "intents" to enable member tracking and uses the "bot.run" method to start the Discord client with the bot token.

For this bot to work, the "openai.api_key" variable must contain your personal OpenAI API Key, and in the last line, "token" must be replaced with the actual token of your Discord bot.

Authors of the libraries and API's used in my code:

    - "discord.py": Written by Rapptz and contributors.
    - "OpenAI API": Developed and maintained by OpenAI.
