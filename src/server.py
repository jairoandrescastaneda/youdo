#!/usr/bin/python
from __future__ import unicode_literals
import os

import youtube_dl

import SeleniumYoutubeClient
import ChannelList
import requests
import datetime

# downloadsPath = "/home/tomascayuelas/Sources/Own/youdo/downloads"
downloadsPath = "/mnt/UnsafeBox01/videos/youtube"


def downloadVideo(videoId):
    yld_opts = {
        'quiet': True,
        'verbose': False,
        'nooverwrites': True,
        'restrictfilenames': True,
        'writethumbnail': False,
        'noplaylist': True,
        'format': 'best'
    }

    with youtube_dl.YoutubeDL(yld_opts) as ydl:
        ydl.download([videoId])

    return videoId


def checkChannelFolder(folderName):
    return os.path.isdir(folderName)


def createChannelFolder(folderName):
    print(">> Creating folder")
    os.mkdir(folderName)

connection = ChannelList.pgConnection()

for channel in ChannelList.sqliteChannelFindAll(connection):
    print(channel["name"] + " --> " + channel["id"])

    os.chdir(downloadsPath)

    if not checkChannelFolder(channel["name"]):
        createChannelFolder(channel["name"])
    else:
        print("Already exists")

    os.chdir(downloadsPath + "/" + channel["name"])

    r = requests.get(channel["thumbnail"])
    thumbnailName = channel["id"] + "_thumbnail.jpg"
    with open(thumbnailName, "wb") as f:
        f.write(r.content)

    videoId = SeleniumYoutubeClient.getLastVideoInChannel(channel["id"])

    downloadVideo(videoId)

videoId = SeleniumYoutubeClient.getLastVideoInChannel("UCLheucogviCR5Bh8pNktURQ")

downloadVideo(videoId)