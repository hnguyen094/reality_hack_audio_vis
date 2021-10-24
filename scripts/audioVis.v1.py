import numpy
from sense_hat import SenseHat
import pyaudio

import helper
import colors
import microphone

led_dim = (8, 8)

pa = pyaudio.PyAudio()
deviceIndex = -1
for x in xrange(0, pa.get_device_count()):
    info = pa.get_device_info_by_index(x)
    if info["name"] == "pulse":
        deviceIndex = info["index"]
        print "Pulse index: ", deviceIndex

sense = SenseHat()
sense.low_light = True

led_buffer = [colors.black] * led_dim[0] * led_dim[1]

def micUpdate(audioSamples):
    global led_buffer
    x, y = led_dim
    audioSamples /= 1e3

    chunkLen = len(audioSamples) / x
    chunks = helper.chopToChunks(audioSamples, chunkLen)
    arr = []
    for i in range(0, x):
        arr.append(max(abs(chunks.next())))
    for i in range(0, len(led_buffer)):
        color = colors.white if (float(i / y)/y < arr[i % x]) else colors.black
        led_buffer[i] = color
    sense.set_pixels(led_buffer)

microphone.start_stream(micUpdate)
