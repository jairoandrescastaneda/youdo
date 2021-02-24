import random
import re

from bs4 import BeautifulSoup
from requests_html import HTMLSession

userAgents = [
    'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
]

random.shuffle(userAgents)


def getLastVideoInChannel(channelId):
    headers = {
        'User-Agent': userAgents[0],
    }
    video_url = 'https://www.youtube.com/channel/' + channelId + '/videos?view=0&sort=dd'

    # init an HTML Session
    session = HTMLSession()
    # get the html content
    response = session.get(video_url)

    # execute Java-script
    waitInSeconds = random.randint(1, 3)
    response.html.render(wait=waitInSeconds)

    source = BeautifulSoup(response.html.html, "html.parser")

    videos = source.findAll('a', class_='yt-simple-endpoint style-scope ytd-grid-video-renderer')

    return re.split(r"(\/\w*\?v=)", videos[0].attrs['href'])[2]