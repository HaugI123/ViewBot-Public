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
    #pid = checkTor()
    #os.system("kill {}".format(pid))
    os.system("taskkill /f /im tor.exe")
    driver.quit()


def acceptConsentIfNeeded():
    try:
        driver.find_element_by_xpath(
            "//*[contains(text(), 'I agree')]").click()
    except:
        print("No Consent Page Found matching -> I agree")
    try:
        driver.find_element_by_xpath(
            "//*[contains(text(), 'I Agree')]").click()
    except:
        print("No Consent Page Found matching -> I Agree")

def driverCriteria():
    if date.today().isoweekday() <= 5:
        if datetime.datetime.utcnow().hour < 12:
            createNewDriver(driverPath)
        else:
            if random.randrange(0,10) <= 3:
              print("Weekday after hours with 30percent chance")
              createNewDriver(driverPath)  
            else:
                print("Skipped Driver")
                sleep(5)
                driverCriteria()
    else:
        if datetime.datetime.utcnow().hour >= 12:
            createNewDriver(driverPath)
        else:
            if random.randrange(0,10) <= 6:
              createNewDriver(driverPath) 


# Main
if __name__ == '__main__':
    driverPath = r'C:\Users\t\Desktop\chromedriver'
    URL = "https://check.torproject.org/"
    lengthOfVideo = 60
    sessionViews = 10000000

    driver = createNewDriver(driverPath)
    viewCounter = 0
    viewPerProxy = 0

    while viewCounter <= sessionViews:
        acceptConsentIfNeeded()
        sleep(2)
        try:
            driver.refresh()
        except Exception:
            viewPerProxy = 0
            closeDriver()
            createNewDriver(driverPath)
        sleep(5)
        closeDriver()
        
        driverCriteria()

        print("View counter: ", viewCounter)
