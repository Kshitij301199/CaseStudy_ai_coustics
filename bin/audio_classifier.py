import os
from pydub import AudioSegment

# Function to classify speech quality based on audio file duration
def classify_speech_quality(file_path):
    audio = AudioSegment.from_file(file_path)
    duration_seconds = len(audio) / 1000  # Convert milliseconds to seconds

    if duration_seconds < 10:
        return "Short"
    elif 10 <= duration_seconds < 30:
        return "Medium"
    else:
        return "Long"

# Function to process and classify speech quality for a set of audio files
def process_and_classify_audio_files(file_directory):
    for filename in os.listdir(file_directory):
        if filename.endswith(".mp3"):
            file_path = os.path.join(file_directory, filename)
            quality = classify_speech_quality(file_path)
            print(f"Speech file '{filename}' classified as {quality} speech.")

# Example usage
audio_directory = "../audio_files/"
process_and_classify_audio_files(audio_directory)
