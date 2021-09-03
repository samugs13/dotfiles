from typing import List

from libqtile import qtile
from libqtile import bar, layout, widget, extension, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.command import lazy

import fontawesome as fa
import os
import re
import socket
import subprocess

from scripts import arcobattery
from libqtile.utils import guess_terminal

mod = "mod4"
terminal =guess_terminal()

#####################
#      COLORS       #
#####################

# Load script to read colors from pywal
from scripts import pywal_colors

colors = pywal_colors.colors

blanco = "#ffffff"
negro = "#000000"

# colors = ["#003b4c",     # Background
        # "#66a5ad",      
        # "#ececec",       
        # "#999999",     
        # "#73b8bf",     
        # "#50a5af",       
        # "#40848c",       
        # "#306369",       
        # "#204246",     
        # "#102123",       
        # ]

################################################################################################################
#                                                   KEYS                                                       #
################################################################################################################

keys = [

# Switch between windows

    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

# Move windows between left/right columns or move up/down in current stack.

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "space", lazy.layout.next(), desc="Switch window focus to other pane(s) of stack"),

# Super + function keys

    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle full screen"),

# Resize up, down, left, right

    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        desc="Grow window left",
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        desc="Grow window right",
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        desc="Grow window down",
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        desc="Grow window up",
    ),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

# Toggle between split and unsplit sides of stack.
# Split = all windows displayed | Unsplit = 1 window displayed but still with multiple stack panes

    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

# Toggle between different layouts as defined below

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

# Restart/Shutdown Qtile

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

# Function Keys

    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q sset Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master playback 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master playback 5%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),

# Apps and scripts

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(fontsize=11))),
    
    Key([mod], "F4", lazy.spawn("/home/s4mb4/Escritorio/scripts/dmenu-togglescreenlayout.sh")),
    Key([mod], "F5", lazy.spawn("/home/s4mb4/Escritorio/scripts/dmenu-audiosettings.sh")),
    Key([mod], "b", lazy.spawn("brave --new-window")),
    Key([mod], "d", lazy.spawn("dolphin")),
    Key([mod], "s", lazy.spawn("spotify")),
    Key([mod], "w", lazy.spawn("brave --new-window https://web.whatsapp.com/")),
    Key([mod], "x", lazy.spawn("slock")),
    Key([mod], "z", lazy.spawn("/home/s4mb4/Escritorio/scripts/dmenu-powersettings.sh")),
]


#######################################################################################################
#                                         GROUPS                                                      #
#######################################################################################################

__groups = {
        1: Group(name=fa.icons['terminal'], layout='monadtall'),
        2: Group(name=fa.icons['globe'], layout='monadtall'),
        3: Group(name=fa.icons['folder-open'], layout='monadtall'),
        4: Group(name=fa.icons['code'], layout='monadtall'),
        5: Group(name=fa.icons['video'], layout='maximized'),
        6: Group(name=fa.icons['photo-video'], layout='maximized'),
        7: Group(name=fa.icons['music'], layout='maximized'),
        8: Group(name=fa.icons['comment-dots'], layout='maximized'),
        9: Group(name=fa.icons['skull-crossbones'], layout='BSPlayout'),
 }

groups = [__groups[i] for i in __groups]
def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name),
        #    desc="move focused window to group {}".format(i.name)),
    ])


################################
#            LAYOUTS           #
################################

layout_theme = {"border_width":3,
                "border_focus": colors[5],
                "border_normal": colors[0],
                "single_border_width": 0,
                "margin":7,
                }

layouts = [

    layout.MonadTall(**layout_theme),

    layout.Max(name='maximized'),

    layout.Bsp(
        name='BSPlayout',
        **layout_theme),

    ]

################################
#            WIDGETS           #
################################

widget_defaults = dict(
    font='Hack',
    fontsize=14,
    padding = 2,
)
extension_defaults = widget_defaults.copy()

################################
#            SCREENS           #
################################

screens = [

    Screen(

        #TOP BAR
        top=bar.Bar(
            [
                widget.Spacer(
                    length=5,
                ),

                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    text = fa.icons["python"],
                    background = colors[0],
                    foreground = blanco,
                    fontsize = 17,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('dmenu_run')},
                ),

                widget.Spacer(
                    length = 5,
                ),

                widget.WindowName(
                    font = "Hack Bold",
                    background=colors[0],
                    foreground=colors[6],
                    empty_group_string="Desktop",
                    max_chars=90,
                    fontsize = 14,
                    padding = 1,
                ),

                widget.GroupBox(
                   font = 'Font Awesome 5 Free Solid',
                   active = colors[3],
                   inactive = colors[7],
                   highlight_method="block",
                   this_current_screen_border = colors[4],
                   block_highlight_text_color = blanco,
                   center_aligned = True,
                   background = colors[0],
                   fontsize = 14,
                ),

                widget.Spacer(
                    background=colors[0],
                    length = bar.STRETCH,
                ),
                
                widget.Systray(background = colors[0]),
                
                arcobattery.BatteryIcon(
                         padding=0,
                         scale=0.7,
                         y_poss=2,
                         theme_path="/home/s4mb4/.config/qtile/icons/battery_icons_horiz",
                         update_interval = 5,
                         background = colors[0]
                ),

                widget.Spacer(
                    length = 2,
                ),

                widget.Clock(
                    format= '%H:%M',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e tty-clock -s')},
                ),

                widget.Spacer(
                    length = 2,
                ),

                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    fontsize = 15,
                    text= fa.icons['sign-out-alt'] + ' ',
                    foreground=blanco,
                    padding = 5,
                    background = colors[0],
                    mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn("/home/s4mb4/Escritorio/scripts/dmenu-powersettings.sh")}
                ),

            ],
            
            size = 23,
            margin = [7, 7, 0, 7], #top,right,bottom,left
            background=colors[0],
        ),


        #BOTTOM BAR
        bottom=bar.Bar(
            [
               
                widget.Clock(
                    font = 'Font Awesome 5 Free',
                    format= fa.icons['calendar-alt'] + '  %a, %d de %h de %Y',
                    padding = 7,
                    foreground = negro,
                    background = colors[2],
                    mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal + " --hold -e cal -n 1")}
                ),
                
                widget.TextBox(
                    text="\uf0da",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[2],
                    background = colors[5],
                ),

                widget.CheckUpdates(
                    font = 'Font Awesome 5 Free',
                    update_interval=20,
                    foreground = negro,
                    colour_have_updates = negro,
                    colour_no_updates = negro,
                    distro = 'Arch_checkupdates',
                    display_format = fa.icons['sync-alt'] + ' {updates} updates',
                    no_update_string = fa.icons['sync-alt'] + ' no updates',
                    padding = 5,
                    mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal + " -e sudo pacman -Syu")},
                    background = colors[5],
                ),

                widget.TextBox(
                    text="\uf0da",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[5],
                    background = colors[3],
                ),

                widget.Backlight(
                   font = 'Font Awesome 5 Free',
                   backlight_name = 'intel_backlight',
                   brightness_file = 'brightness',
                   fmt = fa.icons['sun'] + ' {}',
                   padding = 5,
                   foreground = negro,
                   background = colors[3],
                ),

                widget.TextBox(
                    text="\uf0da",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[3],
                    background = colors[6],
                ),

                widget.ThermalSensor(
                    font = 'Font Awesome 5 Free',
                    foreground = negro,
                    padding = 5,
                    fmt = fa.icons['temperature-low'] + ' {}',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e sensors')},
                    background = colors[6]
                ),

                widget.TextBox(
                    text="\uf0da",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[6],
                    background = colors[1],
                ),

                widget.CPU(
                    font = 'Font Awesome 5 Free',
                    foreground = negro,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    format = fa.icons['brain'] + ' CPU {load_percent}%',
                    padding = 5,
                    background = colors[1]
                ),

                widget.TextBox(
                    text="\uf0da",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[1],
                    background = colors[4],
                ),

#                 widget.CurrentLayoutIcon(
#                     foreground = negro,
#                     padding = 5,
#                     scale = 0.7,
#                     background = colors[4],
#                 ),

                widget.CurrentLayout(
                    foreground = negro,
                    padding = 5,
                    background = colors[4]
                ),
                
                widget.TextBox(
                    text="\uf0da",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[4],
                    background = "#00000000",
                ),
                
                widget.Spacer(length=bar.STRETCH), #1140
                
                widget.Image(
                    filename = '~/.config/qtile/icons/luffy.jpg'
                ),

                widget.TextBox(
                    text = 's4mb4@mars',
                    font = 'Hack Bold',
                    foreground = blanco,
                    padding = 5,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)},
                ),

                widget.Spacer(length=2)
               
                ],
            20,
            margin = [0, 0, 0, 0],
            background="#00000000",
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='confirm'),
    Match(title='dialog'),
    Match(title='download'),
    Match(title='error'),
    Match(title='file_progress'),
    Match(title='notification'),
    Match(title='splash'),
    Match(title='toolbar'),
    Match(title='Arandr'),
    Match(title='feh'),
    Match(title='Open File'),
], **layout_theme)
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

# Alternative autostart:
#cmd = [
#     "commands",
#]
# 
#for x in cmd:
#    os.system(x)
