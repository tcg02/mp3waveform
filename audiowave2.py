#!/usr/bin/env python
from pylab import *
import wave
import numpy as np
import matplotlib.pyplot as plt

def show_wave_n_spec(speech):
    spf = wave.open(speech,'r')
    sound_info = spf.readframes(-1)
    sound_info = np.fromstring(sound_info, 'Int16')

    f = spf.getframerate()
   
    subplot(211)
    plot(sound_info)
    title('Wave from and spectrogram of %s' % speech)

    subplot(212)
    spectrogram = specgram(sound_info, Fs = f, scale_by_freq=True,sides='default')
   
    show()
    spf.close()

fil = "audiowave.wav"

show_wave_n_spec(fil)