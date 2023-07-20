# GPT-YouTube-DiscordBot

This Discord bot leverages the `youtube_transcript_api` and `openai` modules to generate summarized transcripts of YouTube videos. Upon receiving a YouTube video link, the bot fetches the video's transcript, summarizes it, and sends the summary to the requesting user or channel.

## Prerequisites

To run this bot, you will need:

- Python 3.6 or above
- `discord` module
- `youtube_transcript_api` module
- `openai` module
- `urllib.parse`

You can install these modules using pip:

## Getting Started

1. Clone this repository.
git clone https://github.com/AmaroTruong/YoutubeSummaryDiscordBot
2. Navigate to the directory.
3. Open the bot script file (`bot.py`) in your preferred text editor.
4. Update `TOKEN` with your Discord bot's token and `openai.api_key` with your OpenAI API key:
```python
openai.api_key = "YOUR_OPENAI_API_KEY"
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
```
## Running the Bot

1. Once you have installed the prerequisites and updated the API keys, you can run the bot with:
python bot.py

If the bot starts successfully, it will print out a message confirming it's now running.

## Bot Commands

- `$transcribe <YouTube Video URL>`: The bot will post the summarized transcript in the same channel.
- `$transcribePM <YouTube Video URL>`: The bot will send the summarized transcript to the requesting user in a private message.

## Code Overview

The bot has several core functions:

- `getResponse(url)`: This function fetches a YouTube video's transcript, summarizes it using OpenAI GPT-3.5, and returns the summary.
- `sendMessage(message, user_message, is_private)`: This function sends the summarized transcript either to the same channel or as a private message to the user.
- `on_ready()`: This function prints a message when the bot is successfully running.
- `on_message(message)`: This function triggers whenever a message is received. If the message is a valid command, the bot will generate and send the summarized transcript.

## Screenshots

<img width="1110" alt="Screenshot 2023-07-19 at 10 00 04 PM" src="https://github.com/AmaroTruong/YoutubeSummaryDiscordBot/assets/137460611/b1bf6c93-b54b-4457-b7da-6713313e88d6">

<img width="681" alt="Screenshot 2023-07-19 at 10 05 28 PM" src="https://github.com/AmaroTruong/YoutubeSummaryDiscordBot/assets/137460611/57efdfc8-488f-4f55-b307-c36edf587c3f">

<img width="950" alt="Screenshot 2023-07-19 at 10 05 57 PM" src="https://github.com/AmaroTruong/YoutubeSummaryDiscordBot/assets/137460611/a3ad5cae-8bc4-4e63-b0af-8b1dea6c69f9">


## How it Works

The bot listens for messages in the server. When it detects a valid command, it fetches the transcript of the specified YouTube video using the `youtube_transcript_api`. The transcript is then summarized using OpenAI's GPT-3.5, and the summary is sent back to the Discord server.



