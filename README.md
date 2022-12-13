# YouTube Summary Extraction using ChatGPT

**DISCLAIMER: USE AT YOUR OWN RISK. CHATGPT API IS UNOFFICIAL. I CANNOT GUARANTEE OPENAI WILL NOT TERMINATE YOUR ACCOUNT**

This script uses the [ChatGPT](https://github.com/acheong08/ChatGPT) library to extract a summary and conclusion from a given YouTube video. It does this by first downloading the captions for the video and passing them to ChatGPT for summarization and conclusion extraction.

## Usage

To use this script, first install the necessary dependencies by running:

```pip install -r requirements.txt```

You will also need to put your [session_token](https://github.com/acheong08/ChatGPT/wiki/Setup) in youtube.py:

```config = {
      "session_token": "<SESSION_TOKEN>",
  }```

Next, provide a YouTube video URL as a command line argument when running the script:

```python script.py https://www.youtube.com/watch?v=VIDEO_ID```


The summary will be printed to the command line.

**Note:** This library is rapidly changing and may break without being updated.

For more information on setting up and using ChatGPT, please see the [Wiki](https://github.com/acheong08/ChatGPT/wiki).
