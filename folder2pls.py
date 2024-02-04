import os
import audioread
import math

formats=('mp3','ogg')
pls="[playlist]\n"
count=0

for file in os.listdir():
    if os.path.isfile(file) and file.endswith(formats):
        count+=1
        pls+="File{0}={1}\n".format(count,os.path.abspath(file))
        pls+="Title{0}={1}\n".format(count,file.split("\\")[-1].split(".")[0])
        with audioread.audio_open(file) as f:
            duration=int(math.ceil(f.duration))
        pls+="Length{0}={1}\n".format(count,duration)
        print("Added {0} to playlist".format(file))
    else:
        print("{0} is a folder, or an unsupported file".format(file))
pls+="NumberOfEntries={0}\n".format(count)
pls+="Version=2"

with open("playlist.pls",'w',encoding="utf-8") as f:
    f.write(pls)

#print(pls)