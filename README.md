# Reality Hack -- Pi + Mic + SenseHAT Audio Visualizer

This is just a set of scripts that visualize raw audio coming in.
## Installation
```bash
sudo apt install python-pyaudio
```

## Running The Script(s)
My first pass is
```bash
cd reality_hack_audio_vis/scripts/
python audioVis.v1.py
```
which attempts to split the samples coming from the frame to chunks and display each chunk as a column.
This did not work as expected (and I have no idea what's happening) but it looks OK so it still lives here.

My second pass (based on the first)
```bash
cd reality_hack_audio_vis/scripts/
python audioVis.v2.py
```
attempts to get the volume for each frame and displays 8 past frames on the led matrix -- each column being a frame,
and each frame showing its volume. It might be easier for you to see it yourself.

## TODOs
I refactored a little bit, but it could use some additional performance enhancements and commenting.

In addition, it could use a filter/curve remapping to make the audio more reactive in the relevant voice ranges. The frame rate could also be tweaked to be dynamic and adjust to changing network conditions.

## Credits
The project is heavily based on the work done at https://github.com/scottlawsonbc/audio-reactive-led-strip/blob/master/python/visualization.py
Specifically, both the `config.py` and `microphone.py` is based on the scripts there.
