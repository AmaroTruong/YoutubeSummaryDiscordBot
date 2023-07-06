import discord
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


TOKEN = 'MTEyNjI5NTM4MzQ5NzI2NTE4Mg.G0GTpq.NGtavXCIqe4jGir-QwJRtCwgrMrPTj1u_BtKrQ'

def getResponse(url):
    # get videoID from link
    parsedUrl = urlparse(url)
    qsDict = parse_qs(parsedUrl.query)
    videoId = qsDict.get('v')
    videoId = videoId[0]

    # uses the videoID to get transcript 
    finalTranscript = [] 
    videoText = YouTubeTranscriptApi.get_transcript(videoId, languages=['en'])
    for words in videoText:
        output = words['text']
        finalTranscript.append(output)

    # I want summary to be the gpt4 summary
    # not yet implemented
    summary = finalTranscript
    return(summary)

async def sendMessage(message, user_message, is_private):
    try:
        response = getResponse(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: "{user_message}" ({channel})')

    if user_message.startswith('?'):
        user_message = user_message[1:]
        await sendMessage(message, user_message, is_private=True)
    else:
        await sendMessage(message, user_message, is_private=False)

client.run(TOKEN)
