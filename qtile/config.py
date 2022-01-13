from typing import List

from libqtile import qtile
from libqtile import bar, layout, widget, extension, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.command import lazy

import fontawesome as fa
import os
import subprocess
import socket

from scripts import arcobattery
from libqtile.utils import guess_terminal
from scripts import getIP

ip = getIP.ip
mod = "mod4"
terminal =guess_terminal()

#####################
#      COLORS       #
#####################

# Load script to read colors from pywal
from scripts import pywal_colors

colors = pywal_colors.colors

blanco = "#e8eae9"
negro = "#000000"
gris = '#1e2126'

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

    Key([mod, "control"], "r", lazy.layout.normalize(), desc="Reset all window sizes"),

# Toggle between split and unsplit sides of stack.
# Split = all windows displayed | Unsplit = 1 window displayed but still with multiple stack panes

    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

# Toggle between different layouts as defined below

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

# Restart/Shutdown Qtile

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

# Switch keyboard layout
    
    Key([mod], "k", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),

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
    
    Key([mod], "F4", lazy.spawn(os.environ["HOME"] + "/Escritorio/scripts/dmenu-togglescreenlayout.sh")),
    Key([mod], "F5", lazy.spawn(os.environ["HOME"] + "/Escritorio/scripts/dmenu-audiosettings.sh")),
    Key([mod], "b", lazy.spawn("brave --new-window")),
    Key([mod], "d", lazy.spawn("dolphin")),
    Key([mod], "n", lazy.spawn("brave --new-window https://www.netflix.com/browse")),
    Key([mod], "o", lazy.spawn("okular")),
    Key([mod], "s", lazy.spawn("spotify")),
    Key([mod], "w", lazy.spawn("brave --new-window https://web.whatsapp.com/")),
    Key([mod], "x", lazy.spawn("slock")),
    Key([mod], "z", lazy.spawn(os.environ["HOME"] + "/Escritorio/scripts/dmenu-powersettings.sh")),
]


#######################################################################################################
#                                         GROUPS                                                      #
#######################################################################################################

__groups = {
        1: Group(name=fa.icons['terminal'], layout='bsp'),
        2: Group(name=fa.icons['globe'], layout='monadtall'),
        3: Group(name=fa.icons['folder-open'], layout='monadwide'),
        4: Group(name=fa.icons['code'], layout='monadwide'),
        5: Group(name=fa.icons['video'], layout='max'),
        6: Group(name=fa.icons['edit'], layout='max'),
        7: Group(name=fa.icons['music'], layout='max'),
        8: Group(name=fa.icons['comment-dots'], layout='max'),
        9: Group(name=fa.icons['skull-crossbones'], layout='monadwide'),
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

    layout.MonadWide(**layout_theme),
    
    layout.Max(),

    layout.Bsp(**layout_theme),

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
                    foreground=colors[4],
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
                   disable_drag = True,
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
                    font ='Hack Nerd Font',
                    format= '%H:%M',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e tty-clock -s')},
                ),

                widget.Spacer(
                    length = 2,
                ),

                widget.Pomodoro(
                    length_long_break = 25,

                ),

                widget.Spacer(
                    length=2,
                ),

                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    fontsize = 17,
                    text = fa.icons['sign-out-alt'],
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
                    format= fa.icons['calendar-alt'] + ' %a, %d de %h de %Y',
                    padding = 7,
                    foreground = negro,
                    background = colors[3],
                    mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal + " --hold -e cal -n 2")}
                ),
                
                widget.TextBox(
                    text="\uf0da",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[3],
                    background = colors[5],
                ),

                widget.KeyboardLayout(
                    configured_keyboards = ['es','us'],
                    fmt = fa.icons['keyboard'] + ' {}',
                    background = colors[5],
                    padding = 5,
                    foreground = negro,
                ),

                widget.TextBox(
                    text="\uf0da",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[5],
                    background = colors[2],
                ),

                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    text = fa.icons['user-secret'] + ' ' + ip,
                    padding = 5,
                    foreground = negro,
                    background = colors[2],
                    mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal + " --hold -e ip a")}, 
                ),

                widget.TextBox(
                    text="\uf0da",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[2],
                    background = colors[6],
                ),
                
                widget.CheckUpdates(
                    font = 'Font Awesome 5 Free',
                    update_interval=20,
                    foreground = negro,
                    colour_have_updates = negro,
                    colour_no_updates = negro,
                    distro = 'Arch_checkupdates',
                    display_format = fa.icons['sync'] + ' {updates} updates',
                    no_update_string = fa.icons['sync'] + ' updated',
                    padding = 5,
                    mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal + " -e sudo pacman -Syu")},
                    background = colors[6],
                ),

                widget.TextBox(
                    text="\uf0da",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[6],
                    background = colors[1],
                ),

                widget.CurrentLayoutIcon(
                    foreground = negro,
                    padding = 5,
                    scale = 0.7,
                    background = colors[1],
                ),

                widget.CurrentLayout(
                    foreground = blanco,
                    padding = 0,
                    background = colors[1],
                    fmt = '{} '
                ),
                
                widget.TextBox(
                    text="\uf0da",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[1],
                    background = "#00000000",
                ),
                
                widget.Spacer(length=bar.STRETCH),
               
                widget.WidgetBox(widgets=[
                    
                    widget.LaunchBar(
                        progs=[
                            (fa.icons['discord'], 'brave --new-window https://www.discord.com', 'Discord'),
                            (fa.icons['github'], 'brave --new-window https://www.github.com', 'Github'),
                            (fa.icons['reddit-alien'], 'brave --new-window https://www.reddit.com', 'Reddit'),
                            (fa.icons['twitch'], 'brave --new-window https://www.twitch.com', 'Twitch'),
                            (fa.icons['youtube'], 'brave --new-window https://www.youtube.com', 'Youtube'),
                            (fa.icons['spotify'], 'spotify', 'Spotify'),
                            (fa.icons['skype'], 'skypeforlinux', 'Skype'),
                            (fa.icons['linkedin'], 'brave --new-window https://www.linkedin.com', 'LinkedIn'),
                        ],
                    ),
                ],
                    font = 'Font Awesome 5 Free',
                    fontsize = 16,
                    foreground = blanco,
                    text_closed = fa.icons['dragon'],
                    text_open = fa.icons['docker'],
                ),
                     
                widget.Spacer(length=bar.STRETCH),
                
                widget.TextBox(
                    text="\uf0d9",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[1],
                    background = "#00000000",
                ),

                widget.Backlight(
                   font = 'Font Awesome 5 Free',
                   backlight_name = 'intel_backlight',
                   brightness_file = 'brightness',
                   fmt = fa.icons['sun'] + ' {}',
                   padding = 5,
                   foreground = blanco,
                   background = colors[1],
                ),

                widget.TextBox(
                    text="\uf0d9",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[6],
                    background = colors[1],
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
                    text="\uf0d9",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[2],
                    background = colors[6],
                ),

                widget.CPU(
                    font = 'Font Awesome 5 Free',
                    foreground = negro,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    format = fa.icons['brain'] + ' CPU {load_percent}%',
                    padding = 5,
                    background = colors[2]
                ),
                
                widget.TextBox(
                    text="\uf0d9",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[5],
                    background = colors[2],
                ),

                widget.DF(
                    visible_on_warn = False,
                    font = 'Font Awesome 5 Free',
                    fmt = fa.icons['hdd'] + ' {}',
                    foreground = negro,
                    background = colors[5],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e df -h')},
                    
                ),
                
                widget.TextBox(
                    text="\uf0d9",
                    fontsize = 37,
                    padding = 0,
                    foreground = colors[3],
                    background = colors[5],
                ),

                widget.Net(
                    font = 'Font Awesome 5 Free',
                    background = colors[3],
                    foreground = negro,
                    interface = 'wlo1',
                    padding = 5,
                    format = fa.icons['signal'] + ' {interface}: {down} ↓↑ {up}',
                     mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal + " --hold -e ip l")},  
                ),
              
            ],
            20,
            margin = [0, 0, 0, 0],
            background="#00000000",
        ),
    ),
]

def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

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
    Match(title='arandr'),
    Match(title='feh'),
    Match(title='Open File'),
    Match(title='Qalculate!'),
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
# cmd = ["xrandr --dpi 96"]

# for x in cmd:
#     os.system(x)
