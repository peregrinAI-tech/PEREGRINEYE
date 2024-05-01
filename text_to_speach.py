from gtts import gTTS
from pygame import mixer
import time

# Text to be converted to speech
text = "this is only a text that is all this is"

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False which tells the
# module that the converted audio should have a
# high speed
speech = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
speech.save("audios/text2.mp3")

# Initialize the mixer module
mixer.init()

# Load the mp3 file
mixer.music.load("audios/response.mp3")

# Set the volume
mixer.music.set_volume(0.05)

# Play the mp3 file
mixer.music.play()

# Wait for the audio to finish playing
while mixer.music.get_busy():
    time.sleep(1)

# Exit the program
exit()
