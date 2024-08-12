# Main file for the PeregrinEye Prescription Reader project
from button_library import Button
import subprocess
import os
from PIL import Image
from gtts import gTTS
import google.generativeai as genai
import json

# Configure Gemini API
genai.configure(api_key="AIzaSyBAom9mA-tKAfhLmXvlpqaBqZHGnVgICik")
model = genai.GenerativeModel('models/gemini-pro-vision')

button = Button()

photo_directory = 'photos'
photo_name = 'prescription'
i = 1

def save_to_Audio(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(f'audios/response{i}.mp3')
    os.system(f'mpg321 audios/response{i}.mp3')

# New prompt for prescription extraction
prompt = """You are a digital assistant designed to extract information from medical prescriptions. 
Given an image of a prescription, extract and structure the following information in JSON format:
{
  "patient_name": "",
  "doctor_name": "",
  "date": "",
  "medications": [
    {
      "name": "",
      "dosage": "",
      "frequency": "",
      "duration": ""
    }
  ],
  "additional_instructions": ""
}
If any field is not present in the prescription, leave it as an empty string. Be accurate and concise in your extraction."""

while True:
    if button.button_pressed():
        print("Button pressed, taking picture of prescription...")
        
        # Take picture
        subprocess.run(['libcamera-jpeg', '-o', f'{photo_directory}/{photo_name}{i}.jpg', '-t', '2000'])
        print(f"Picture {i} taken successfully.")
        
        # Open and process image
        imagen = Image.open(f'{photo_directory}/{photo_name}{i}.jpg')
        flipped_image = imagen.transpose(Image.FLIP_LEFT_RIGHT)
        imagen_rotada = flipped_image.rotate(180)
        imagen_rotada.save(f'{photo_directory}/{photo_name}{i}.jpg')
        print(f"Picture {i} processed successfully.")
        
    if button.button_released():
        print("Button released, analyzing prescription...")
        response = model.generate_content([prompt, imagen_rotada])
        
        try:
            # Parse the JSON response
            prescription_data = json.loads(response.text)
            
            # Create a readable summary
            summary = f"Prescription for {prescription_data['patient_name']}. "
            summary += f"Prescribed by Dr. {prescription_data['doctor_name']} on {prescription_data['date']}. "
            
            for med in prescription_data['medications']:
                summary += f"Medication: {med['name']}, {med['dosage']}, {med['frequency']}, for {med['duration']}. "
            
            summary += f"Additional instructions: {prescription_data['additional_instructions']}"
            
            print(summary)
            save_to_Audio(summary)
        except json.JSONDecodeError:
            error_message = "Sorry, I couldn't properly read the prescription. Please try again."
            print(error_message)
            save_to_Audio(error_message)
        
        i += 1

    button.wait()
