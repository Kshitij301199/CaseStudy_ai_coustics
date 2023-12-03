# CaseStudy_ai_coustics

## Overview

This project is designed to crawl the [Open Culture](https://www.openculture.com/freeaudiobooks) website for free audiobooks, download the available MP3 files, and perform a comprehensive analysis of the audio data.

## Features

1. **Web Crawling:** The script initiates a web crawl on the provided link to extract URLs of MP3 files available on the Open Culture website.

2. **Download MP3 Files:** The extracted MP3 URLs are used to download the corresponding audio files to a local directory.

3. **Audio Analysis:** The downloaded MP3 files undergo detailed analysis, including duration, channels, sample width, frame rate, and loudness. The analysis results are presented in a readable format.

# Getting Started

## Prerequisites

- Python 3.x installed
- Dependencies installed (specified in the `requirements.txt` file)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

# Directory Structure

    ├───audio_files
        ├── ...

    └───bin
        ├── audio_analysis.py
        ├── crawl_and_download.py
        └── test.ipynb

    └───images
        ├── ...

# Usage

    └───bin
        ├── crawl_and_download.py
        usage: crawl_and_download.py [-h] --link
                             LINK [--n N]    

        Analyse audio mp3 file

        optional arguments:
        -h, --help   show this help message and    
                    exit
        --link LINK  URL to the Website
        --n N        Number of links to download 
example link used: `https://www.openculture.com/freeaudiobooks`

    └───bin
        ├── audio_analysis.py
        usage: audio_analysis.py [-h] --filename
                         FILENAME

        Analyse audio mp3 file

        optional arguments:
        -h, --help           show this help        
                            message and exit      
        --filename FILENAME  Path to the MP3 file 

# Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Kshitij301199/CaseStudy_ai_coustics.git
   cd CaseStudy_ai_coustics
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

# License

This project is licensed under the [MIT License](LICENSE.md). Feel free to use, modify, and distribute the code according to the terms of the license.

# Acknowledgements

Special thanks to [Open Culture](https://www.openculture.com/freeaudiobooks) for providing free audiobooks, and to the open-source community for creating and maintaining the tools used in this project.

# Contributions

Contributions are welcome! If you encounter issues or have suggestions for improvements, please [open an issue](https://github.com/your-username/your-repository/issues) or submit a pull request.

# Author

Kshitij Kar
