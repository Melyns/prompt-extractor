import os
import re
import time

def extract_prompt_from_file(filepath):
    try:
        with open(filepath, 'rb') as file:
            data = file.read()

        data_str = data.decode('utf-8', errors='ignore')
        
        start_marker = 'EXtparameters'
        start_index = data_str.find(start_marker)
        if start_index == -1:
            return None

        start_index += len(start_marker)

        end_index = data_str.find('Negative prompt:', start_index)
        if end_index == -1:
            end_index = data_str.find('Steps:', start_index)

        if end_index == -1:
            return None

        prompt = data_str[start_index:end_index].strip().replace('\x00', '')

        # Remove LORA triggers
        cleaned_prompt = re.sub(r'<[^>]+>', '', prompt).strip()

        return cleaned_prompt

    except Exception:
        return None

def process_image_file(filename, directory, prompts_folder, counters):
    image_path = os.path.join(directory, filename)
    prompt = extract_prompt_from_file(image_path)
    if prompt:
        text_filename = os.path.splitext(filename)[0] + '.txt'
        text_path = os.path.join(prompts_folder, text_filename)
        with open(text_path, 'w') as text_file:
            text_file.write(prompt)
        counters['processed'] += 1
        counters['prompts_generated'] += 1
        print(f"Extracted prompt from {filename} and saved to {text_filename}")
    else:
        counters['not_processed'] += 1
        print(f"No valid prompt found in {filename}, skipping.")

def process_images_in_directory(directory):

    image_files = [f for f in os.listdir(directory) if f.lower().endswith('.png')]

    counters = {
        'processed': 0,
        'not_processed': 0,
        'prompts_generated': 0
    }

    if image_files:
        prompts_folder = os.path.join(directory, 'Prompts')
        if not os.path.exists(prompts_folder):
            os.makedirs(prompts_folder)

        for filename in image_files:
            process_image_file(filename, directory, prompts_folder, counters)

        return counters, prompts_folder

    return counters, None

if __name__ == "__main__":
    start_time = time.time()

    directory = os.getcwd()
    counters, prompts_folder = process_images_in_directory(directory)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print()
    print(f"Job finished in: {elapsed_time:.2f} seconds")
    print(f"Images processed: {counters['processed']}")
    print(f"Prompts extracted: {counters['prompts_generated']}")
    print(f"Images without prompt: {counters['not_processed']}")
    print()

    if prompts_folder:
        print(f"Prompts can be found at {prompts_folder}")
    else:
        print("No images were processed.")
    print()
