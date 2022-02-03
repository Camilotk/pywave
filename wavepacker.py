import signalgenerator as sg
import numpy as np
import wave as wv
import struct
import os

def pack(values, name):
    if not os.path.exists(os.path.join(os.getcwd(), 'out')):
        os.mkdir('out')
    audio = wv.open('out/' + name + '.wav', 'w')
    audio.setnchannels(1)
    audio.setframerate(sg.SAMPLE_RATE)
    audio.setsampwidth(2)
    audio.setnframes(len(values))
    for value in values:
        audio.writeframes(value.tobytes())
    audio.close()

def create_note(time, freq, name):
    pack(sg.generate_samples(time, freq), name)


create_note (1500.0, 261.63, 'c4')
# # create_audio(1500.0, 293.66, 'd4')
# # create_audio(1500.0, 329.63, 'e4')
# # create_audio(1500.0, 392.0, 'g4')
create_note(1500.0, 440.0, 'a4')
# # create_audio(1500.0, 493.88, 'b4')
