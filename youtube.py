import yt_dlp
import webvtt
import re
import os
import sys

from revChatGPT.revChatGPT import Chatbot

def get_summary(captions, output="summary"):
    # For the config please go here:
    # https://github.com/acheong08/ChatGPT/wiki/Setup
    config = {
        "session_token": "<SESSION_TOKEN>",
    }

    chatbot = Chatbot(config, conversation_id=None)

    if output == "summary":
        prompt = "Can you list some of the takeaways from this text please? Either in a few paragraphs (less than 500 words), or bullet points. Also, please don't include anything about sponsors. Try not to be biased; if there are opposing views/conclusions, try to include details from both. Here is the text: "
    else:
        prompt = "Please try to determine the conclusion of this text. In your response, include the question that the conclusion is addressing: "

    summary = chatbot.get_chat_response(prompt + captions, output="text")
    return summary['message']


def remove_text_in_parenthesis(s: str) -> str:
    # Use a regex to match text within parenthesis and square brackets
    # and replace them with an empty string
    s = re.sub(r'[\[\(][^\]\)]*[\]\)]', '', s)
    # Replace multiple spaces with a single space
    s = re.sub(' +', ' ', s)
    # Return the modified string
    return s


def check_file_exists(directory, file_extension):
    # Check if any file in the given directory has the given file extension
    files = os.listdir(directory)
    return any(file.endswith(file_extension) for file in files)


# URL of the YouTube video.
# If a URL was provided as a command line argument, use that.
# Otherwise, default to a Marques Brownlee link.
if len(sys.argv) > 1:
    video_url = sys.argv[1]
else:
    video_url = "https://www.youtube.com/watch?v=0gNauGdOkro"

# Try to download curated subtitles. If it doesn't work, fallback to autogenerated
with yt_dlp.YoutubeDL({
    'writeautomaticsub': False,
    'writesubtitles': True,
    'subtitleslangs': ['en'],
    'skip_download': True
}) as ydl:
    ydl.download([video_url])

if not check_file_exists(os.getcwd(), ".vtt"):
    with yt_dlp.YoutubeDL({
        'writeautomaticsub': True,
        'writesubtitles': False,
        'subtitleslangs': ['en'],
        'skip_download': True
    }) as ydl:
        ydl.download([video_url])

# Print the names of all files with the '.vtt' extension
captions = []
files = os.listdir(os.getcwd())
for file in files:
    if file.endswith('.vtt'):
        for line in webvtt.read(file):
            text = line.text.strip()
            captions.append(remove_text_in_parenthesis(text))

        # Get the unique captions and sort them
        captions = sorted(set(captions))

        # Encode the Unicode strings using the utf-8 codec and handle any exceptions
        captions = [c.encode("utf-8", "replace").decode() for c in captions]

        print(get_summary("\n".join(captions)))

        os.remove(file)