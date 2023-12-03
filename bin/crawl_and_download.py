import os
import requests
from bs4 import BeautifulSoup
import re

def download_audio(url: str, save_path:str):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()  # Check if the request was successful

        # Save the audio file
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Audio file downloaded successfully: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading audio file: {e}")
        

# Function to crawl a webpage and extract all MP3 links
def crawl_and_extract_mp3_links(url:str, num_links:int = 10):
    try:
        # Send an HTTP request to the webpage
        response = requests.get(url,timeout=10)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links with an 'href' attribute containing '.mp3'
        mp3_links = [a['href'] for a in soup.find_all('a', href=re.compile(r'\.mp3'))][:num_links]

        return mp3_links

    except requests.exceptions.RequestException as e:
        print(f"Error accessing webpage: {e}")
        return []

# Example usage
webpage_url = "https://www.openculture.com/freeaudiobooks"
mp3_links = crawl_and_extract_mp3_links(webpage_url)

# Download each MP3 file
for index, mp3_link in enumerate(mp3_links, start=1):
    # Create a filename based on the MP3 link
    names = mp3_link.split("/")
    pattern = re.compile(r".*\.mp3$")
    name = list(filter(pattern.match, names))[0]
    filename = os.path.join("../audio_files", f"audio_{name}")

    # Download the MP3 file
    download_audio(mp3_link, filename)