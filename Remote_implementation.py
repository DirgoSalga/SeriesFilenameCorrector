# -*- coding: utf-8 -*-
"""
Created on Wed May 30 10:50:20 2018

@author:Dirgo
"""
from sys import argv
import os
import json
from filename_corrector import *


def platzhalter(pfad):
    return str(pfad)


if __name__ == "__main__":
    test = platzhalter(*argv[1:])

    with open('secrets.json', 'r') as secretsfile:
        secret_dict = json.load(secretsfile)
    secret_key = secret_dict['API']

    os.chdir(test)

    lista = episode_list_maker(test)
    lista.sort()
    splitter = sep_finder(lista)
    head, shift = header_finder(lista)
    tail = tail_finder(lista)

    instances_list = [EpisodeFilename(i, head, shift, tail, splitter) for i in lista]

    prompt1 = input("With additional Kodi changes?[y/n]\n").lower() == "y"
    prompt2 = input("Do you wish to retrieve the names from an online database?[y/n]\n").lower() == "y"

    make_change(instances_list, kodi=prompt1, dbrequest=prompt2, api_secret=secret_key)
