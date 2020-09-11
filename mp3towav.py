# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:20:38 2020

@author: SDahal
"""
import os.path
from pydub import AudioSegment

def mp3towav(filename):                                                                       
    mp3file = filename+".mp3"
    wavfile = filename+".wav"    
    # convert wav to mp3           
    if(os.path.exists(wavfile)):
        print("WAV file already exists!")
        return wavfile    
    print("Converting to WAV format!")                                        
    sound = AudioSegment.from_mp3(mp3file)
    sound.export(wavfile, format="wav")
    return wavfile