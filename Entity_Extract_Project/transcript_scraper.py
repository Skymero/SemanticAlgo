from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
from xml.etree.ElementTree import ParseError
# from translate import Translator

def get_languages(video_id):
    url = f'https://www.googleapis.com/youtube/v3/captions?part=id,snippet&videoId={video_id}&key={api_key}'
    response = requests.get(url)
    data = response.json()

    print(data)
    if 'error' in data:
        print(f"Error: {data['error']['message']}")
        return []
    
    #print(data['items'][0]['snippet']['language'])
        
    language = data['items'][0]['snippet']['language']    
    
    return language
    


def has_english_transcript(video_id):
    try:
        transcripts = YouTubeTranscriptApi.get_transcripts([video_id], languages=['en'])
        return len(transcripts) > 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def get_transcript(video_id):
    """
    Retrieves the transcript of a YouTube video given its video ID.

    Args:
        video_id (str): The ID of the YouTube video.

    Returns:
        None

    This function uses the YouTubeTranscriptApi library to retrieve the transcript of a YouTube video. It takes the video ID as input and saves the transcript in a text file named "transcript.txt". The function first retrieves the transcript using the `get_transcript` method of the `YouTubeTranscriptApi` class, specifying the video ID and the language as 'en'. It then prints the type, length, and the first element of the transcript list. The function then iterates over each element in the transcript list and appends the 'text' field to a list called `textList`. The function then concatenates all the elements in `textList` into a single string called `transcriptString` and prints it. Finally, the function opens the file "transcript.txt" in write mode and writes the `transcriptString` to the file.

    Note:
        - The function assumes that the `YouTubeTranscriptApi` library is imported at the beginning of the file.
        - The function assumes that the `video_id` parameter is a valid YouTube video ID.
        - The function does not handle any exceptions that may occur during the retrieval or file writing process.

    """
    try:
        if has_english_transcript(video_id):
            srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            textList = []
            for i in srt:
                textList.append(i['text'])

            transcriptString = ""
            for item in textList:
                transcriptString += item + " "

            return transcriptString, True, 'en'
        
        else:
            print(f"Skipping video {video_id}: No English transcript available")
            
            lan = get_languages(video_id) 
            srt = YouTubeTranscriptApi.get_transcript(video_id, languages=[lan])
            textList = []
            for i in srt:
                textList.append(i['text'])

            transcriptString = ""
            for item in textList:
                transcriptString += item + " "

            return transcriptString, False, lan
            
    except ParseError as e:
        print(f"Error parsing XML data for video {video_id}: {e}")
        return None
        
def get_video_id(api_key, playlist_id):
    
    # Define the API request URL
    url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={playlist_id}&maxResults=50&key={api_key}'
    
    # Make the request and get the response
    response = requests.get(url)
    data = response.json()
    
    if 'error' in data:
        print(f"Error: {data['error']['message']}")
        return []
    
    #extract the video IDs from the response
    video_ids = [item['contentDetails']['videoId'] for item in data['items']]
    
    return video_ids


api_key = "AIzaSyA7G8WsdPw5kgLAPmWG8nlE-KbrDOnPJvM"
playlist_id = "PLBGpyGDMhIZP9l_TaPWzB1aIfdBnJTy5i"

video_ids = get_video_id(api_key, playlist_id)
#print(video_ids)

for item in video_ids:
    #print(item)
    transcript, flag, language = get_transcript(item)
    if flag is True:
        with open(f"transcripts/transcript_{item}.txt", "w",encoding='utf-8') as f:
            f.write(transcript)
    else:
        continue
        # with open(f"transcripts/transcript_{item}.txt", "w",encoding='utf-8') as f:
        #     f.write(transcript)
        #     f.close()
        
        
        # with open(f"transcripts/transcript_{item}.txt", "r",encoding='utf-8') as f:
        #     text = f.read()
            
        # src_lang = language
        # dest_lang = 'en'
        # translator = Translator(from_lang=src_lang, to_lang=dest_lang)
        # translation = translator.translate(text)
        
        # with open(f"transcripts/transcript_{item}_translated.txt", "w",encoding='utf-8') as file:
        #     file.write(translation)
                
            
            
            
        
        
    