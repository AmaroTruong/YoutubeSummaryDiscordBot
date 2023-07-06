from youtube_transcript_api import YouTubeTranscriptApi

finalTranscript = [] 

videoText = YouTubeTranscriptApi.get_transcript('Z6nkEZyS9nA', languages=['en'])
for words in videoText:
    output =(words['text'])
    finalTranscript.append(output)

answer = finalTranscript
print(answer)

