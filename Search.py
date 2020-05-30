# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:01:04 2020

@author:Dirgo
"""

import webbrowser
import tmdbsimple as db
import json


def db_search(title, secret_key, tv=True):
    """
    Finds the title in TMDB and returns the id code.
    :param title: <str> title of the series or movie
    :param tv: <bool> True if tv show, false if movie.
    :return: <int> id code
    """
    db.API_KEY = secret_key
    search = db.Search()
    if tv:
        response = search.tv(query=title)
    else:
        response = search.movie(query=title)
    results = search.results
    return results[0]["id"]


def episode_list_extraction(show_id, season, secret_key):
    """

    :param show_id:
    :param season:
    :return:
    """
    db.API_KEY = secret_key
    season_info = db.TV_Seasons(show_id, season).info()
    episode_names = ["{0:02d} {1}".format(i + 1, x["name"]) for i, x in enumerate(season_info["episodes"])]
    return episode_names


if __name__ == '__main__':
    id = db_search("Game of Thrones")
    print(episode_list_extraction(id, 1))
