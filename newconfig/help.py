# -*- coding: utf-8; -*-

import os
import types
from libqtile.command import lazy

homedir = os.environ["HOME"]

keymap = {
    'mod4': 'win',
    'mod1': 'alt',
    'shift': 'shift',
    'control': 'ctrl',
    'Tab': 'tab',
    'ampersand': '1',
    'eacute': '2',
    'quotedbl': '3',
    'apostrophe': '4',
    'parenleft': '5'
}


def shortcuts(keys):
    _path = os.path.join(homedir, "qtile_shortcuts")
    sep = "\n{0:25}| ".format("")
    with open(_path, 'w') as _file:
        _file.write("{0:25}| {1:55}\n".format("KEYS COMBINATION",
                                              "COMMAND"))
        _file.write("{0:80}\n".format("=" * 80))
        for key in keys:
            _modifiers = [keymap.get(k, k) for k in key.modifiers]
            _key = keymap.get(key.key, key.key)
            combo = "{0}+{1}".format('+'.join(_modifiers), _key)
            _file.write("{0:25}| ".format(combo))
            cmds = []
            for cmd in key.commands:
                args = []
                for arg in cmd.args:
                    if isinstance(arg, types.FunctionType):
                        args.append("'{0}'".format(arg.__name__))
                    else:
                        args.append(repr(arg))
                args_str = ""
                if len(args) > 0:
                    args_str = "({0},)".format(", ".join(args))
                cmds.append("{0} {1}".format(cmd.name, args_str))
            _file.write("{0:55}\n".format(sep.join(cmds)))
            _file.write("{0:80}\n".format("-" * 80))
    return lazy.spawn("xterm -wf -e less {0}".format(_path))
