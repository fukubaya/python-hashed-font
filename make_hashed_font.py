#!/usr/bin/python
# -*- coding: utf-8 -*-

# 
# make_hashed_font.py
# 
# Created by FUKUBAYASHI Yuichiro on 2017/01/21
# Copyright (c) 2017, FUKUBAYASHI Yuichiro
# 
# last update: <2017/01/21 00:13:26>
# 


__version__ = "0.0.1"
usage = "%(prog)s [options] [args]"

import sys
import argparse
from hashlib import sha256

import fontTools.ttLib.tables
import fontTools.ttLib

DIGIT_KEYS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def create_parser():
    parser = argparse.ArgumentParser(
        description="make a hashed font from TrueType font",
        version=__version__)

    parser.add_argument(
        '-i', '--input',
        action='store',
        required=True,
        type=str,
        dest='input_ttf_path',
        help='input TTF file path')

    parser.add_argument(
        '-s', '--salt',
        action='store',
        type=str,
        dest='salt',
        help='salt sting [default: %(default)s]',
        default='SALT')

    parser.add_argument(
        '-o', '--output',
        action='store',
        type=str,
        dest='output_ttf_path',
        help='output TTF file path [default: %(default)s]',
        default='out.ttf')

    return parser

def main(args):

    # variables
    input_ttf_path = args.input_ttf_path
    output_ttf_path = args.output_ttf_path
    salt = args.salt

    # TrueType font object
    tt = fontTools.ttLib.TTFont(input_ttf_path)

    # start
    print "input: %s" % (input_ttf_path)

    
    chars = set()
    glyph_map = {}
    hmtx_map = {}

    glyphs_keys = sorted(tt['glyf'].glyphs.keys())
    salt = "salt"
    
    for g in glyphs_keys:
        digit = DIGIT_KEYS[int(sha256(g + salt).hexdigest(), 16) % 10]
        chars.add(g)
        glyph_map[g] = tt['glyf'].glyphs[digit]
        hmtx_map[g] = tt['hmtx'].metrics[digit]

    glyph_map['.notdef'] = tt['glyf'].glyphs['.notdef']

    for g in glyphs_keys:
        tt['glyf'].glyphs[g] = glyph_map[g]
        tt['hmtx'].metrics[g] = hmtx_map[g]

    # write file
    tt.save(output_ttf_path)
    print "wrote: %s" % (output_ttf_path)

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    main(args)
