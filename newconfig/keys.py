# -*- coding: utf-8; -*-

import copy
from os.path import dirname, expanduser
from libqtile.command import lazy
from libqtile.config import Key
from .groups import groups_dict as groups
from .help import shortcuts
from .functions import window_to_prev_group, window_to_next_group

SCRSHOT = expanduser('~/screenshot/$(date +%Y-%m-%d_%H-%M-%S).png')


TERMINAL_APP = "sakura"
TERMINAL_APP = "lxterminal"

win = 'mod4'
alt = 'mod1'
shift = 'shift'
ctrl = 'control'
tab = 'Tab'

# see http://docs.qtile.org/en/latest/manual/config/keys.html
base_keys = [

    # ---- System related commands (quit or reload) ----
    # Exit qtile
    Key([win, ctrl], "q",        lazy.shutdown()),
    # Shutdown computer
    Key([alt, ctrl], "q",        lazy.spawn("systemctl poweroff")),
    # Reboot computer
    Key([alt, ctrl], "r",        lazy.spawn("systemctl reboot")),
    # Reboot kernel
    Key([ctrl, shift], "r",      lazy.spawn("sudo systemctl kexec")),
    # Reload configuration
    Key([win, ctrl], "r",        lazy.restart()),

    # ---- Layout related commands ----
    # Select next layout
    Key([win, ctrl], "l",        lazy.next_layout()),
    # Select previous layout
    Key([win, ctrl, shift], "l", lazy.prev_layout()),

    # ---- Groups related commands ----
    # Select named group
    Key([win, ctrl], "g",        lazy.switchgroup()),
    # Switch between current/next
    Key([win], 'Escape',         lazy.screen.togglegroup()),
    # Switch to next group
    Key([alt, ctrl], 'Right',    lazy.screen.next_group()),
    # Switch to previous group
    Key([alt, ctrl], 'Left',     lazy.screen.prev_group()),

    # ---- Stack related commands ----
    # Split/unsplit current stack
    Key([win], "s",              lazy.layout.toggle_split()),
    # Select next stack
    Key([win], "Left",           lazy.layout.left()),
    # Select previous stack
    Key([win], "Right",          lazy.layout.right()),

    # ---- Layout specific keys (Stacks layout) ----
    # Swap stacks
    # Key([win], "space",          lazy.layout.rotate()),
    # Add a new stack to the layout
    # Key([win], "p",              lazy.layout.add()),
    # Remove a stack from the layout
    # Key([win], "m",              lazy.layout.delete()),
    # Move window to next stack
    # Key([win, ctrl], "Left",     lazy.layout.client_to_next()),
    # Key([win, ctrl], "Right",    lazy.layout.client_to_next()),

    # ---- Resizing related commands (Columns layout) ----
    # Grow window up
    Key([win, shift], "Up",     lazy.layout.grow_up()),
    # Grow window down
    Key([win, shift], "Down",   lazy.layout.grow_down()),
    # Grow stack left
    Key([win, shift], "Left",   lazy.layout.grow_left()),
    # Grow stack right
    Key([win, shift], "Right",  lazy.layout.grow_right()),
    # Normalize windows
    Key([win, shift], "less",    lazy.layout.normalize()),

    # ---- Window related commands ----
    # Select next window in stack
    Key([alt], tab,              lazy.layout.down()),
    Key([win], "Up",             lazy.layout.down()),
    # Select last window in stack
    Key([alt, shift], tab,       lazy.layout.up()),
    Key([win], "Down",           lazy.layout.up()),
    # Move window down
    Key([win, ctrl], "Up",       lazy.layout.shuffle_up()),
    # Move window up
    Key([win, ctrl], "Down",     lazy.layout.shuffle_down()),
    # Move window to previous stack
    Key([win, ctrl], "Left",     lazy.layout.shuffle_left()),
    # Move window to next stack
    Key([win, ctrl], "Right",    lazy.layout.shuffle_right()),
    # Move window to previous group
    Key([win, alt], "Left",      window_to_prev_group),
    # Move window to next group
    Key([win, alt], "Right",     window_to_next_group),
    # Toggle floating wine
    Key([win], 'f',              lazy.window.toggle_floating()),
    # Kill current window
    Key([win], "x",              lazy.window.kill()),

    # ---- Application related commands ----
    # Launch a custom command
    Key([win], "r",              lazy.spawncmd()),
    Key([alt], "F2",             lazy.spawncmd()),
    # Launch lxteminal
    Key([win], "Return",         lazy.spawn(TERMINAL_APP)),
    Key([win], "t",              lazy.spawn(TERMINAL_APP)),
    # Launch firefox
    Key([win], "w",              lazy.spawn("firefox")),
    Key([win, ctrl], "w",        lazy.spawn("firefox -private-window")),
    Key([win, alt], "w",         lazy.spawn("firefox -P")),
    # Launch Chromium
    Key([win, shift], "w",       lazy.spawn("chromium")),
    # Launch PCmanFM
    Key([win], "e",              lazy.spawn("pcmanfm")),
    # Lock screen using xscreensaver
    Key([win], 'l',              lazy.spawn('xlock -mode swarm '
                                            '+enablesaver +usefirst')),
    Key([], 'XF86ScreenSaver',   lazy.spawn('xlock -mode swarm '
                                            '+enablesaver +usefirst')),

    # ---- Stay awake mode ----

    Key([win, alt], "s", lazy.spawn(expanduser("~/.scripts/awake"))),

    # ---- Screenshot related commands ----
    Key([win], "p",
        lazy.spawn("bash -c \"mkdir -p {0} && "
                   "scrot -u {1} -e 'mirage $f'\"".format(dirname(SCRSHOT),
                                                          SCRSHOT))),
    Key([win, ctrl], "p",
        lazy.spawn("bash -c \"mkdir -p {0} && "
                   "scrot {1} -e 'mirage $f'\"".format(dirname(SCRSHOT),
                                                       SCRSHOT))),

    # ---- Multimedia related commands ----
    Key(
        [], "XF86AudioRaiseVolume",
        # lazy.spawn("amixer -c 0 -q set Master 2dB+")
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        # lazy.spawn("amixer -c 0 -q set Master 2dB-")
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2%")
    ),
    Key(
        [ctrl], "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-source-volume @DEFAULT_SOURCE@ +2%")
    ),
    Key(
        [ctrl], "XF86AudioLowerVolume",
        lazy.spawn("pactl set-source-volume @DEFAULT_SOURCE@ -2%")
    ),
    Key(
        [], "XF86AudioMute",
        # lazy.spawn("amixer -c 0 -q set Master toggle")
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")
    ),
    Key(
        [], "XF86AudioMicMute",
        lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle")
    ),

]


# ---- Groups related commands ----
def insert_groups(keys):
    for group in groups:
        # Move focused window to group
        keys.append(Key([win, ctrl], groups[group],
                        lazy.window.togroup(group)))
        # Switch to group
        keys.append(Key([win], groups[group],
                        lazy.group[group].toscreen()))
        # Move focused window to roup and switch to it
        keys.append(Key([win, alt], groups[group],
                        lazy.window.togroup(group),
                        lazy.group[group].toscreen()))


# ---- Help related commands ----
def insert_shortcuts(keys):
    keys.append(Key([win], "h", shortcuts(keys)))


def get_keys():
    _keys = copy.copy(base_keys)
    insert_groups(_keys)
    insert_shortcuts(_keys)
    return _keys


keys = get_keys()
