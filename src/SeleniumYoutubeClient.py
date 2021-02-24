import re
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def getLastVideoInChannel(channelId):
    options = Options()
    options.add_argument("--headless=true")
    options.add_argument("--window-size=1920,1200")

    # download Chrome Webdriver
    # https://sites.google.com/a/chromium.org/chromedriver/download
    # put driver executable file in the script directory
    # https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
    chrome_driver = os.path.join(os.getcwd(), "chromedriver")

    driver = webdriver.Chrome(options=options, executable_path=chrome_driver)

    url = 'https://www.youtube.com/channel/' + channelId + '/videos?view=0&sort=dd'

    driver.get(url)

    absoluteXpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/div[1]/div[1]/h3/a'
    element = driver.find_element_by_xpath(absoluteXpath)
    videoId = re.split(r"(\/\w*\?v=)", element.get_attribute('href'))[2]

    return videoId
