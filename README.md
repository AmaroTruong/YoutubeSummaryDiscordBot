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

<img width="1099" alt="Screenshot 2023-07-06 at 1 56 16 AM" src="https://github.com/AmaroTruong/YoutubeSummaryDiscordBot/assets/137460611/ec2a3ef5-2c0d-4db4-a37e-e3a4268fbdac">

<img width="666" alt="Screenshot 2023-07-06 at 1 58 26 AM" src="https://github.com/AmaroTruong/YoutubeSummaryDiscordBot/assets/137460611/dd46bd01-d6ea-4d11-b4c3-bfbc090a3742">

<img width="950" alt="Screenshot 2023-07-06 at 1 58 36 AM" src="https://github.com/AmaroTruong/YoutubeSummaryDiscordBot/assets/137460611/587e68a3-4dd8-4df6-9f5b-dfd80f2e58bb">

<img width="760" alt="Screenshot 2023-07-06 at 1 59 04 AM" src="https://github.com/AmaroTruong/YoutubeSummaryDiscordBot/assets/137460611/e8c726d0-2e48-448d-81be-872b33d9d5aa">

## How it Works

The bot listens for messages in the server. When it detects a valid command, it fetches the transcript of the specified YouTube video using the `youtube_transcript_api`. The transcript is then summarized using OpenAI's GPT-3.5, and the summary is sent back to the Discord server.



