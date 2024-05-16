#This is the code for the voice recording and playback test. It will record audio from the microphone and save it to a .wav file. It will then play the audio back to the user. 
# This code is used to test the microphone and speaker functionality of the AdaVoice system.
# This output is later supposed to be translated to text and then processed by openai but I never got to that point

import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1           # Number of channels
BITRATE = 44100        # Audio Bitrate
CHUNK_SIZE = 512       # Chunk size to 
RECORDING_LENGTH = 10  # Recording Length in seconds
WAVE_OUTPUT_FILENAME = "myrecording.wav"
audio = pyaudio.PyAudio()

info = audio.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", audio.get_device_info_by_host_api_device_index(0, i).get('name'))

print("Which Input Device would you like to use?")
device_id = int(input()) # Choose a device
print("Recording using Input Device ID "+str(device_id))

stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=BITRATE,
    input=True,
    input_device_index = device_id,
    frames_per_buffer=CHUNK_SIZE
)

recording_frames = []

for i in range(int(BITRATE / CHUNK_SIZE * RECORDING_LENGTH)):
    data = stream.read(CHUNK_SIZE)
    recording_frames.append(data)

stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(BITRATE)
waveFile.writeframes(b''.join(recording_frames))
waveFile.close()
