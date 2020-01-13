from __future__ import unicode_literals
import youtube_dl
import cv2
import os
import time
import ctypes
import os.path
from os import startfile
import os
path = (os.path.dirname(os.path.realpath(__file__))) 

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=dQw4w9WgXcQ'])
if os.path.isfile('Rick Astley - Never Gonna Give You Up (Video)-dQw4w9WgXcQ.mp4'):
    filename = 'Rick Astley - Never Gonna Give You Up (Video)-dQw4w9WgXcQ.mp4'
else:
    filename = 'Rick Astley - Never Gonna Give You Up (Video)-dQw4w9WgXcQ.mkv'


vidcap = cv2.VideoCapture(filename)
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    name = "image"+str(count)+".jpg"
    if hasFrames:
        cv2.imwrite(name,image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
#plays music
startfile(filename)

SPI_SETDESKWALLPAPER = 20
num=1

while num < 425:
    imgloc = str(path)+ '\image' + str(num) + '.jpg'
    #print(imgloc)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imgloc , 0)
    num = num + 1
    #print(num)
    time.sleep(0.5)




    #make gif
#clip = VideoFileClip('Rick Astley - Never Gonna Give You Up (Video)-dQw4w9WgXcQ.mp4')
#clip.write_gif('rickrolled.gif',fps = 6 , program='ffmpeg')








