# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:00:11 2018

@author:Dirgo
"""

from bs4 import BeautifulSoup
import requests


def site_scanner(url, **kwargs):
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, "html.parser")
    titles = soup.find_all(**kwargs)
    all_titles = ""
    for title in titles[1::2]:
        all_titles += "%s %s\n" % (title.attrs["episode"], title.text.strip())

    return all_titles.strip()


if __name__ == "__main__":
    from Search import *

    search = input("What show are you looking for?\n")
    print(site_scanner(mdatabase_search(search), class_="no_click open"))
