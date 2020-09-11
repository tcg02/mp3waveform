import wave
from mp3towav import *
import pylab
import pandas as pd
import numpy as np 

def get_wav_info(wav_file): 
    wav = wave.open(wav_file, "r")
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, "Int16")
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

def show_wave_n_spec(display_data):    
    pylab.subplot(211)
    pylab.plot(display_data)
    pylab.title('Wave from and spectrogram ')         
    pylab.show() 

filename, file_extension = os.path.splitext(sys.argv[1]) 

wavfile = mp3towav(filename)
sound_info, f = get_wav_info(wavfile)
df = pd.DataFrame (sound_info)
datalength = len(df)
pixelspersecond = 20
interval = f//pixelspersecond
compressed_df = df.groupby(np.arange(datalength)//interval).mean()

#show_wave_n_spec(compressed_df)


import json
import sys
digits = 2
json_content = {"sample_rate":22050,"samples_per_pixel":interval}
max_val = float(max(compressed_df[0]))
new_data = []
for x in compressed_df[0]:
    new_data.append(round(x / max_val, digits))

json_content["data"] = new_data

file_content = json.dumps(json_content, separators=(',', ':'))

with open(filename+".json", "w") as f:
    f.write(file_content)