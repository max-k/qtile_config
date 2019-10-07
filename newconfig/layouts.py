# -*- coding: utf-8; -*-

from libqtile import layout
from .colors import color_alert, color_frame, color_ok


# see http://docs.qtile.org/en/latest/manual/ref/layouts.html
layouts = [
    # layout.Stack(autosplit=False,
    #              num_stacks=1,
    #              border_focus=color_ok,
    #              border_normal=color_frame),
    layout.Columns(split=False,
                   num_columns=1,
                   border_focus=color_ok,
                   border_normal=color_frame),
    # layout.Max(),
    layout.Floating(border_focus=color_alert, border_normal=color_frame),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.RatioTile(),
    # layout.Slice(),
    # layout.Tile(border_focus=color_alert, border_normal=color_frame),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Unused yet.
floating_layout = layout.Floating(
    border_focus=color_alert,
    border_normal=color_frame,
    float_rules=[dict(role='buddy_list', ), ],
)
