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


def generate_groups():
    groups = []
    for group in groups_dict:
        groups.append(Group(group))
    return sorted(groups, key=lambda g: g.name)


groups = generate_groups()
