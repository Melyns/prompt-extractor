# prompt-extractor

Simple python script for extracting prompts from images generated with ForgeUI or A1111.

**Important**: Only works with images that were saved as .png format. Only works with unmodified image outputs. Meaning if you postprocess an image in external software, the metadata will be lost & this script won't function. 

## Usage

1. [Download](https://github.com/Melyns/prompt-extractor/archive/refs/heads/main.zip) and place `prompt-extractor.py` in the directory containing your images.  (Example: `D:\AI\Images\Forge`)

2. Open a terminal or command prompt in that directory.  (Example: `cd D:\AI\Images\Forge`)

3. Run the script with the following command:
   ```bash
   python .\prompt-extractor.py
   
It will create a subfolder & dump all the prompts there with file name matching the original image.
