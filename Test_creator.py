# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 23:43:59 2018

This is just a function which should create a directory filled with files with the typical structure. This can be used
to test that the program is in fact working.

@author:Dirgo
"""
import os

test = ['The.Crown.S01E01.Wolferton.Splash.720p.WebRip.x264-[MULVAcoded].mp4',
        'The.Crown.S01E02.Hyde.Park.Corner.720p.WebRip.x264-[MULVAcoded].mp4',
        'The.Crown.S01E03.Windsor.720p.WebRip.x264-[MULVAcoded].mp4',
        'The.Crown.S01E04.Act.of.God.720p.WebRip.x264-[MULVAcoded].mp4',
        'The.Crown.S01E05.Smoke.and.Mirrors.720p.WebRip.x264-[MULVAcoded].mp4',
        'The.Crown.S01E06.Gelignite.720p.WebRip.x264-[MULVAcoded].mp4',
        'The.Crown.S01E07.Scientia.Potentia.Est.720p.WebRip.x264-[MULVAcoded].mp4',
        'The.Crown.S01E08.Pride.and.Joy.720p.WebRip.x264-[MULVAcoded].mp4',
        'The.Crown.S01E09.Assassins.720p.WebRip.x264-[MULVAcoded].mp4',
        'The.Crown.S01E10.Gloriana.720p.WebRip.x264-[MULVAcoded].mp4']

test2 = ['How I Met Your Mother S03E05 How I Met Everyone Else (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E10 The Yips (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E13 Ten Sessions (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E17 The Goat (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E20 Miracles (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E03 Third Wheel (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E16 Sandcastles in the Sand (1080p x265 Joy).m4v',
         "How I Met Your Mother S03E06 I'm Not That Guy (1080p x265 Joy).m4v",
         'How I Met Your Mother S03E09 Slapsgiving (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E15 The Chain of Screaming (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E04 Little Boys (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E18 Rebound Bro (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E11 The Platinum Rule (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E12 No Tomorrow (1080p x265 Joy).m4v',
         "How I Met Your Mother S03E02 We're Not from Here (1080p x265 Joy).m4v",
         'How I Met Your Mother S03E08 Spoiler Alert (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E07 Dowisetrepla (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E19 Everything Must Go (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E01 Wait for It (1080p x265 Joy).m4v',
         'How I Met Your Mother S03E14 The Bracket (1080p x265 Joy).m4v']

test3 = ['S1.Ep.01.Standing.Up.in.the.Milky.Way.mp4',
         'S1.Ep.02.Some.of.the.Things.That.Molecules.Do.mp4',
         'S1.Ep.03.When.Knowledge.Conquered.Fear.mp4',
         'S1.Ep.04.A Sky.Full.of.Ghost.mp4',
         'S1.Ep.05.Hiding.In.The.Light.mp4',
         'S1.Ep.06.Deeper.Deeper.Deeper.Still.mp4',
         'S1.Ep.07.The.Clean.Room-muxed.mp4',
         'S1.Ep.08.Sisters.of.the.Sun.mp4',
         'S1.Ep.09.The.Lost.Worlds.of.Planet.Earth.mp4',
         'S1.Ep.10.The.Electric.Boy.mp4',
         'S1.Ep.11.The.Immortals.mp4',
         'S1.Ep.12.The.World.Set.Free.mp4',
         'S1.Ep.13.Unafraid.of.the.Dark.mp4']


def create_tests(camino):
    test_path = camino + "/test"
    test_path2 = camino + "/test2"
    test_path3 = camino + "/test3"

    os.mkdir(test_path)
    os.mkdir(test_path2)
    os.mkdir(test_path3)
    for i in test:
        os.system("echo > \"%s/%s\"" % (test_path, i))
    for j in test2:
        os.system("echo > \"%s/%s\"" % (test_path2, j))
        for k in test3:
            os.system("echo > \"%s/%s\"" % (test_path3, k))


if __name__ == '__main__':
    from sys import argv

    create_tests(*argv[1:])
