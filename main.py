# Import the required functions
from transcription import transcribe_audio, generate_summary, send_email_summary

# Replace with the path to your audio file
audio_file_path = "gs://your-bucket-name/path/to/your/audio-file.mp3"

# Transcribe and generate a summary
transcription = transcribe_audio(audio_file_path)
print("Transcription:", transcription)
summary = generate_summary(transcription)
print("Summary:", summary)

# Let the user review and edit the summary
print("\nPlease review the summary and make any necessary changes:")
edited_summary = input()
if edited_summary.strip() != "":
    summary = edited_summary

# Replace with the email addresses you want to send the summary to
email_addresses = ["varna.mantas@gmail.com", "crow.commerce@gmail.com"]

# Send the summary to the provided email addresses
send_email_summary(email_addresses, summary)
