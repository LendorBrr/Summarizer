# TranscriberGPT

TranscriberGPT is a tool that transcribes live or recorded conversations, generates summaries using OpenAI's GPT-3, and sends the summaries via email.

## Prerequisites

- Python 3.7 or higher
- Google Cloud Speech-to-Text API credentials (JSON key file)
- OpenAI API key
- An email account for sending the summaries

## Dependencies

- google-cloud-speech
- google-auth
- google-auth-httplib2
- google-auth-oauthlib
- google-api-python-client
- grpcio
- openai
- pyaudio
- requests

## Installation

1. Clone this repository:

```bash
git clone https://github.com/LendorBrr/TranscriberGPT.git
cd TranscriberGPT

Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate

Install the required packages:
pip install -r requirements.txt

Configuration
1. Set up your Google Cloud Speech-to-Text API credentials by placing your JSON key file in the project directory and setting the GOOGLE_APPLICATION_CREDENTIALS environment variable:
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"

2. Open transcription.py and replace the placeholder openai_api_key value with your actual OpenAI API key.

3. Configure the email sender, recipient, and server settings in transcription.py according to your preferences.

Usage

Run the main.py script to start the transcription and summary generation process:

python main.py

The script will transcribe live conversations, generate summaries using GPT-3, and send the summaries via email.
