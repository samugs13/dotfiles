################################
#            WIDGETS           #
################################

import fontawesome as fa

from libqtile import widget, bar
from libqtile import qtile

from .keys import terminal 
from .colors import colors, blanco, negro
from .scripts import arcobattery
from .scripts import getIP
ip = getIP.ip

widget_defaults = dict(
    font='Hack',
    fontsize=14,
    padding = 2,
)
extension_defaults = widget_defaults.copy()

primary_widgets = [
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
                         theme_path="/home/s4mb4/.config/qtile/settings/icons/battery_icons_horiz",
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
]

secondary_widgets = [
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
]



