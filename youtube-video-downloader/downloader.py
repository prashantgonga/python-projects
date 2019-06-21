#Simple Youtube Video Downloader
#https://github.com/nficano/pytube/issues/404 - The issue has been now fixed
#pip install pytube

from pytube import YouTube

print('Enter the YouTube video URL below')
videoLink = input()

yt = YouTube(videoLink)
videos = yt.streams.all()

s = 1
for video in videos:
    print(str(s) + " . "+str(video))
    s = s+1

print('Enter the number next to the video quality to download')

videoQuality = int(input())
downloadVideo = videos[videoQuality-1]

print('Enter the folder location where you want to save the file')
destination = input()
downloadVideo.download(destination)

print(" Video downloaded!")
