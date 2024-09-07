# prompt-extractor

Python script for extracting prompts from images generated with Forge or A1111.
> [!IMPORTANT]
> Only works with unmodified .png images. Images that were modified in editing software lose metadata and their prompt. 

## Usage

1. [Download](https://github.com/Melyns/prompt-extractor/archive/refs/heads/main.zip) and place `prompt-extractor.py` in the directory containing your images.  (Example: `D:\AI\Images\Forge`)

2. Open a terminal or command prompt in that directory.  (Example: `cd D:\AI\Images\Forge`)

3. Run the script with the following command:
   ```bash
   python .\prompt-extractor.py
   
It will create a subfolder & dump all the prompts there with file name matching the original image.
