# -*- coding: utf-8 -*-
"""
Created on Wed May 30 10:39:57 2018

@author:Dirgo
"""
import os
from tkinter.filedialog import askdirectory
from tkinter import Tk
from filename_corrector import *

if __name__ == "__main__":
    master = Tk()
    master.withdraw()
    test = askdirectory(title="Choose the folder that contains the season you want to correct")

    os.chdir(test)

    lista = episode_list_maker(test)

    splitter = sep_finder(lista)
    head, shift = header_finder(lista)
    tail = tail_finder(lista)

    kodi_bool = input("Do you want to make the change for Kodi? [y/n]\n") == "y"
    db_bool = input("Do you want to extract the names from an online database? [y/n]\n") == "y"
    dash_change = input("Do you want to remove an extra dash between number and name? [y/n]\n") == "y"

    instances_list = [EpisodeFilename(i, head, shift, tail, splitter) for i in lista]
    make_change(instances_list, kodi=kodi_bool, dbrequest=db_bool, dashremove=dash_change)
    # for instance in instances_list:
    #     print("mv \"%s\" \"%s\"" % (instance.original, kodi_change(instance.original, 2)))
