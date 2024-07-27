# AddyGPT Discord Bot

AddyGPT is a Discord bot that uses the OpenAI API to engage in conversations based on predefined chat types (professional, casual, or friendly) by loading respective chat history from a text file.

## Features

- Engages in conversations based on predefined chat types.
- Uses OpenAI's GPT-3 model for generating responses.
- Maintains chat history to preserve conversation context.

## Prerequisites

- Python 3.6 or higher
- Discord account and server with permission to add bots
- OpenAI API key

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/AddyGPT.git
   cd AddyGPT
   ```

2. **Install the required packages:**

   ```bash
   pip install discord openai
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory and add your OpenAI API key and Discord secret key:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   DISCORD_SECRET_KEY=your_discord_secret_key
   ```

4. **Prepare chat history files:**

   Create `chat1.txt` (professional), `chat2.txt` (casual), and `chat3.txt` (friendly) in the root directory with initial chat content.

5. **Run the bot:**

   ```bash
   python addy_gpt_bot.py
   ```

## Usage

- The bot loads chat history from the specified file and continues the conversation.
- Mention the bot in your messages to get a response.
- The conversation type depends on the initial chat history loaded from the respective file.


## Notes

- Replace `your_openai_api_key` and `your_discord_secret_key` with actual keys.
- Ensure the bot has permission to read and send messages in the channels you use.
