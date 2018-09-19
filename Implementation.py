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
    test = askdirectory()

    os.chdir(test)

    lista = episode_list_maker(test)

    splitter = sep_finder(lista)
    head, shift = header_finder(lista)
    tail = tail_finder(lista)

    instances_list = [EpisodeFilename(i, head, shift, tail, splitter) for i in lista]
    make_change(instances_list, kodi=True, dbrequest=False)
    # for instance in instances_list:
    #     print("mv \"%s\" \"%s\"" % (instance.original, kodi_change(instance.original, 2)))
