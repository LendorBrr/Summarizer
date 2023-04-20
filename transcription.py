import os
import io
import requests
from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account
from google.cloud.speech_v1p1beta1 import types

# Transcribe audio using Google Speech-to-Text API
def transcribe_audio(gcs_uri):
    credentials = service_account.Credentials.from_service_account_file("/path/to/json/file.json")
    client = speech.SpeechClient(credentials=credentials)

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,  # Assuming the file is in MP3 format
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    response = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = response.result(timeout=300)

    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript

    return transcription

# Summarize text using ChatGPT-4 API

def generate_summary(text):
    openai_api_key = "YOUR-API-KEY"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "prompt": f"Please provide a summary of the following text in 5 bullet points:\n\n{text}",
        "max_tokens": 150,
        "n": 1,
        "stop": None,
        "temperature": 0.7
    }

    response = requests.post(
        "https://api.openai.com/v1/engines/text-davinci-003/completions",
        headers=headers,
        json=data
    )

    response.raise_for_status()

    summary = response.json()["choices"][0]["text"].strip()
    return summary

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_summary(email_addresses, summary, edited_summary=None):
    if edited_summary is not None:
        summary = edited_summary

    email_sender = "EMAIL@EMAIL.COM"
    email_password = "Donkey123"

    msg = MIMEMultipart()
    msg["From"] = email_sender
    msg["To"] = ", ".join(email_addresses)
    msg["Subject"] = "Meeting Summary"

    body = MIMEText(summary, "plain")
    msg.attach(body)

    try:
        with smtplib.SMTP_SSL("XXXX.siteground.biz", 465) as server:
            server.login(email_sender, email_password)
            server.sendmail(email_sender, email_addresses, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print("Error while sending email:", e)
