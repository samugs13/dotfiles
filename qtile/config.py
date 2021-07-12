from typing import List

from libqtile import qtile
from libqtile import bar, layout, widget, extension, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.command import lazy

import fontawesome as fa
import os
import re
import socket
import subprocess

import arcobattery

mod = "mod4"
terminal ="alacritty"

#####################
#      COLORS       #
#####################

negro = "#282D39"
blanco = "#ffffff"
gris = "#636A78"
amarillo = "#b0ead9"
azul = "#31658c"
verde = "#A3BE8C"
rojo = "#BF616A"
beige = "#8292b2"
amarillo2 = "#EBCB8B"

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

    Key([], "Print", lazy.spawn("spectacle")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")), 
    Key([], "XF86AudioMute", lazy.spawn("amixer -q sset Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master playback 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master playback 5%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")), 

# Apps
    
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        
        dmenu_prompt="DMENU",
        dmenu_font="Monospace-11",
        background = negro,
        selected_background=amarillo2,
        foreground="#ffffff",
        selected_foreground=negro,

    ))),

    Key([mod], "b", lazy.spawn("brave --new-window")),
    Key([mod], "d", lazy.spawn("dolphin")),
    Key([mod], "o", lazy.spawn("obs")),
    Key([mod], "s", lazy.spawn("spotify")),
    Key([mod], "t", lazy.spawn("teams")),  
    Key([mod], "y", lazy.spawn("skypeforlinux")),
    Key([mod], "w", lazy.spawn("brave --new-window https://web.whatsapp.com/")),
]


#######################################################################################################
#                                         GROUPS                                                      #
#######################################################################################################

# groups = [Group(i) for i in "12345"]

__groups = {
        1: Group(fa.icons['terminal']),
        2: Group(fa.icons['globe']),
        3: Group(fa.icons['folder-open']),
        4: Group(fa.icons['code']),
        5: Group(fa.icons['video']),
        6: Group(fa.icons['photo-video']),
        7: Group(fa.icons['spotify']),
        8: Group(fa.icons['whatsapp']),
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
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


################################
#            LAYOUTS           #
################################
    
layouts = [
    layout.MonadTall(
        border_width=3,
        border_focus = amarillo,
        border_normal = beige, 
        single_border_width=0, 
        margin=7,
    ),
]


################################
#            WIDGETS           #
################################

widget_defaults = dict(
    font='Hack',
    fontsize=12,
    padding = 2,
)
extension_defaults = widget_defaults.copy()    

def init_widget_list():
    widget_list = [

                widget.Sep(
                    linewidth = 0,
                    padding = 8,
                    background = negro
                ),

                widget.GroupBox(
                   font = "Ubuntu bold",
                   fontsize = 14,
                   margin_y = 3,
                   margin_x = 0,
                   padding_y = 5,
                   padding_x = 3,
                   borderwidth = 3,
                   active = blanco,
                   inactive = blanco,
                   highlight_color = gris,
                   highlight_method="line",
                   this_current_screen_border = amarillo,
                   background = negro,
                   foreground = blanco,
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = negro
                ),

                widget.TextBox(
                    text = '\uf0d9',
                    background = negro,
                    foreground = amarillo,
                    padding = 0,
                    fontsize = 37
                ),

                widget.WindowName(
                    foreground=negro,
                    background= amarillo,
                    font = "Hack",
                    fontsize = 13,
                    max_chars = 100,
                    padding = 10,
                ),

                widget.TextBox(
                    text = '\uf0da',
                    background = negro,
                    foreground = amarillo,
                    padding = 0,
                    fontsize = 37
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = negro
                ),

                widget.Notify(
                    padding = 4,
                    background = negro,
                    foreground = blanco,
                    foreground_low = amarillo2,
                    foreground_urgent = rojo,
                    default_timeout = 15,

                ),

                widget.Cmus(),

                widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = negro
                ),

                widget.TextBox(
                    text = '',
                    background = negro,
                    foreground = azul,
                    padding = 0,
                    fontsize = 37
                ),
                
                widget.TextBox(
                    text = fa.icons['brain'],
                    foreground = blanco,
                    background = azul,
                    padding = 3,
                ),

                widget.CPU(
                    foreground = blanco,
                    background = azul,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    format = 'CPU {freq_current}GHz {load_percent}%',
                    padding = 0
                ),
                
                widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = azul
                ),

                widget.TextBox(
                    text = '| '+ fa.icons['temperature-low'],
                    foreground = blanco,
                    background = azul,
                    padding = 3,
                ),

                widget.ThermalSensor(
                    background = azul,
                    foreground = blanco,
                    padding = 0
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = azul
                ),

                widget.TextBox(
                    text = '| ' + fa.icons['sync-alt'], 
                    background = azul,
                    foreground = blanco,
                    padding = 3,
                ),

                widget.CheckUpdates(
                    update_interval=60, 
                    foreground = blanco,
                    colour_have_updates = blanco,
                    background = azul,
                    distro = 'Arch_checkupdates',
                    display_format = '{updates} updates',
                    no_update_string = 'no updates',
                ),

                 widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = azul
                ),

                widget.TextBox(
                   text = '| ' + fa.icons['sun'],
                   background = azul,
                   foreground = blanco,
                   padding = 3,
                ),
                
                widget.Backlight(
                   backlight_name = 'intel_backlight',
                   brightness_file = 'brightness',
                   padding = 0,
                   background = azul,
                   foreground = blanco,
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = azul
                ),

                #widget.Battery(
                #    charge_char='ᐱ',
                #    discharge_char='ᐯ',
                #    full_char='⇋',
                #    low_percentaje = 0.15,
                #    background = azul,
                #    foreground = blanco,
                #    format = '{percent:2.0%} {char}',
                #    notify_below = 0.2,
                #    padding = 0,
                #    show_short_text = True,
                #    low_foreground = rojo,
                #    low_percentage = 0.2,
                #    update_interval = 1,
                #), 

               # widget.Sep(
               #     linewidth = 0,
               #     padding = 15,
               #     background = azul
               # ),

                widget.TextBox(
                   text = "| ",
                   background = azul,
                   foreground = blanco,
                   padding = 3,
                ),

                widget.Clock(
                    format='%A %d de %B - %H:%M',
                    background = azul,
                    foreground = blanco,
                    padding = 1,
                    mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal + " --hold -e cal -n 2")}
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 3,
                    background = azul
                ),

                widget.TextBox(
                    text = "|",
                    padding = 3,
                    background = azul,
                    foreground = blanco,
                ),

                widget.Systray(
                    padding =0,
                    icon_size = 18,
                    background = azul,
                ),
                
                widget.TextBox(
                    text = '\uf0da',
                    background = negro,
                    foreground = azul,
                    padding = 0,
                    fontsize = 37
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = negro
                ),

                widget.TextBox(
                     font = 'Ubuntu bold',
                     fontsize = 15,
                     text= '⏻',
                     background=negro,
                     foreground=blanco,
                     padding = 1,
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 8,
                    background = negro
                ),
              ]
    return widget_list


################################
#            SCREENS           #
################################

def init_screens():
    return [Screen(top=bar.Bar(init_widget_list(), size=20, background = negro))]

screens = init_screens()



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
])
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
#     "setxkbmap es",
#     "feh --bg-fill /home/s4mb4/.config/qtile/wallpapers/fsociety.png",
#     "compton &",
#]
# 
#for x in cmd:
#    os.system(x)


