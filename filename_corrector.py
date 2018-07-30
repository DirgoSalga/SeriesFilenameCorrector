# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:51:40 2018

@author:Dirgo
"""

import os
from Search import mdatabase_search
from EpisodeListExtraction import site_scanner


class EpisodeFilename:
    """This is a class that breaks the name of a typical video file into its different components.
    This makes it much easier to modify and the process should actually be more or less automatic."""

    def __init__(self, filestring, head, shift, tail, splitter):
        self.original = filestring  # string
        self.key1 = head  # string
        self.key2 = tail  # string
        self.shift = shift  # int
        self.sep = splitter  # str
        self.formato = self.original.split(".")[-1]  # str

    def filename_modifier(self):
        ind1 = self.original.find(self.key1) + self.shift
        ind2 = self.original.find(self.key2)
        if ind2 == -1:
            short = self.original[ind1:]
        else:
            short = self.original[ind1:ind2]
        words = short.split(self.sep)
        new = "%s" % words[0]
        for word in words[1:-1]:
            if word == "and" or word == "the" or word == "of":
                new += " " + word
            else:
                new += " " + word.capitalize()
        new += "%s.%s" % (words[-1], self.formato)
        return new


def episode_list_maker(direct):
    """"This function decides what the most common format in the directory is.
    And makes a list of the files of this format.
    WARNING: It only works if the episodes have all the same format."""
    bruto = os.listdir(direct)
    formats_dict = {}
    for a in bruto:
        formato = a.split(".")[-1]
        formats_dict[formato] = formats_dict.get(formato, 0) + 1
    lista_formatos = formats_dict.items()
    count = []
    for _, c in lista_formatos:
        count.append(c)
    max_count = max(count)
    for _, c in lista_formatos:
        if c == max_count:
            vid_format = _
    netto = []
    for elemento in bruto:
        if elemento.split(".")[-1] == vid_format:
            netto.append(elemento)
    return netto


def sep_finder(filelist):
    """Function gets a list of filenames and figures out which character separates the words.
    Among the possibilities the following characters are considered: dot, space, dash  and underscore."""
    sep_sym_dict = {0: ".", 1: " ", 2: "-", 3: "_"}
    ai = bi = ci = di = 0
    while ai < 3 and bi < 3 and ci < 3 and di < 3:
        for name in filelist:
            a = len(name.split(".")) - 1  # Format always gets the last item of the separation, it shouldn't count.
            b = len(name.split(" "))
            c = len(name.split("-"))
            d = len(name.split("_"))
        len_list = [a, b, c, d]
        longest = max(len_list)
        indice = len_list.index(longest)
        if indice == 0:
            ai += 1
        elif indice == 1:
            bi += 1
        elif indice == 2:
            ci += 1
        else:
            di += 1
    results_list = [ai, bi, ci, di]
    winner = sep_sym_dict[results_list.index(max(results_list))]
    return winner


def header_finder(file_list):
    """This function is supposed to compare the beginnings of all filenames so it can decide which parts all filenames
    have in common and can be trimmed off the final result."""

    sep_symbol = sep_finder(file_list)
    for i in range(1, len(file_list)):
        a = file_list[i - 1].split(sep_symbol)
        b = file_list[i].split(sep_symbol)

        """This is the index of the last word that is identical in all filenames. Normally is the next one is the one I
        am really interested in"""
        same_to_index = 0

        if len(a) >= len(b):
            for j in range(1, len(a)):
                if a[j] == b[j]:
                    same_to_index += 1
                else:
                    break
        else:
            for j in range(1, len(b)):
                if a[j] == b[j]:
                    same_to_index += 1
                else:
                    break
    """At this point I know that they are all the same until same_to_index, let's check what happens with the next word
    if we break it down even further."""
    for k in range(1, len(file_list)):
        a = file_list[i - 1].split(sep_symbol)[same_to_index + 1]
        b = file_list[i].split(sep_symbol)[same_to_index + 1]

        same_to_index_in_word = 0
        if len(a) >= len(b):
            for l in range(1, len(a)):
                if a[l] == b[l]:
                    same_to_index_in_word += 1
            else:
                break
        else:
            for l in range(1, len(b)):
                if a[l] == b[l]:
                    same_to_index_in_word += 1
                else:
                    break
    """result is the portion word, after the last one that is identical on every file name, that is reapeated across all
    files."""
    result = file_list[2].split(sep_symbol)[same_to_index + 1][:same_to_index_in_word + 1]
    shift = len(result)  # This is just on how much we have to shift to slice the string properly

    return result, shift


def tail_finder(file_list):
    """This function is supposed to compare the endings of all filenames so it can decide which parts all filenames
        have in common and can be trimmed off the final result."""

    sep_symbol = sep_finder(file_list)
    for i in range(1, len(file_list)):
        a = file_list[i - 1].split(sep_symbol)[::-1]
        b = file_list[i].split(sep_symbol)[::-1]
        same_to_index = 0

        if len(a) >= len(b):
            for j in range(1, len(a)):
                if a[j] == b[j]:
                    same_to_index += 1
                else:
                    break
        else:
            for j in range(1, len(b)):
                if a[j] == b[j]:
                    same_to_index += 1
                else:
                    break
    result = file_list[1].split(sep_symbol)[::-1][same_to_index]
    return result


def kodi_change(original, season):
    """For this function to work, the names have to already have been
    corrected. This means in the format:
    e.g.: 01 Pilot.mp4"""
    formato = original.split(".")[-1]
    end_index = len(original) - len(formato) - 1
    sin_formato = original[:end_index]
    if season < 10:
        new = "%s_s0%de%s.%s" % (sin_formato.strip(), season, sin_formato[:2], formato)
    else:
        new = "%s_s%de%s.%s" % (sin_formato.strip(), season, sin_formato[:2], formato)
    return new


def make_change(episode_list, kodi=False, dbrequest=False):
    """The function takes a list of instances of the EpisodeFilename class"""

    if not dbrequest:
        if not kodi:
            for episode in episode_list:
                print("rename ", episode.original, "\t\t", episode.filename_modifier())
            prompt = input("Do you wish to make this filename changes? [y/n]")
            if prompt == "y":
                if os.name == "nt":
                    for episode in episode_list:
                        os.system("rename \"%s\" \"%s\"" % (episode.original, episode.filename_modifier()))
                elif os.name == "posix":
                    for episode in episode_list:
                        os.system("mv \"%s\" \"%s\"" % (episode.original, episode.filename_modifier()))
        elif kodi:
            season = int(input("Season? [1,2,3,...]"))
            for episode in episode_list:
                print("rename ", episode.original, "\t\t", kodi_change(episode.filename_modifier(), season))
            prompt = input("Do you wish to make this filename changes? [y/n]")
            if prompt == "y":
                if os.name == "nt":
                    for episode in episode_list:
                        os.system(
                            "rename \"%s\" \"%s\"" % (
                                episode.original, kodi_change(episode.filename_modifier(), season)))
                elif os.name == "posix":
                    for episode in episode_list:
                        os.system(
                            "mv \"%s\" \"%s\"" % (episode.original, kodi_change(episode.filename_modifier(), season)))
    elif dbrequest:
        show = input("What's the name of the show?\n")
        season = int(input("Season? [1,2,3,...]\n"))
        db_url = mdatabase_search(show, season)
        episode_txt = site_scanner(db_url, class_="no_click open").split("\n")
        if not kodi:
            for i in range(len(episode_list)):
                print("rename ", episode_list[i].original, "\t\t", episode_txt[i] + "." + episode_list[i].formato)
            prompt = input("Do you wish to make this filename changes? [y/n]")
            if prompt == "y":
                if os.name == "nt":
                    for i in range(len(episode_list)):
                        os.system("rename \"%s\" \"%s\"" % (
                            episode_list[i].original, episode_txt[i] + "." + episode_list[i].formato))
                elif os.name == "posix":
                    for i in range(len(episode_list)):
                        os.system("mv \"%s\" \"%s\"" % (
                            episode_list[i].original, episode_txt[i] + "." + episode_list[i].formato))
        elif kodi:
            for i in range(len(episode_list)):
                print("rename ", episode_list[i].original, "\t\t",
                      kodi_change(episode_txt[i] + "." + episode_list[i].formato, season))
            prompt = input("Do you wish to make this filename changes? [y/n]")
            if prompt == "y":
                if os.name == "nt":
                    for i in range(len(episode_list)):
                        os.system("rename \"%s\" \"%s\"" % (
                            episode_list[i].original,
                            kodi_change(episode_txt[i] + "." + episode_list[i].formato, season)))
                elif os.name == "posix":
                    for i in range(len(episode_list)):
                        os.system("mv \"%s\" \"%s\"" % (
                            episode_list[i].original,
                            kodi_change(episode_txt[i] + "." + episode_list[i].formato, season)))
