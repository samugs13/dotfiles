from libqtile import qtile
from libqtile import widget
from libqtile.lazy import lazy

import fontawesome as fa
import os
import re
import socket
import subprocess

terminal ="alacritty"

negro = "#282D39"
blanco = "#ffffff"
amarillo = "#b0ead9"
azul = "#31658c"
verde = "#037a77"
amarillo3 = "#ffbf00"

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
                   highlight_color = "#5d5d5d",
                   highlight_method="line",
                   this_current_screen_border = amarillo3,
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
                    foreground = verde,
                    padding = 0,
                    fontsize = 37
                ),

                widget.WindowName(
                    foreground=blanco,
                    background= verde,
                    font = "Hack Bold",
                    fontsize = 13,
                    max_chars = 100,
                    padding = 5,
                ),

                widget.TextBox(
                    text = '\uf0da',
                    background = negro,
                    foreground = verde,
                    padding = 0,
                    fontsize = 37
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = negro
                ),
               
                widget.Mpris2(
                    name='spotify',
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_chars=None,
                    stop_pause_text='',
                    markup = True,
                    foreground = blanco,
                    fontshadow = amarillo3,
                    padding = 4,
                    fmt = '🎶 {}',
                    fontsize = 13
                ),

                widget.Mpris2(
                    name='ncspot',
                    objname="org.mpris.MediaPlayer2.ncspot",
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_chars=None,
                    stop_pause_text='',
                    foreground = blanco,
                    fontshadow = amarillo3,
                    padding = 4,
                    fmt = '🎶 {}',
                    fontsize = 13
                ),

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

                widget.CurrentLayoutIcon(
                    background = azul,
                    foreground = blanco,
                    padding = 3,
                    scale = 0.7

                ),

                widget.CurrentLayout(
                    background = azul,
                    foreground = blanco,
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = azul
                ),
                
                widget.TextBox(
                    text = '| '+ fa.icons['brain'],
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
                    padding = 0,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e sensors')},
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
                    update_interval=20, 
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
                     mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn("/home/s4mb4/Escritorio/scripts/dmenu-powermanager.sh")}
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 8,
                    background = negro
                ),
              ]
    return widget_list