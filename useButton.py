# filename: main.py
from button_library import Button
from audio_library import AudioRecorder
import subprocess

button = Button()
#recorder = AudioRecorder(button)

recording_process = None


while True:
    if button.button_pressed():
        print("Button pressed")
        # Aquí puedes hacer lo que quieras cuando el botón esté presionado

    if button.button_released():
        print("Button released")

        # Aquí puedes hacer lo que quieras cuando el botón sea liberado
    button.wait()
