# -*- coding: utf-8 -*-
"""
Created on Wed May 30 14:01:04 2018

@author:Dirgo
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import webbrowser
import os

driver = os.getcwd() + r"\Drivers\chromedriver.exe"


def mdatabase_search(input_text, season, tv=True):
    if os.name is "posix":  # headless on rpi
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(800, 600))
        display.start()
        browser = webdriver.Firefox()
    else:
        import sys
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout)
        browser = webdriver.Firefox(firefox_binary=binary)
    browser.get(r"https://www.themoviedb.org/")
    search_field = browser.find_element_by_id("search_v4")

    search_field.send_keys(input_text)
    search_field.send_keys(Keys.ENTER)
    try:
        results = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, "result")))
    except TimeoutException:
        print("Took too long to load page...")
    # results = browser.find_elements_by_class_name("title")
    print(results[0].get_attribute("id"))
    listica = results[0].get_attribute("id").split("_")
    if tv:

        if listica[0] == "tv":
            id_number = listica[-1]
            print(id_number)
        browser.close()
        return r"https://www.themoviedb.org/tv/%s/season/%d" % (id_number, season)
    else:
        if listica[0] == "movie":
            id_number = listica[-1]
            print(id_number)
        browser.close()
        return r"https://www.themoviedb.org/movie/%s" % id_number


if __name__ == "__main__":
    search = input("What show are you looking for?\n")
    webbrowser.open(mdatabase_search(search, 2, tv=True))
