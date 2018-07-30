# -*- coding: utf-8 -*-
"""
Created on Wed May 30 14:01:04 2018

@author:Dirgo
"""

from selenium import webdriver
import webbrowser

# driver = r"D:\Dirgo\Documents\Web Drivers\chromedriver_win32\chromedriver.exe"


def mdatabase_search(input_text, season, tv=True):
    browser = webdriver.Firefox()
    browser.get(r"https://www.themoviedb.org/")
    search_field = browser.find_element_by_id("search_v4")

    search_field.send_keys(input_text)
    search_field.submit()

    results = browser.find_elements_by_class_name("title")
    listica = results[0].get_attribute("id").split("_")
    if tv:

        if listica[0] == "tv":
            id_number = listica[-1]
            print(id_number)
        browser.close()
        #season = int(input("Season? [1,2,3,...]\n"))
        return r"https://www.themoviedb.org/tv/%s/season/%d" % (id_number, season)
    else:
        if listica[0] == "movie":
            id_number = listica[-1]
            print(id_number)
        browser.close()
        return r"https://www.themoviedb.org/movie/%s" % id_number


if __name__ == "__main__":
    search = input("What show are you looking for?\n")
    webbrowser.open(mdatabase_search(search, tv=False))
