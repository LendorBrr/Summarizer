# Import the required functions
from transcription import transcribe_audio, generate_summary, send_email_summary

# Replace with the path to your audio file
gcs_uri = "gs://your_bucket/joe.mp3"

# Transcribe and generate a summary
transcription = transcribe_audio(gcs_uri)
print("Transcription:", transcription)
summary = generate_summary(transcription)
print("Summary:", summary)

# Let the user review and edit the summary
print("\nPlease review the summary and make any necessary changes:")
edited_summary = input()
if edited_summary.strip() != "":
    summary = edited_summary

# Replace with the email addresses you want to send the summary to
email_addresses = ["EMAIL@gmail.com"]

# Send the summary to the provided email addresses
send_email_summary(email_addresses, summary)
