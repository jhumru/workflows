import sys
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def download_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        plaintext_transcript = TextFormatter().format_transcript(transcript)
        with open('transcript.txt', 'w') as f:
            f.write(plaintext_transcript)
    except Exception as e:
        print('An error occurred:', str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_transcript.py <YouTube Video ID>")
        sys.exit(1)
    video_id = sys.argv[1]
    download_transcript(video_id)
