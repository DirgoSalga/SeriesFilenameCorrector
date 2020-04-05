# -*- coding: utf-8 -*-
"""
Created on Wed May 30 10:50:20 2018

@author:Dirgo
"""
from sys import argv
import os
from filename_corrector import *


def platzhalter(pfad):
    return str(pfad)


if __name__ == "__main__":
    test = platzhalter(*argv[1:])

    os.system("export DISPLAY:=0")
    os.chdir(test)

    lista = episode_list_maker(test)

    splitter = sep_finder(lista)
    head, shift = header_finder(lista)
    tail = tail_finder(lista)

    instances_list = [EpisodeFilename(i, head, shift, tail, splitter) for i in lista]

    prompt1 = input("With additional Kodi changes?[y/n]\n")
    prompt2 = input("Do you wish to retrieve the names from an online database?[y/n]\n")
    prompt3 = input("Remove dash between episode number and episode name?[y/n]\n")
    prompt4 = input("Do you have a direct link?[y/n]\n")

    if prompt1 == "y":
        decision = True
    else:
        decision = False

    if prompt2 == "y":
        dbool = True
    else:
        dbool = False

    if prompt3 == "y":
        chbool = True
    else:
        chbool = False

    if prompt4 == "y":
        url = input("Link:\n")
        with_link = True
    else:
        url = None
        with_link = False

    make_change(instances_list, kodi=decision, dbrequest=dbool, directlink=with_link, link=url, dashremove=chbool)
