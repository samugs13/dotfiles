from typing import List
from libqtile import hook
import os
import subprocess

from settings.keys import keys, mod
from settings.mouse import mouse
from settings.widgets import widget_defaults, extension_defaults, primary_widgets, secondary_widgets
from settings.layouts import layouts, floating_layout
from settings.groups import groups
from settings.screens import screens
from settings.colors import colors, blanco, negro

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    path = os.environ["HOME"]
    path += "/.config/qtile/"
    subprocess.call(path + "autostart.sh")
