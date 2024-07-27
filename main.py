# app id: 1266729445226577991
# public key: ad1072ec3bf71c65a8324ddfdf6f3b5db00f1f162c2cad2e9c93efc97ebbba0e
import discord
import os
import openai

# file = input("Enter 1, 2, or 3 for loading the chat:\n ")
file = "1"
match (file):
    case "1":
        file = "chat1.txt"  # for professional talks
    case "2":
        file = "chat2.txt"  # for casual talks
    case "3":
        file = "chat3.txt"  # for friendly talks
    case _:
        print("Invalid choice.")
        exit()

with open(file, "r") as f:
    chat = f.read()

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("discord_secret_key")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        try:
            chat += f"{message.author}: {message.content}\n"
            print(f'Message from {message.author}: {message.content}')
            if self.user != message.author:
                if self.user in message.mentions:
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"{chat}\nAddyGPT: ",
                        temperature=1,
                        max_tokens=256,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    channel = message.channel
                    messageToSend = response.choices[0].text
                    await channel.send(messageToSend)
        except Exception as e:
            print(e)
            chat = ""


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
