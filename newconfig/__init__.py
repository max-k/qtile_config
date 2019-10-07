# -*- coding: utf-8; -*-
# flake8: noqa

from .floating import floating_apps
from .groups import groups
from .hooks import autostart, floating  # , restart_on_randr
from .keys import keys
from .layouts import layouts
from .mouse import mouse
from .screens import detect_screens, screens

main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True

# java app don't work correctly if the wmname isn't set to a name that happens
# to be on java's whitelist (LG3D is a 3D non-reparenting WM written in java).
wmname = 'LG3D'

# screens = []
#
#
# def main(qtile):
#     screens.extend(detect_screens(qtile))
