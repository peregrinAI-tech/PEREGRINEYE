#Main file for the PeregrinEye project, just be sure that you have all the libraries installed
# and run with python main.py
from button_library import Button
import subprocess
import os
from PIL import Image
from audio_library import AudioRecorder #It is not being used, never got able to make it work
from gtts import gTTS
from pygame import mixer
from dotenv import load_dotenv
import os
import glob
import openai
from base64 import b64encode

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

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

#We create our speak function
def save_to_Audio(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(f'audios/response{i}.mp3')
    os.system(f'mpg321 audios/response{i}.mp3')

#We define the prompt for our eyeAgent
prompt = """You are a digital assistant designed to provide visual feedback for blind 
individuals, helping them navigate their surroundings. Upon receiving an image, describe 
in detail the key objects and structures, including their relative positions and contextual 
information. Your responses should be concise, clear, and informative, 
enabling users to orient themselves effectively. Additionally, learn and adapt to frequently 
visited places to provide personalized guidance. Be natural in your responses, and focus on 
providing valuable assistance to empower your users in their daily navigation."""

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return b64encode(image_file.read()).decode('utf-8')

while True:
    if button.button_pressed():
        print("Button pressed")
        #recorder.record('audios/instructions.wav')
        # Here we take a picture and save it
        subprocess.run(['libcamera-jpeg', '-o', user_input.lower()+f'{i}.jpg', '-t', '2000'])
        print(f"Picture {i} taken successfully.")
        # Opens Image taken
        imagen = Image.open(user_input.lower()+f'{i}.jpg')
        #Flips image because that is how the camera interprets it
        flipped_image = imagen.transpose(Image.FLIP_LEFT_RIGHT)
        # We rotate the image 180 degrees, this is because the camera is upside down
        imagen_rotada = flipped_image.rotate(180)
        # Saves rotated image
        imagen_rotada.save(user_input.lower()+f'{i}.jpg')
        print(f"Picture {i} transformed successfully.")
        i = i + 1
        
    if button.button_released():
        print("Button released")
        
        # Encode the image
        base64_image = encode_image(user_input.lower()+f'{i-1}.jpg')
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=300
        )
        
        description = response.choices[0].message.content
        print(description)
        save_to_Audio(description)
        
    button.wait()