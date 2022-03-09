import time  # Required to use delay functions
import wave

import pyaudio
import serial.tools.list_ports

find_port = ""
# for i in serial.tools.list_ports.comports():
#     print(i)
#     if "COM3" in i:
#         find_port = "COM3"
#     else:
#         print("enter an arduino device or check cable")
serialPort = serial.Serial(
    port="COM3", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
time.sleep(2)  # wait for 2 seconds for the communication to get established

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
dev_index = 1
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=dev_index,
                )

print("* recording")

frames = []

while 1:
    data = stream.read(CHUNK)
    frames.append(data)
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.frames.writeframes(b''.join(frames))
    wf.close()

    serialPort.write(wf.wave.open("r"))

# stream.stop_stream()
# stream.close()
# p.terminate()
#

# wf.close()
