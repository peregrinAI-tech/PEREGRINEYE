#Main file for the PeregrinEye project , just be sure that you have all the libraries installed
# and run with python main.py
from button_library import Button
import subprocess
import os
from PIL import Image
from audio_library import AudioRecorder #It is not being used , never got able to make it work
from gtts import gTTS
from pygame import mixer
from dotenv import load_dotenv
import os
load_dotenv
import glob

import google.generativeai as genai
genai.configure(api_key="your-api-key")
model = genai.GenerativeModel('models/gemini-pro-vision')

button = Button()
# delete -- recorder = AudioRecorder()


photo_directory = 'photos'
photo_name = 'aroundMe'
# Read directory and all jpg
photos = glob.glob(os.path.join(photo_directory, '*.jpg'))

# Extract name on all photos
photo_numbers = [int(''.join(filter(str.isdigit, os.path.splitext(os.path.basename(photo))[0]))) for photo in photos]

# Identify max number
if photo_numbers:
    max_number = max(photo_numbers)
else:
    max_number = 0
i = max_number + 1
user_input = f"{photo_directory}/{photo_name}"
#initiate mixer to control audio playback
#mixer.init()
#mixer.music.set_volume(0.05)


#We create our speak function -- For whatever reason th quality of the audio is not the best
#as to when i create a wav and reproduce it with aplay but I just could not save a
# wav with this library
def save_to_Audio(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(f'audios/response{i}.mp3')
    os.system(f'mpg321 audios/response{i}.mp3')

#We define the prompt for our eyeAgent
prompt = """You are a a digital assistant designed to provide visual feedback for blind 
individuals, helping them navigate their surroundings. Upon receiving an image, describe 
in detail the key objects and structures, including their relative positions and contextual 
information. Your responses should be concise, clear, and informative, 
enabling users to orient themselves effectively. Additionally, learn and adapt to frequently 
visited places to provide personalized guidance. Be natural in your responses, and focus on 
providing valuable assistance to empower your users in their daily navigation."""

while True:
    if button.button_pressed():
        print("Button pressed")

        #recorder.record('audios/instructions.wav')

        # Here we take a picture and save it , for whatever reason a lot of prompt appears
        # in the console, probably all the processing of the image, it does not break anything 
        # but it is annoying, if we could ommit this and just take the picture quicker it would be
        # better
        subprocess.run(['libcamera-jpeg', '-o', user_input.lower()+f'{i}.jpg', '-t', '2000'])
        print(f"Picture {i} taken successfully.")
        # Opens Image taken
        imagen = Image.open(user_input.lower()+f'{i}.jpg')
        #Flips image because that is how gemni vision interprets it
        flipped_image = imagen.transpose(Image.FLIP_LEFT_RIGHT)
        # We rotate the image 180 degrees, this is because the camera is upside down
        imagen_rotada = flipped_image.rotate(180)

        # Saves rotated image
        imagen_rotada.save(user_input.lower()+f'{i}.jpg')
        print(f"Picture {i} transformed successfully.")
        i = i + 1
        
    if button.button_released():
        print("Button released")
        response = model.generate_content([prompt, imagen_rotada])
        print(response.text)
        save_to_Audio(response.text)
        

    button.wait()
