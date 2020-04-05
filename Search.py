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


def mdatabase_search(input_text, season, tv=True):
    if os.name is "posix":  # headless on rpi
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        browser = webdriver.Firefox(options=opts)
    else:
        driver = os.getcwd() + r"\Drivers\chromedriver.exe"
        browser = webdriver.Chrome(driver)
    browser.get(r"https://www.themoviedb.org/")
    lupa = browser.find_element_by_class_name("search")
    lupa.click()
    search_field = browser.find_element_by_id("search_v4")

    search_field.send_keys(input_text)
    search_field.send_keys(Keys.ENTER)
    try:
        results = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, "result")))
    except TimeoutException:
        print("Took too long to load page...")
    print(results[0].get_attribute("id"))
    listica = results[0].get_attribute("href").split("?")[0].split("/")[-2:]
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
