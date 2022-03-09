# import serial  # Serial imported for Serial communication
# import time  # Required to use delay functions
# # import pyautogui  # Required to to perform actions
# import serial.tools.list_ports
#
# import pyaudio
#
# find_port = ""
# for i in serial.tools.list_ports.comports():
#     if i[1] == "COM3":
#         find_port = i[1]
#     else:
#         print("enter an arduino device or check cable")
# ArduinoSerial = serial.Serial(find_port, 9600)  # Create Serial port object called arduinoSerialData
# time.sleep(2)  # wait for 2 seconds for the communication to get established
# while True:
#     incoming = str(ArduinoSerial.readline())  # read the serial data and print it as line
#     print(incoming)

 
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
dev_index=1
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

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    print(data)
    print(frames)
print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()