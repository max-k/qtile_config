# -*- coding: utf-8; -*-

from libqtile.config import Group

# Groups dictionnary {name: hotkey} (Mine reflects AZERTY Layout)
groups_dict = {"1": "ampersand",
               "2": "eacute",
               "3": "quotedbl",
               "4": "apostrophe",
               "5": "parenleft",
               "6": "minus",
               "7": "egrave",
               "8": "underscore",
               "9": "ccedilla"}

groups = sorted([Group(group) for group in groups_dict], key=lambda g: g.name)
