# Reality Hack -- Pi + Mic + SenseHAT Audio Visualizer
## Abstract
When working with a remote team, we often either feel overimmersed (e.g. "Zoom fatigue") or underimmersed (e.g. feelings of isolation). 
For some, being passively monitoring a discord channel seems to fit in this middle-ground that is not unlike being in a room together.

For me, I wanted to use our "Reality Kit" (Raspberry Pi 4 + Microphone + SenseHAT + Camera) to create another middle-ground of copresence by visualizing another kit's audio volume. This way, one person can 'see' collaboration and liveliness on the other end, without needing to worry about informational leakage or distracting conversations that would happen in a Discord voice channel.

This could happen within the team, or between teams, or between a remote hacker and a public space on-site. The update rate (can be configured) is 10FPS, where each frame requires a single integer/float sent over the network.


This is just a set of scripts that visualize ~~raw~~ microphone audio coming in.
## Installation
```bash
sudo apt install python-pyaudio
pip install numpy
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

**Shane's Idea** each teammate can have a different color for visualization (in the intra-team case) and you can have more granularity in who's talking (or at least, which reality kit is recording) to have increased copresence.
**Austin's Idea** why not an intercom/walkie-talkie system, allowing one kit to connect to the other end for quick messages?

## Credits
The project is heavily based on the work done at https://github.com/scottlawsonbc/audio-reactive-led-strip/blob/master/python/visualization.py
Specifically, both the `config.py` and `microphone.py` is based on the scripts there.
