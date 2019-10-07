# -*- coding: utf-8; -*-

import os
import subprocess
from libqtile import hook
from .floating import floating_apps


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([os.path.join(home, '.config/qtile/autostart.sh')])


@hook.subscribe.client_new
def floating(window):
    # Manually defined floating apps
    if any((window.window.get_name() in floating_apps,
            # Dialogs
            window.window.get_wm_type() == 'dialog',
            # Pop-Up from another window
            window.window.get_wm_transient_for(),
            # Jdownloader
            window.window.get_name().startswith('win'))):
        window.floating = True


# @hook.subscribe.screen_change
# def restart_on_randr(qtile, ev):
#     # TODO only if numbers of screens changed
#     qtile.cmd_restart()
