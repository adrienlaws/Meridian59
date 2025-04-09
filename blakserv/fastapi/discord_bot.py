import discord
import requests
import json
from config import DISCORD_BOT_TOKEN, API_BASE_URL  # Import both the token and API base URL from config.py

# Create a Discord client
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Help command
    if message.content.startswith("!help"):
        help_message = (
            "**Available Commands:**\n"
            "- `!who`: Lists all online players.\n"
            "- `!show-object <object_id>`: Displays details of a specific object.\n"
            "- `!send-users <message>`: Sends a message to all users.\n"
            "- `!save-game`: Saves the current game state.\n"
            "- `!send-object <object_id> <message> [<param1> <param2> ... <param8>]`: Sends a message to a specific object with optional parameters.\n"
        )
        await message.channel.send(help_message)

    # Command to query the /admin/who endpoint
    if message.content.startswith("!who"):
        await message.channel.send("Querying online players...")

        try:
            response = requests.get(f"{API_BASE_URL}/admin/who")
            if response.status_code == 200:
                data = response.json()
                players = data.get("players", [])
                if not players:
                    await message.channel.send("No players are currently online.")
                else:
                    result = "**Online Players:**\n"
                    for player in players:
                        name = player.get("name", "Unknown")
                        location = player.get("location", "Unknown")
                        object_id = player.get("objectID", "N/A")
                        result += f"- **Name:** {name}, **Location:** {location}, **ObjectID:** {object_id}\n"
                    await message.channel.send(result)
            else:
                await message.channel.send(f"Failed to query API: {response.status_code} - {response.text}")
        except Exception as e:
            await message.channel.send(f"An error occurred: {str(e)}")

    # Command to query the /admin/show-object/{object_id} endpoint
    elif message.content.startswith("!show-object"):
        try:
            object_id = message.content.split(" ")[1]  # Extract object ID
            response = requests.get(f"{API_BASE_URL}/admin/show-object/{object_id}")
            if response.status_code == 200:
                data = response.json()
                obj = data.get("object", {})
                properties = obj.get("properties", {})

                # Format the properties with indentation for better readability
                formatted_properties = "\n".join(
                    [f"    - **{key}:** {value}" for key, value in properties.items()]
                )

                # Construct the result message
                result = (
                    f"**Object Details:**\n"
                    f"- **ID:** {obj.get('object_id')}\n"
                    f"- **Class:** {obj.get('class')}\n"
                    f"- **Properties:**\n{formatted_properties}"
                )
                await message.channel.send(result)
            else:
                await message.channel.send(f"Failed to query object: {response.status_code} - {response.text}")
        except Exception as e:
            await message.channel.send(f"An error occurred: {str(e)}")

    # Command to send a message to all users
    elif message.content.startswith("!send-users"):
        try:
            msg = " ".join(message.content.split(" ")[1:])  # Extract the message
            if not msg:
                await message.channel.send("Usage: !send-users <message>")
                return

            # Send the message as a query parameter
            response = requests.post(f"{API_BASE_URL}/admin/send-users", params={"message": msg})
            if response.status_code == 200:
                await message.channel.send("Message sent to all users successfully.")
            else:
                await message.channel.send(f"Failed to send message: {response.status_code} - {response.text}")
        except Exception as e:
            await message.channel.send(f"An error occurred: {str(e)}")

    # Command to save the game
    elif message.content.startswith("!save-game"):
        try:
            response = requests.post(f"{API_BASE_URL}/admin/save-game")
            if response.status_code == 200:
                await message.channel.send("Game saved successfully.")
            else:
                await message.channel.send(f"Failed to save game: {response.status_code} - {response.text}")
        except Exception as e:
            await message.channel.send(f"An error occurred: {str(e)}")

    # Command to send a message with optional parameters to a specific object
    elif message.content.startswith("!send-object"):
        try:
            # Extract object ID, message, and optional parameters
            parts = message.content.split(" ", 2)
            if len(parts) < 3:
                await message.channel.send("Usage: !send-object <object_id> <message> [<param1> <param2> ... <param8>]")
                return

            object_id = parts[1]
            remaining_parts = parts[2].split(" ")

            # The first part is the message, the rest are optional parameters
            message_text = remaining_parts[0]
            optional_params = remaining_parts[1:]

            # Map optional parameters to param1, param2, ..., param8
            params = {"object_id": object_id, "message": message_text}
            for i, param in enumerate(optional_params[:8]):  # Limit to 8 parameters
                params[f"param{i + 1}"] = param

            # Send the parameters as query parameters
            response = requests.post(f"{API_BASE_URL}/admin/send-object", params=params)
            if response.status_code == 200:
                await message.channel.send(f"Message sent to object '{object_id}' successfully with parameters: {params}")
            else:
                await message.channel.send(f"Failed to send message to object: {response.status_code} - {response.text}")
        except Exception as e:
            await message.channel.send(f"An error occurred: {str(e)}")

# Run the bot
client.run(DISCORD_BOT_TOKEN)