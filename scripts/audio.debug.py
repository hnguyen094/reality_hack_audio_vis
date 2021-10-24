import pyaudio
pa = pyaudio.PyAudio()
chosen_device_index = -1
for x in xrange(0, pa.get_device_count()):
    info = pa.get_device_info_by_index(x)
    print pa.get_device_info_by_index(x)
    if info["name"] == "pulse":
        chosen_device_index = info["index"]
        print "Chosen index: ", chosen_device_index
