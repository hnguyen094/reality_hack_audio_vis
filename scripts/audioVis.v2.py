from sense_hat import SenseHat
import pyaudio

import microphone
import helper
import colors
import config

led_dim = config.LED_ARRAY_SIZE

sense = SenseHat()
sense.low_light = True

led_buffer = [colors.black] * led_dim[0] * led_dim[1]
maxVol = 1
rawVolWindow = [0] * led_dim[0]

def micCallback(audioSamples):
    global led_buffer, maxVol, rawVolWindow
    x, y = led_dim
    audioSamples /= 1e3

    vol = max(abs(audioSamples))
    if config.ADAPTIVE_VOLUME_NORMALIZATION and vol > maxVol:
        maxVol = vol

    rawVolWindow.pop(0)
    rawVolWindow.append(vol)

    def lightUp(index):
        normVol = float(rawVolWindow[index % led_dim[0]] / maxVol)
        threshold = float(index / led_dim[1]) / led_dim[1]
        return colors.black if normVol < threshold else colors.white

    helper.foreach(led_buffer, lightUp)
    sense.set_pixels(led_buffer)

microphone.start_stream(micCallback)
