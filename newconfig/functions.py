# -*- coding: utf-8; -*-

from libqtile.command import lazy


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        idx = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[idx - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        idx = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[idx + 1].name)


# kick a window to another screen (handy during presentations)
def kick_to_next_screen(qtile, direction=1):
    current_scr_index = qtile.screens.index(qtile.currentScreen)
    other_scr_index = (current_scr_index + direction) % len(qtile.screens)
    othergroup = None
    for group in qtile.cmd_groups().values():
        if group['screen'] == other_scr_index:
            othergroup = group['name']
            break
    if othergroup:
        qtile.moveToGroup(othergroup)
