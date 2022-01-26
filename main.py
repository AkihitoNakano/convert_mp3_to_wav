import os
from glob import glob
from pydub import AudioSegment

target_dir = r'C:\Users\akihi\Desktop\before\mp3'
save_dir = r'C:\Users\akihi\Desktop\before\mp3\wav'

audio_files = glob(target_dir + '/*.mp3')
for file in audio_files:
    sound = AudioSegment.from_mp3(file)
    base_name = os.path.splitext(os.path.basename(file))[0]
    save_name = save_dir + '\\' + base_name + '.wav'
    sound.export(save_name, format="wav")
