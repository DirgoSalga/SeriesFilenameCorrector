# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:51:40 2018

@author:Dirgo
"""

import os
from Search import *


class EpisodeFilename:
    """This is a class that breaks the name of a typical video file into its different components.
    This makes it much easier to modify and the process should actually be more or less automatic."""

    def __init__(self, filestring, head, shift, tail, splitter):
        self.original = filestring  # string
        self.key1 = head  # string
        self.key2 = tail  # string
        self.shift = shift  # int
        self.sep = splitter  # string
        self.formato = self.original.split(".")[-1]  # string
        self.with_dash = None

    def filename_modifier(self, dashremover):
        """"dashremover [bool]: apply dash_remover method on function"""
        ind1 = self.original.find(self.key1) + self.shift
        ind2 = self.original.find(self.key2)
        if ind2 == -1:
            no_format = self.original[:self.original.find(self.formato) - 1]  # -1 because of the dot
            short = no_format[ind1:]
        else:
            short = self.original[ind1:ind2 - 1]  # Eliminate the separator at the end
        words = short.split(self.sep)
        new = words[0]
        for word in words[1:-1]:
            if word == "and" or word == "the" or word == "of":
                new += " " + word
            else:
                new += " " + word.capitalize()
        new += " %s.%s" % (words[-1], self.formato)
        if dashremover:
            self.with_dash = new
            return self.dash_remover()
        else:
            return new

    def dash_remover(self):
        """This function takes an already corrected filename and simply removes
        a dash between episode number and the name of the episode.

        Example:
            input = 01 - Pilot.mp4
            output = 01 Pilot.mp4"""

        pieces = self.with_dash.split("-")
        new = pieces[0].strip() + "".join(pieces[1:])
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
    same_index_list = list()
    for i in range(len(file_list)):
        a = file_list[i].split(sep_symbol)
        for m in range(len(file_list)):
            b = file_list[m].split(sep_symbol)

            """This is the index of the last word that is identical in all filenames. Normally is the next one is the one I
            am really interested in"""
            same_to_index_running = 0

            if len(a) <= len(b):
                for j in range(len(a)):
                    if a[j] == b[j]:
                        same_to_index_running += 1
                    else:
                        break
            else:
                for j in range(len(b)):
                    if a[j] == b[j]:
                        same_to_index_running += 1
                    else:
                        break
            same_index_list.append(same_to_index_running)
    same_to_index = min(same_index_list) - 1  # index actually starts at 0
    """At this point I know that they are all the same until same_to_index, let's check what happens with the next word
    if we break it down even further."""
    in_word_list = list()
    for k in range(len(file_list)):
        a = file_list[k].split(sep_symbol)[same_to_index + 1]
        for n in range(len(file_list)):
            b = file_list[n].split(sep_symbol)[same_to_index + 1]

            same_to_index_in_word_running = 0
            if len(a) <= len(b):
                for l in range(len(a)):
                    if a[l] == b[l]:
                        same_to_index_in_word_running += 1
                    else:
                        break
            else:
                for l in range(len(b)):
                    if a[l] == b[l]:
                        same_to_index_in_word_running += 1
                    else:
                        break
            in_word_list.append(same_to_index_in_word_running)

    same_to_index_in_word = min(in_word_list) - 1
    if same_to_index_in_word == -1:
        result = file_list[2].split(sep_symbol)[same_to_index]
        shift = len(result) + 1  # The separator is still included in this case
    elif same_to_index_in_word > -1:
        result = file_list[2].split(sep_symbol)[same_to_index + 1][:same_to_index_in_word + 1]
        shift = len(result)  # This is just on how much we have to shift to slice the string properly
    return result, shift


def tail_finder(file_list):
    """This function is supposed to compare the endings of all filenames so it can decide which parts all filenames
        have in common and can be trimmed off the final result."""
    file_list_no_format = list()
    for file in file_list:
        list_of_words = file.split(".")[:-1]
        file_no_format = str()
        if sep_finder(file_list) != ".":
            for word in list_of_words:
                file_no_format += word
        elif sep_finder(file_list) == ".":
            file_no_format += list_of_words[0]
            for word in list_of_words[1:]:
                file_no_format += "." + word
        file_list_no_format.append(file_no_format)
    sep_symbol = sep_finder(file_list_no_format)
    same_index_list = list()
    for i in range(len(file_list_no_format)):
        a = file_list_no_format[i].split(sep_symbol)[::-1]
        for m in range(len(file_list_no_format)):
            b = file_list_no_format[m].split(sep_symbol)[::-1]
            same_to_index_running = 0

            if len(a) <= len(b):
                for j in range(len(a)):
                    if a[j] == b[j]:
                        same_to_index_running += 1
                    else:
                        break
            else:
                for j in range(len(b)):
                    if a[j] == b[j]:
                        same_to_index_running += 1
                    else:
                        break
            same_index_list.append(same_to_index_running)
    same_to_index = min(same_index_list) - 1
    if same_to_index > -1:
        result = file_list_no_format[1].split(sep_symbol)[::-1][same_to_index]
    elif same_to_index <= -1:
        result = "__NO_TAIL_FOUND__"
    return result


def kodi_change(original, season):
    """For this function to work, the names have to already have been
    corrected. This means in the format:
    e.g.: 01 Pilot.mp4"""
    formato = original.split(".")[-1]
    end_index = len(original) - len(formato) - 1
    sin_formato = original[:end_index]
    if season < 10:
        new = "%s_s0%de%s.%s" % (sin_formato.strip(), season, sin_formato[:2].strip(), formato)
    else:
        new = "%s_s%de%s.%s" % (sin_formato.strip(), season, sin_formato[:2].strip(), formato)
    return new


def make_change(episode_list, kodi=False, dbrequest=False, dashremove=False, api_secret=None):
    """The function takes a list of instances of the EpisodeFilename class"""

    if not dbrequest:
        if not kodi:
            for episode in episode_list:
                print("rename ", episode.original, "\t\t", episode.filename_modifier(dashremove))
            prompt = input("Do you wish to make this filename changes? [y/n]")
            if prompt == "y":
                if os.name == "nt":
                    for episode in episode_list:
                        os.system("rename \"%s\" \"%s\"" % (episode.original, episode.filename_modifier(dashremove)))
                elif os.name == "posix":
                    for episode in episode_list:
                        os.system("mv \"%s\" \"%s\"" % (episode.original, episode.filename_modifier(dashremove)))
        elif kodi:
            season = int(input("Season? [1,2,3,...]"))
            for episode in episode_list:
                print("rename ", episode.original, "\t\t", kodi_change(episode.filename_modifier(dashremove), season))
            prompt = input("Do you wish to make this filename changes? [y/n]")
            if prompt == "y":
                if os.name == "nt":
                    for episode in episode_list:
                        os.system(
                            "rename \"%s\" \"%s\"" % (
                                episode.original, kodi_change(episode.filename_modifier(dashremove), season)))
                elif os.name == "posix":
                    for episode in episode_list:
                        os.system(
                            "mv \"%s\" \"%s\"" % (
                                episode.original, kodi_change(episode.filename_modifier(dashremove), season)))
    elif dbrequest:
        show = input("What's the name of the show?\n")
        season = int(input("Season? [1,2,3,...]\n"))
        show_id = db_search(show, api_secret)
        episode_txt = episode_list_extraction(show_id, season, api_secret)
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
