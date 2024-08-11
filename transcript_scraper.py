from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
from xml.etree.ElementTree import ParseError


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

            return transcriptString
        
        else:
            print(f"Skipping video {video_id}: No English transcript available")
            return None
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


video_url = "https://www.youtube.com/watch?v=XXYlFuWEuKI&list=RDQMgEzdN5RuCXE&start_radio=1&ab_channel=TheWeekndVEVO"
api_key = "AIzaSyA7G8WsdPw5kgLAPmWG8nlE-KbrDOnPJvM"
playlist_id = "PLBGpyGDMhIZP9l_TaPWzB1aIfdBnJTy5i"

video_ids = get_video_id(api_key, playlist_id)
print(video_ids)

for item in video_ids:
    print(item)
    transcript = get_transcript(item)
    if transcript is not None:
        with open(f"transcripts/transcript_{item}.txt", "w",encoding='utf-8') as f:
            f.write(transcript)
    