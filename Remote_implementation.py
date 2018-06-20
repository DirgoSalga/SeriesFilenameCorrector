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

    os.chdir(test)

    lista = episode_list_maker(test)

    splitter = sep_finder(lista)
    head, shift = header_finder(lista)
    tail = tail_finder(lista)

    instances_list = [EpisodeFilename(i, head, shift, tail, splitter) for i in lista]

    prompt = input("With additional Kodi changes?[y/n]\n")
    if prompt == "y":
        decision = True
    else:
        decision = False
    make_change(instances_list, kodi=decision)
