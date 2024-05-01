import pyaudio
import wave
from button_library import Button

class AudioRecorder:
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    BITRATE = 44100
    CHUNK_SIZE = 512

    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.device_id = 0  # Use device 0 by default
        self.button = Button()

    def record(self, output_filename):
        stream = self.audio.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.BITRATE,
            input=True,
            input_device_index=self.device_id,
            frames_per_buffer=self.CHUNK_SIZE
        )

        recording_frames = []

        while self.button.button_pressed():
            data = stream.read(self.CHUNK_SIZE)
            recording_frames.append(data)

        stream.stop_stream()
        stream.close()

        waveFile = wave.open(output_filename, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.BITRATE)
        waveFile.writeframes(b''.join(recording_frames))
        waveFile.close()

    def play(self, input_filename):
        wf = wave.open(input_filename, 'rb')

        stream = self.audio.open(
            format=self.audio.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )

        data = wf.readframes(self.CHUNK_SIZE)

        while data != b'':
            stream.write(data)
            data = wf.readframes(self.CHUNK_SIZE)

        stream.stop_stream()
        stream.close()

    def close(self):
        self.audio.terminate()
