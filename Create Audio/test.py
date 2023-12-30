import pandas as pd
from gtts import gTTS
import os

def text_to_speech(text_input, output_audio_path, lang='en-us'):
    # Create a gTTS object with the specified language and gender
    tts = gTTS(text=text_input, lang=lang, slow=False)

    # Save the speech as an audio file
    tts.save(output_audio_path)

def generate_audio_from_csv(csv_file_path, output_folder_path, lang='en-us'):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)

    # Iterate through each row and generate audio
    for index, row in df.iterrows():
        text_input = row['text']
        output_audio_path = f"{output_folder_path}/output{index + 1}.mp3"
        text_to_speech(text_input, output_audio_path, lang=lang)

if __name__ == "__main__":
    csv_file_path = "texts.csv"
    output_folder_path = "output"

    generate_audio_from_csv(csv_file_path, output_folder_path, lang='en-us')
