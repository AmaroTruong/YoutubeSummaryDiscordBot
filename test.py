from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

def getResponse(url):

    parsedUrl = urlparse(url)
    if "youtube.com" not in parsedUrl.netloc:
        raise ValueError("The provided URL is not a YouTube link")
    qsDict = parse_qs(parsedUrl.query)
    videoId = qsDict.get('v')
    if videoId is None:
        raise ValueError("The provided URL does not include a video ID")

    videoId = videoId[0]

    finalTranscript = [] 

    videoText = YouTubeTranscriptApi.get_transcript(videoId, languages=['en'])
    for words in videoText:
        output = words['text']
        finalTranscript.append(output)

    summary = finalTranscript
    return(summary)

url = "https://www.youtube.com/watch?v=Z6nkEZyS9nA&ab_channel=Python360"
print(getResponse(url))
