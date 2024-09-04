# prompt-extractor

Simple python script for extracting prompts from images generated with ForgeUI or A1111.

**Important**: Only works with images that were saved as .png format

## Usage

1. [Download](https://github.com/Melyns/prompt-extractor/archive/refs/heads/main.zip) and place `prompt-extractor.py` in the directory containing your images.  (Example: `C:\Users\User\Pictures\WebUI`)

2. Open a terminal or command prompt in that directory.  (Example: `cd C:\Users\User\Pictures\WebUI`)

3. Run the script with the following command:
   ```bash
   python .\prompt-extractor.py
   
It will create a subfolder & dump all the prompts there with file name matching the original image.

## How it works
This script reads each .png image file, extracts the prompt text from the metadata. Then it saves the extracted prompts as .txt files in a subfolder named Prompts.
