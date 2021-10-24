import config

def chopToChunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def getPulseIndex():
    pa = pyaudio.PyAudio()
    for x in xrange(0, pa.get_device_count()):
        info = pa.get_device_info_by_index(x)
        if info["name"] == "pulse":
            return info["index"]

def foreach(lst, callback):
    for i in range(0, len(lst)):
        lst[i] = callback(i)

def dimColor(color, factor=config.DIM_FACTOR):
    return [channel / factor for channel in color]
