import os
from pydub import AudioSegment
import eyed3
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import argparse

# Function to classify speech quality based on audio file duration
def analyze_audio_quality(file_path):
    """
    Analyze the quality of an audio file.

    Parameters:
    - file_path (str): The path to the audio file.

    Notes:
    - This function checks if the specified file exists.
    - It loads the audio file using the pydub library.
    - Basic information about the audio file is extracted, including duration, channels, sample width, and frame rate.
    - Loudness, represented by the average amplitude (root mean square), is measured.
    - The analysis results are printed to the console.

    Example:
    ```python
    analyze_audio_quality("path/to/your/audio/file.mp3")
    ```

    Output:
    ```
    Duration: 120.50 seconds
    Channels: 2
    Sample Width: 2 bytes
    Frame Rate: 44100 Hz
    Loudness: 0.05 dB
    ```
    """
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
    """
    Read metadata from an MP3 file and print information.

    Parameters:
    - file_path (str): The path to the MP3 file.

    Returns:
    - str: The title of the MP3 file.

    Notes:
    - This function checks if the specified file exists.
    - It loads the MP3 metadata using the eyed3 library.
    - Metadata information including title, artist, album, track number, year, and duration is printed to the console.
    - The function returns the title of the MP3 file.

    Example:
    ```python
    mp3_title = read_mp3_metadata("path/to/your/audio/file.mp3")
    print(f"Title: {mp3_title}")
    ```

    Output:
    ```
    Title: Example Title
    Artist: Example Artist
    Album: Example Album
    Track Number: 1
    Year: 2022
    Duration: 240.5 seconds
    ```
    """
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
    """
    Plot the waveform and spectrum of an audio file using the librosa library.

    Parameters:
    - file_path (str): The path to the audio file.
    - title (str): The title for the plot and the filename.

    Notes:
    - This function loads the audio file using librosa.
    - It plots the waveform and the spectrum of the audio.
    - The title is used to create a filename for the saved plot.
    - The plot is saved as a JPEG image in the 'images' directory.

    Example:
    ```python
    plot_librosa("path/to/your/audio/file.mp3", "Example_Plot_Title")
    ```

    Output:
    - The function generates and saves a plot of the waveform and spectrum in the 'images' directory.
    """
    import warnings
    warnings.filterwarnings("ignore")
    
    title = title.lower().strip().replace(" ","_")
    data, sampling_rate = librosa.load(file_path)
    
    fig,ax = plt.subplots(nrows=2, ncols=1, figsize = (12,8))
    librosa.display.waveshow(data, sr=sampling_rate,ax=ax[0])
    n_fft = 2048
    ft = np.abs(librosa.stft(data[:n_fft], hop_length = n_fft+1))
    ax[1].plot(ft)
    ax[1].set_title('Spectrum')
    ax[1].set_xlabel('Frequency Bin')
    ax[1].set_ylabel('Amplitude')
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

