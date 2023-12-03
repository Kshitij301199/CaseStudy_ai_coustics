import os
from pydub import AudioSegment
import eyed3
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import argparse

# Function to classify speech quality based on audio file duration
def analyze_audio_quality(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Load the audio file
    audio = AudioSegment.from_file(file_path)

    # Get basic information
    duration_seconds = len(audio) / 1000.0
    channels = audio.channels
    sample_width = audio.sample_width
    frame_rate = audio.frame_rate

    # Measure loudness (average amplitude)
    loudness = audio.rms

    # Print the analysis results
    print(f"Duration: {duration_seconds:.2f} seconds")
    print(f"Channels: {channels}")
    print(f"Sample Width: {sample_width} bytes")
    print(f"Frame Rate: {frame_rate} Hz")
    print(f"Loudness: {loudness:.2f} dB")
    
def read_mp3_metadata(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Load MP3 metadata
    audiofile = eyed3.load(file_path)

    # Print metadata information
    print(f"Title: {audiofile.tag.title}")
    print(f"Artist: {audiofile.tag.artist}")
    print(f"Album: {audiofile.tag.album}")
    print(f"Track Number: {audiofile.tag.track_num}")
    print(f"Year: {audiofile.tag.getBestDate()}")
    print(f"Duration: {audiofile.info.time_secs} seconds")
    return audiofile.tag.title
    
def plot_librosa(file_path,title):
    import warnings
    warnings.filterwarnings("ignore")   
    
    title = title.lower().strip().replace(" ","_")
    data, sampling_rate = librosa.load(file_path);
    
    fig,ax = plt.subplots(nrows=2, ncols=1, figsize = (12,8))
    
    librosa.display.waveshow(data, sr=sampling_rate,ax=ax[0])
    
    n_fft = 2048
    
    ft = np.abs(librosa.stft(data[:n_fft], hop_length = n_fft+1))
    ax[1].plot(ft);
    ax[1].set_title('Spectrum');
    ax[1].set_xlabel('Frequency Bin');
    ax[1].set_ylabel('Amplitude');
    fig.tight_layout()
    os.chdir("images/")
    fig.savefig(f'{title}.jpeg',dpi=300)

def main():
    parser = argparse.ArgumentParser(description="Analyse audio mp3 file")
    parser.add_argument("--filename",required=True , help="Path to the MP3 file")

    args = parser.parse_args()
    title = read_mp3_metadata(args.filename)
    analyze_audio_quality(args.filename)
    plot_librosa(args.filename,title)

if __name__ == "__main__":
    main()

