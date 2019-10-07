# -*- coding: utf-8; -*-

import copy
import os
from socket import gethostname
from libqtile.config import Screen
from libqtile import bar, widget
from .colors import color_alert, color_frame, color_ok
from .widgets import Backlight, Battery
# from .widgets import ThermalSensor, Volume


# http://www.fileformat.info/info/unicode/char/search.htm


widget_defaults = dict(
    font='Nimbus Sans L',
    fontsize=14,
)


def get_wl_iface():
    for iface in os.listdir('/sys/class/net'):
        if iface.startswith('wl'):
            return iface


def battery_widget(battery):
    return Battery(
               **widget_defaults,
               battery=battery,
               charge_char=u'▲',
               discharge_char=u'▼',
               full_char='⚡',
               unknown_char='⚡',
               empty_char='\U0001F480',
               low_foreground=color_alert,
               high_foreground=color_ok,
               format='{char} {percent} {watt:.1f}W',
               short_format='{char} {percent}',
               show_short_text=False
           )


LEFT_SIDE_LIST = [
    widget.GroupBox(
        **widget_defaults,
        disable_drag=True,
        hide_unused=True,
        this_current_screen_border=color_frame,
        this_screen_border=color_frame,
        urgent_text=color_alert,
    ),
    widget.CurrentLayout(**widget_defaults)
]
PROMPT = widget.Prompt(**widget_defaults)
TASKLIST = widget.TaskList(
    **widget_defaults,
    border=color_frame,
    highlight_method='block',
    max_title_width=110,
    urgent_border=color_alert,
    txt_floating=u'🗗',
    txt_maximized=u'🗖',
    txt_minimized=u'🗕',
)
ONLY_MAIN_LIST = [
    widget.Systray(**widget_defaults),
]
if not gethostname().endswith('vm'):
    ONLY_MAIN_LIST.append(
        Backlight(
            **widget_defaults,
            backlight_name='intel_backlight'
        )
    )
    ONLY_MAIN_LIST.append(
        widget.Wlan(
            **widget_defaults,
            interface=get_wl_iface(),
            format='\U0001F4F6 {quality}',
            disconnected_message='W off'
        )
    )
BATTERY_LIST = []
RIGHT_SIDE_LIST = [
    # ThermalSensor(),
    # Volume(),
    widget.CPUGraph(
        graph_color=color_alert,
        fill_color='{}.5'.format(color_alert),
        border_color=color_frame,
        line_width=2,
        border_width=1,
        samples=60,
    ),
    widget.MemoryGraph(
        graph_color=color_alert,
        fill_color='{}.5'.format(color_alert),
        border_color=color_frame,
        line_width=2,
        border_width=1,
        samples=60,
    ),
    widget.NetGraph(
        graph_color=color_alert,
        fill_color='{}.5'.format(color_alert),
        border_color=color_frame,
        line_width=2,
        border_width=1,
        samples=60,
    ),
    widget.Clock(
        **widget_defaults,
        format='%d/%m %H:%M %p',
    )
]

for battery in ['BAT1', 'BAT0']:
    if os.path.islink(f'/sys/class/power_supply/{battery}'):
        BATTERY_LIST.append(battery_widget(battery))

screens = [
    Screen(
        top=bar.Bar([
            *LEFT_SIDE_LIST,
            PROMPT,
            TASKLIST,
            *ONLY_MAIN_LIST,
            *BATTERY_LIST,
            *RIGHT_SIDE_LIST
        ], 32,),
    ),
]


def detect_screens(qtile):
    _screens = copy.copy(screens)
    while len(_screens) < len(qtile.conn.pseudoscreens):
        _screens.append(
            Screen(
                top=bar.Bar([
                    *LEFT_SIDE_LIST,
                    TASKLIST,
                    *BATTERY_LIST,
                    *RIGHT_SIDE_LIST
                ], 32, ),
            )
        )
    return _screens
