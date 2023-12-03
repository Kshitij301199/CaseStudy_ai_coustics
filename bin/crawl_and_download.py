import os,re
import requests
from bs4 import BeautifulSoup
import argparse

def download_audio(url: str, save_path:str):
    """
    Download an audio file from the given URL and save it to the specified path.

    Parameters:
    - url (str): The URL of the audio file to be downloaded.
    - save_path (str): The local path where the audio file will be saved.

    Raises:
    - requests.exceptions.RequestException: If there is an error during the download process.

    Note:
    - The function uses the requests library to send an HTTP GET request to the provided URL.
    - The downloaded audio file is saved in binary mode with a chunked approach to efficiently handle large files.
    - A timeout of 10 seconds is set for the HTTP request.
    - If the download is successful, a confirmation message is printed; otherwise, an error message is printed.
    """
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
    """
    Crawl a webpage, extract MP3 links, and return a list of specified number of links.

    Parameters:
    - url (str): The URL of the webpage to crawl.
    - num_links (int): The number of MP3 links to extract (default is 10).

    Returns:
    - List[str]: A list of MP3 links extracted from the webpage.

    Raises:
    - requests.exceptions.RequestException: If there is an error accessing the webpage.

    Note:
    - The function sends an HTTP request to the provided URL using the requests library.
    - It uses BeautifulSoup to parse the HTML content of the webpage.
    - MP3 links are identified by 'a' tags with an 'href' attribute containing '.mp3'.
    - The function returns a list of MP3 links, limited to the specified number.
    """
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
# webpage_url = "https://www.openculture.com/freeaudiobooks"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyse audio mp3 file")
    parser.add_argument("--link", required=True , help="URL to the Website")
    args = parser.parse_args()
    
    mp3_links = crawl_and_extract_mp3_links(args.link)
    for index, mp3_link in enumerate(mp3_links, start=1):
        # Create a filename based on the MP3 link
        names = mp3_link.split("/")
        pattern = re.compile(r".*\.mp3$")
        name = list(filter(pattern.match, names))[0]
        filename = os.path.join("../audio_files", f"audio_{name}")

        # Download the MP3 file
        download_audio(mp3_link, filename)