# prompt-extractor

Simple python script for extracting prompts from images generated with ForgeUI or A1111.

## Usage

1. Place `prompt-extractor.py` in the directory containing your images.  (Example: `C:\Users\User\Pictures\WebUI`)

2. Open a terminal or command prompt in that directory.  (Example: `cd C:\Users\User\Pictures\WebUI`)

3. Run the script with the following command:
   ```bash
   python ./prompt-extractor.py
4. Done

## How it works
This script reads each image file, extracts the prompt text from its metadata, and cleans it by removing any unwanted characters and tags. Then it saves the extracted prompts as .txt files in a subfolder named Prompts.
