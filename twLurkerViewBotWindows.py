from time import sleep, time
from selenium import webdriver
import random
import math
from selenium.webdriver.chrome.webdriver import WebDriver
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import sys
from DiscordBot import urlList
import os
from selenium.webdriver.common.by import By
import subprocess as sp
import datetime
from datetime import date


def createNewDriver(path):
    global driver
    torexe = os.popen(
        r'C:\Users\t\Desktop\TorBrowser\Browser\TorBrowser\Tor\tor')
    PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % PROXY)
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-geolocation")
    options.add_argument("--disable-media-stream")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option(
        "prefs", {"profile.default_content_settings.cookies": 2})

    driver = webdriver.Chrome(chrome_options=options, executable_path=path)
    try:
        driver.get(URL)
        sleep(7)
    except Exception:
        driver.close()
        createNewDriver(path)
    return driver


def checkTor():
    '''Returns a boolean based on if tor is running'''
    result = sp.check_output('pgrep tor', shell=True).decode('utf-8')
    return result


def closeDriver():
    global driver
    pid = checkTor()
    os.system("kill {}".format(pid))
    driver.quit()


# Main
if __name__ == '__main__':
    driverPath = r'Chrome\chromedriver105.exe'
    URL = input("Enter URL: ")

    # Sleeps before creating first driver -> Wait between 2 minute and 15 minutes
    randInt = random.randrange(180, 900)
    print("Sleeping for: ", randInt/60)
    sleep(randInt)

    viewCounter = 0
    viewPerProxy = 0

    while True:
        # Creates a new driver
        createNewDriver(driverPath)
        # Sleeps during driver operation -> Wait between 30 minute and 2 hours
        sleep(random.randrange(1800, 7200))
        # Close the driver
        closeDriver()
        # Sleeps after driver completion -> Wait between 3 minute and 15 minutes
        sleep(random.randrange(180, 900))
