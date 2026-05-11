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
from selenium.common.exceptions import NoSuchElementException   


def createNewDriver(path):
    global driver
    os.system("taskkill /f /im tor.exe")
    torexe = os.popen(r"C:/Users/t/Desktop/TorBrowser/Browser/TorBrowser/Tor/Tor.exe")
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
        closeDriver()
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
     
def check_exists_by_css_selector(className):
    try:
        webdriver.find_element_by_css_selector(className)
    except NoSuchElementException:
        return False
    return True

def acceptConsentIfNeeded():
    try:
        driver.find_element_by_xpath("//*[contains(text(), 'I agree')]").click()
    except:
        print("No Consent Page Found matching -> I agree")
    try:
        driver.find_element_by_xpath("//*[contains(text(), 'I Agree')]").click()
    except:
        print("No Consent Page Found matching -> I Agree")


# Main
if __name__ == '__main__':
    driverPath = 'C:/Users/t/Desktop/chromedriver'
    #URL = "https://check.torproject.org/"
    URL = "https://www.youtube.com/shorts/SzqbeIQ--r8"
    lengthOfVideo = 23
    sessionViews = 100
    
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
            createNewDriver()
        sleep(random.randrange(round(lengthOfVideo / 2), lengthOfVideo))
        closeDriver()
        createNewDriver(driverPath)

        print("View counter: ", viewCounter)
